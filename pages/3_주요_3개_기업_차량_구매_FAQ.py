import streamlit as st

st.title("❓ 주요 3개 기업 차량 구매 FAQ")
st.divider()

tab1, tab2, tab3 = st.tabs(['현대', '기아', '제네시스'])

with tab1:
    st.write("현대 차량 구매 FAQ")

with tab2:
    st.write("기아 차량 구매 FAQ")

with tab3:
    st.write("제네시스 차량 구매 FAQ")