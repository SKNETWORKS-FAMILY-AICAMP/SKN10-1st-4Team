import streamlit as st
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo
import pandas as pd
import plotly.express as px


st.title("📊 지역별 자동차 등록 현황")
st.divider()
st.header('시도별 자동차 등록 수 현황')

# 데이터 생성
data = {
    "연도": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Total 등록대수": [1887, 1940, 2012, 2099, 2180, 2253, 2320, 2368, 2437, 2491, 2550]
}

# DataFrame 생성
df = pd.DataFrame(data)
with st.container(height=100, border=1, key=None):
    col1, col2 = st.columns(2)
    with col1:
        start_year = st.selectbox(
            "시작 연도를 선택하세요",
            options=df["연도"].tolist(),
            index=0  # 기본값: 첫 번째 연도
        )

    # 종료 연도 선택
    with col2:
        end_year = st.selectbox(
            "종료 연도를 선택하세요",
            options=df["연도"].tolist(),
            index=len(df["연도"]) - 1  # 기본값: 마지막 연도
        )
with st.container(height=550, border=1, key=None):
    # 선택된 기간에 따라 데이터 필터링
    if start_year > end_year:
        st.error("시작 연도가 종료 연도보다 클 수 없습니다.")
    else:
        filtered_df = df[(df["연도"] >= start_year) & (df["연도"] <= end_year)] 
        st.subheader(f"선택된 기간: {start_year}년 ~ {end_year}년")
        
        # 필터링된 데이터 표시
        # st.write(filtered_df)
    
    df = pd.DataFrame(data)

    # Plotly로 막대 그래프 생성
    fig = px.bar(
        df,
        x="연도",
        y="Total 등록대수",
        title="예쁘게 꾸민 Plotly 막대 그래프",
        color="Total 등록대수",  # 색상을 등록대수 값에 따라 다르게 설정
        color_continuous_scale="Blues",  # 색상 팔레트
        template="simple_white"  # 배경 템플릿
    )

    # 그래프 스타일 추가
    fig.update_layout(
        title_font_size=20,
        xaxis_title="연도",
        yaxis_title="등록대수",
        xaxis=dict(tickangle=-45),  # x축 레이블 기울이기
        yaxis=dict(showgrid=True, gridcolor="lightgrey"),  # y축 그리드 설정
    )

    # Streamlit에 Plotly 그래프 표시
    st.plotly_chart(fig)