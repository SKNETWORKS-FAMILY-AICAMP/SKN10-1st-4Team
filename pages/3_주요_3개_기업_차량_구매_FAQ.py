import streamlit as st
import json

st.title("❓ 주요 3개 기업 차량 구매 FAQ")
st.divider()

tab1, tab2, tab3 = st.tabs(['현대', '기아', '제네시스'])

with tab1:
    st.write("현대 차량 구매 FAQ")

with tab2:
    st.write("기아 차량 구매 FAQ")

with tab3:
    st.write("제네시스 차량 구매 FAQ")
    
    file_path = 'genesis_faq.json' # 경로설정
    with open(file_path, 'r', encoding='utf-8') as file:
        faq_data = json.load(file)

    for item in faq_data:
        question = item.get("question", "질문 없음")
        answer = item.get("answer", "답변 없음")
        with st.expander(f"❓ {question}"):
            st.write(answer)