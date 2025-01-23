import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc, patches

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # Windows의 경우
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# CSV 파일 경로
file_path = 'data/Car.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 연도 선택 드롭다운 메뉴
years = df['연도'].unique()
selected_year = st.selectbox('연도를 선택하세요:', years)

# 선택된 연도에 따라 데이터 필터링
filtered_data = df[df['연도'] == selected_year]

# 총 등록대수 계산
total_count = filtered_data['등록대수'].sum()

# 파이 차트 그리기
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    filtered_data['등록대수'], 
    labels=filtered_data['지역'], 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=plt.cm.tab20.colors  # 다양한 색상 사용
)

# 범례 추가
legend_elements = [patches.Patch(facecolor=wedges[i].get_facecolor(), label=f'{region}: {count}')
                   for i, (region, count) in enumerate(zip(filtered_data['지역'], filtered_data['등록대수']))]
ax.legend(handles=legend_elements, title='지역별 등록대수', loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
st.pyplot(fig)