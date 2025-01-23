import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("📊 지역별 자동차 등록 현황")
st.divider()

# 데이터 생성
data = {
    "연도": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Total 등록대수": [1887, 1940, 2012, 2099, 2180, 2253, 2320, 2368, 2437, 2491, 2550]
}

# DataFrame 생성
df = pd.DataFrame(data)

# 연도별 차량 증가 수 계산
df['증가수'] = df['Total 등록대수'].diff().fillna(0).astype(int)

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

        # 이중 y축을 갖는 복합 그래프 생성
        fig = go.Figure()

        # 막대 그래프 추가 (등록대수)
        fig.add_trace(
            go.Bar(
                x=filtered_df["연도"],
                y=filtered_df["Total 등록대수"],
                name="Total 등록대수",
                marker_color="#FCC6FF"
            )
        )

        # 선 그래프 추가 (증가수)
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

        # 레이아웃 업데이트: 이중 y축 설정
        fig.update_layout(
            xaxis=dict(title="연도"),
            yaxis=dict(title="Total 등록대수"),
            yaxis2=dict(
                title="증가수 (천 단위)",
                overlaying="y",
                side="right",
                tickformat=",d"
            ),
            xaxis_tickangle=-45,
            template="simple_white"
        )


        # Streamlit에 Plotly 그래프 표시
        st.plotly_chart(fig)
    
    
