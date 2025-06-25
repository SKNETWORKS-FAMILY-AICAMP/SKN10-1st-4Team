#test
import streamlit as st
import pandas as pd
import plotly.express as px
import pymysql
from common.insert_data import insert_data
from common.insert_data_city import insert_data_city

insert_data()
insert_data_city()

st.set_page_config(layout="centered")

st.title("📊 연도별 자동차 등록 현황")
st.divider()

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

# Streamlit 컨테이너
with st.container():
    # 컬럼 레이아웃 사용
    col1, col2 = st.columns(2)
    # 년도 리스트 생성 및 선택
    years = ef['Year'].unique().tolist()

    # 디폴트 값 설정
    default_start_year_index = 0  # 첫 번째 연도를 디폴트로 설정
    default_end_year_index = len(years) - 1  # 마지막 연도를 디폴트로 설정

    with col1:
        start_year = st.selectbox(
            '첫번째 년도를 선택해주세요.', 
            years, 
            index=default_start_year_index
        )

    with col2:
        end_year = st.selectbox(
            '마지막 년도를 선택해주세요.', 
            years, 
            index=default_end_year_index
        )

# 연도 범위 확인 및 데이터 필터링
if start_year > end_year:
    st.error("Error: The start year cannot be greater than the end year.")
else:
    with st.container():
        # 사용자 입력 값으로 데이터 필터링
        filtered_data = cf[(cf["Year"] >= start_year) & (cf["Year"] <= end_year)]

        # Plotly로 그래프 생성
        fig = px.bar(
            filtered_data, 
            x="Year", 
            y="YearofCar", 
            title="조회결과"
        )

        # axis title 업데이트
        fig.update_xaxes(title_text="연도")
        fig.update_yaxes(title_text="차량 수 (만대)")

        # 그래프 출력
        st.plotly_chart(fig)

}]}