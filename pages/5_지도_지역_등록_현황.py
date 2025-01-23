import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import random

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

# 색상 팔레트 생성
colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(len(city_df))]

# 각 도시의 좌표에 등록대수를 반영한 원 추가
for i, (_, row) in enumerate(filtered_car_df.iterrows()):
    city_id = row['지역ID']
    city_data = city_df[city_df['CityID'] == city_id].iloc[0]
    folium.Circle(
        location=[city_data['Latitude'], city_data['Longitude']],
        radius=row['등록대수'] * 100,  # 등록대수에 비례한 반경
        color=colors[i],
        fill=True,
        fill_color=colors[i],
        fill_opacity=0.6,
        popup=f"{city_data['CityName']} ({row['등록대수']} 만만대)"
    ).add_to(m)

# 지도 표시
folium_static(m)

# 색상 레이블 표시

legend_html = """
<div style="border:1px solid black; padding:5px; width: 200px;">
    <b>지역별 색상 레이블</b><br>
"""
for i, city in city_df.iterrows():
    legend_html += f"<div style='display: flex; align-items: center; margin-bottom: 5px;'><div style='width: 15px; height: 15px; background-color: {colors[i]}; margin-right: 5px;'></div>{city['CityName']}</div>"
legend_html += "</div>"
st.markdown(legend_html, unsafe_allow_html=True)