import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# CSV 파일 경로
car_file_path = 'data/Car.csv'
city_file_path = 'data/City_m.csv'

# CSV 파일 읽기
car_df = pd.read_csv(car_file_path)
city_df = pd.read_csv(city_file_path)

# 연도 선택
years = car_df['연도'].unique()
selected_year = st.selectbox('연도를 선택하세요:', years)

# 선택된 연도에 따라 데이터 필터링
filtered_car_df = car_df[car_df['연도'] == selected_year]

# 지도 생성
m = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 각 도시의 좌표에 등록대수를 반영한 원 추가
for _, row in filtered_car_df.iterrows():
    city_id = row['지역ID']
    city_data = city_df[city_df['CityID'] == city_id].iloc[0]
    folium.Circle(
        location=[city_data['Latitude'], city_data['Longitude']],
        radius=row['등록대수'] * 100,  # 등록대수에 비례한 반경
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(m)

# 지도 표시
folium_static(m)