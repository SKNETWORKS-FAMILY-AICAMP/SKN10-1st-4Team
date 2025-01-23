import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px

st.title("📊 지역별 자동차 등록 현황")
st.divider()

connection = pymysql.connect(
    host = "localhost",
    user = "SKN10_4team",
    password = "skn1234",
    database = "SKN10_4team_1st",
    charset = "utf8"
)

cursor = connection.cursor(pymysql.cursors.DictCursor)

year_data = """
SELECT DISTINCT year
FROM Car
;
"""
cursor.execute(year_data)
years = cursor.fetchall()
year_list = [year['year'] for year in years]

selected_year = st.selectbox("Year", year_list, index=year_list.index('2022'))

st.divider()

car_data = f"""
SELECT City_m.CityName, City_m.CityName2, City_m.Latitude, City_m.Longitude, Car.CarCount
FROM Car
JOIN City_m ON Car.CityID = City_m.CityID
WHERE Car.Year = {selected_year}
ORDER BY City_m.CityID
;
"""
cursor.execute(car_data)
result = cursor.fetchall()

df = pd.DataFrame(result)

city_order = df['CityName'].tolist()

fig = px.pie(df, names = "CityName", values="CarCount",
             hover_data={'CarCount': True}, labels={'CarCount': 'CarCount'},
             category_orders={'CityName': city_order})
fig.update_traces(textposition='outside', textinfo='label+value+percent', textfont_color="black",
                  hole=.4, direction='counterclockwise', rotation=-30)
fig.add_annotation(dict(text=f"{selected_year}", x=0.5, y=0.5, font_color="black", font_size=25, showarrow=False))
fig.update_layout(
    height=600
)
st.plotly_chart(fig)

# 지도 시각화
fig = px.scatter_mapbox(
    df,
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

# 원의 크기 조정 (marker의 최소/최대 크기 설정)
fig.update_traces(
    marker=dict(
        sizemin=10,  # 최소 크기
        sizemode="area",  # 크기를 면적으로 계산
        sizeref=2. * max(df["CarCount"]) / (100**2)  # 크기 조정 (기본 값 대비 키움)
        # line=dict(width=1, color="darkgray")  # 테두리 색상 및 두께 설정
    )
)

fig.update_layout(
    title=f"{selected_year}년 지역별 자동차 등록 현황",
    title_x=0.5,
    margin={"r": 0, "t": 50, "l": 0, "b": 0}
)

st.plotly_chart(fig)