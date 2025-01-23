import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # Windows의 경우
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# CSV 파일 경로
domestic_file_path = 'data/국산차_순위_2021_2024.csv'
foreign_file_path = 'data/해외차_순위_2021_2024.csv'

# CSV 파일 읽기
domestic_df = pd.read_csv(domestic_file_path)
foreign_df = pd.read_csv(foreign_file_path)

# 탭 생성
tab1, tab2 = st.tabs(['국산차', '수입차'])

with tab1:
    # 데이터 시각화
    st.title('국산차 순위')
    st.divider()

    # 연도와 월 선택
    years = domestic_df['연도'].unique()
    months = domestic_df['월'].unique()

    selected_year = st.selectbox('연도를 선택하세요:', years)
    selected_month = st.selectbox('월을 선택하세요:', months)

    # 선택된 연도와 월에 따라 데이터 필터링
    filtered_data = domestic_df[(domestic_df['연도'] == selected_year) & (domestic_df['월'] == selected_month)]

    # 국내산 데이터만 필터링
    domestic_data = filtered_data.iloc[:6]

    # 주요 지표 강조
    total_sales_domestic = domestic_data['판매량'].str.replace(',', '').astype(int).sum()
    st.metric(label="국산차 총 판매량", value=f"{total_sales_domestic:,} 대")

    # 도넛 모양의 파이 차트 생성
    st.subheader('국산차 브랜드별 판매 비율')
    fig, ax = plt.subplots()
    top_3 = domestic_data.iloc[:3]
    others = domestic_data.iloc[3:]
    labels = top_3['브랜드'].tolist() + ['기타 브랜드']
    sizes = top_3['판매량'].str.replace(',', '').astype(int).tolist() + [others['판매량'].str.replace(',', '').astype(int).sum()]
    colors = plt.get_cmap('tab20').colors  # 다양한 색상 사용
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # 도넛 차트의 가운데에 총 판매량 표시
    ax.text(0, 0, f"{total_sales_domestic:,} 대", ha='center', va='center', fontsize=12, fontweight='bold')

    # 파이 차트 표시
    st.pyplot(fig)

    # 데이터 카드 형식으로 표시
    st.subheader('국산차 순위 데이터')
    def create_cards(data):
        for index, row in data.iterrows():
            st.markdown(f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; margin: 10px 0;">
                <h3 style="margin: 0;">{row['순위']}위 - {row['브랜드']}</h3>
                <img src="{row['로고 이미지 링크']}" width="50" style="float: right; margin-left: 10px;">
                <p>판매량: {row['판매량']}</p>
                <p>비율: {row['비율']}</p>
            </div>
            """, unsafe_allow_html=True)

    # 국산차 카드 생성
    create_cards(domestic_data)

with tab2:
    # 데이터 시각화
    st.title('수입차 순위')
    st.divider()

    # 연도와 월 선택
    years = foreign_df['연도'].unique()
    months = foreign_df['월'].unique()

    selected_year = st.selectbox('연도를 선택하세요:', years, key='foreign_year')
    selected_month = st.selectbox('월을 선택하세요:', months, key='foreign_month')

    # 선택된 연도와 월에 따라 데이터 필터링
    filtered_data = foreign_df[(foreign_df['연도'] == selected_year) & (foreign_df['월'] == selected_month)]

    # 주요 지표 강조
    total_sales_foreign = filtered_data['판매량'].str.replace(',', '').astype(int).sum()
    st.metric(label="수입차 총 판매량", value=f"{total_sales_foreign:,} 대")

    # 도넛 모양의 파이 차트 생성
    st.subheader('수입차 브랜드별 판매 비율')
    fig, ax = plt.subplots()
    top_5 = filtered_data.iloc[:5]
    others = filtered_data.iloc[5:]
    labels = top_5['브랜드'].tolist() + ['기타 브랜드']
    sizes = top_5['판매량'].str.replace(',', '').astype(int).tolist() + [others['판매량'].str.replace(',', '').astype(int).sum()]
    colors = plt.get_cmap('tab20').colors  # 다양한 색상 사용
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # 도넛 차트의 가운데에 총 판매량 표시
    ax.text(0, 0, f"{total_sales_foreign:,} 대", ha='center', va='center', fontsize=12, fontweight='bold')

    # 파이 차트 표시
    st.pyplot(fig)

    # 데이터 카드 형식으로 표시
    st.subheader('수입차 순위 데이터')
    create_cards(filtered_data)