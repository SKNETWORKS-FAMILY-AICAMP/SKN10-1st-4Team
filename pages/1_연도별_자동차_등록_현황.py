import streamlit as st
import pandas as pd
import plotly.express as px
import pymysql

st.title("📊 지역별 자동차 등록 현황")
st.divider()
st.header('시도별 자동차 등록 수 현황')

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host="localhost",
    user="SKN10_4team",
    password="skn1234",
    database="SKN10_4team_1st",
    charset="utf8"
)

# SQL 데이터 가져오기
year_data = "select Year FROM Car"
ef = pd.read_sql(year_data, connection)

car_data = """
SELECT Year, SUM(CarCount) YearofCar
FROM SKN10_4team_1st.Car
GROUP BY Year
ORDER BY Year;
"""
cf = pd.read_sql(car_data, connection)
#st.write(ef)
#st.write(cf)
# df.columns = ['Year','CarCount']
with st.container(height=100, border=1, key=None):
    # 컬럼 레이아웃 사용
    col1, col2 = st.columns(2)
    # 년도 리스트 생성 및 선택
    years = ef['Year'].unique().tolist()

    with col1:
        start_year = st.selectbox('Select a start year:', years)

    with col2:
        end_year = st.selectbox('Select an end year:', years)

with st.container(height=484, border=1, key=None):
    # 사용자 입력 값으로 필터링
    filtered_data = cf[(cf["Year"] >= start_year) & (cf["Year"] <= end_year)]

    #st.write(filtered_data)
    # 선택된 기간과 필터링된 데이터 출력
    #st.write(f'Selected year range: {start_year} - {end_year}')
    #st.write("Filtered data:")
    #st.write(filtered_data)

    # Plotly를 사용하여 막대 그래프 그리기
    fig = px.bar(filtered_data, x="Year", y="YearofCar", title="")

    # 그래프 출력
    st.plotly_chart(fig)
