import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("📊 지역별 자동차 등록 현황")
st.divider()
st.header('시도별 자동차 등록 수 현황')

file_path = 'data/Car.csv'
df = pd.read_csv(file_path)

# 데이터 구조 확인
st.write(df.head())

# 데이터 형식 변환 및 결측값 채우기
st.write("등록대수 열의 데이터 유형: ", df['등록대수'].dtype)

df['등록대수'] = pd.to_numeric(df['등록대수'], errors='coerce').fillna(0)
st.write("등록대수 열 변환 후: ", df['등록대수'].dtype)

# 연도별 차량 증가 수 계산
df['증가수'] = df['등록대수'].diff().fillna(0).astype(int)

col1, col2 = st.columns(2)
with col1:
    start_year = st.selectbox(
        "시작 연도를 선택하세요",
        options=df["연도"].unique(),
        index=0
    )

with col2:
    end_year = st.selectbox(
        "종료 연도를 선택하세요",
        options=df["연도"].unique(),
        index=len(df["연도"].unique())-1
    )

if start_year > end_year:
    st.error("시작 연도가 종료 연도보다 클 수 없습니다.")
else:
    filtered_df = df[(df["연도"] >= start_year) & (df["연도"] <= end_year)]
    st.subheader(f"선택된 기간: {start_year}년 ~ {end_year}년")

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=filtered_df["연도"],
            y=filtered_df["등록대수"],
            name="등록대수",
            marker_color="#FCC6FF"
        )
    )

    # 꺾은선 그래프에서 문제를 찾기 위한 확인
    st.write("증가수 열의 값들: ", filtered_df['증가수'].tolist())

    fig.add_trace(
        go.Scatter(
            x=filtered_df["연도"],
            y=filtered_df["증가수"],
            name="증가수",
            yaxis="y2",
            mode='lines+markers',
            line=dict(color='#FF8383', width=3),
            marker=dict(size=8)
        )
    )

    fig.update_layout(
        xaxis=dict(title="연도"),
        yaxis=dict(title="등록대수"),
        yaxis2=dict(
            title="증가수 (천 단위)",
            overlaying="y",
            side="right",
            tickformat=",d"
        ),
        xaxis_tickangle=-45,
        template="simple_white"
    )

    st.plotly_chart(fig)
