import streamlit as st
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

st.set_page_config(layout="wide")

st.title('##별 차량수수')
st.header('시도별 자동차 등록 수 현황')

with st.form("my_form"):
    st.subheader('검색결과')
    with st.container(height=800, border=2, key=None):
        st.text("**통계표")
        st.selectbox("년도 선택1", ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])
        st.selectbox("년도 선택2", ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])
    submitted = st.form_submit_button('제출')

    