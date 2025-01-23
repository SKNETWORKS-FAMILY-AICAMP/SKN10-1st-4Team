import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px

st.title("📊 지역별 자동차 등록 현황")
st.divider()

tab1, tab2 = st.tabs(['파이차트', '지도차트'])

connection = pymysql.connect(
    host = "localhost",
    user = "SKN10_4team",
    password = "skn1234",
    database = "SKN10_4team_1st",
    charset = "utf8"
)

cursor = connection.cursor(pymysql.cursors.DictCursor)

# 연도 데이터 쿼리
year_data = """
SELECT DISTINCT year
FROM Car
;
"""
cursor.execute(year_data)
years = cursor.fetchall()
year_list = [year['year'] for year in years]


with tab1:
    # 파이차트에서 연도 선택
    selected_year1 = st.selectbox("파이차트 연도 선택", year_list, index=year_list.index('2022'))

    st.divider()

    # 데이터 쿼리
    car_data = f"""
    SELECT City_m.CityName, City_m.CityName2, City_m.Latitude, City_m.Longitude, Car.CarCount
    FROM Car
    JOIN City_m ON Car.CityID = City_m.CityID
    WHERE Car.Year = {selected_year1}
    ORDER BY City_m.CityID
    ;
    """
    cursor.execute(car_data)
    result = cursor.fetchall()

    df = pd.DataFrame(result)

    # 파이차트 생성
    city_order = df['CityName'].tolist()

    fig = px.pie(df, names="CityName", values="CarCount",
                 hover_data={'CarCount': True}, labels={'CarCount': 'CarCount'},
                 category_orders={'CityName': city_order})
    fig.update_traces(textposition='outside', textinfo='label+value+percent', textfont_color="black",
                      hole=.4, direction='counterclockwise', rotation=-30)
    fig.add_annotation(dict(text=f"{selected_year1}", x=0.5, y=0.5, font_color="black", font_size=25, showarrow=False))
    fig.update_layout(
        height=600
    )
    st.plotly_chart(fig)

with tab2:
    # 지도차트에서 연도 선택
    selected_year2 = st.selectbox("지도차트 연도 선택", year_list, index=year_list.index('2022'))

    st.divider()

    # 데이터 쿼리
    car_data_map = f"""
    SELECT City_m.CityName, City_m.CityName2, City_m.Latitude, City_m.Longitude, Car.CarCount
    FROM Car
    JOIN City_m ON Car.CityID = City_m.CityID
    WHERE Car.Year = {selected_year2}
    ORDER BY City_m.CityID
    ;
    """
    cursor.execute(car_data_map)
    result_map = cursor.fetchall()

    df_map = pd.DataFrame(result_map)

    # 지도 시각화
    fig = px.scatter_mapbox(
        df_map,
        lat="Latitude",  # 위도
        lon="Longitude",  # 경도
        size="CarCount",  # 자동차 등록 대수 크기
        color="CarCount",  # 색상으로 자동차 대수 표시
        hover_name="CityName",  # 도시명 표시
        hover_data={"CarCount": True},
        color_continuous_scale=px.colors.sequential.Aggrnyl,  # 색상 팔레트 변경
        zoom=6,  # 기본 줌 레벨
        mapbox_style="carto-positron"  # 지도 스타일
    )

    # 원의 크기 조정
    fig.update_traces(
        marker=dict(
            sizemin=10,  # 최소 크기
            sizemode="area",  # 크기를 면적으로 계산
            sizeref=2. * max(df_map["CarCount"]) / (100**2)
        )
    )

    fig.update_layout(
        title=f"{selected_year2}년 지역별 자동차 등록 현황",
        title_x=0.5,
        margin={"r": 0, "t": 50, "l": 0, "b": 0}
    )

    st.plotly_chart(fig)