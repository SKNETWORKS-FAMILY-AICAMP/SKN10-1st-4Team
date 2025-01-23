import streamlit as st
import json

st.title("❓ 주요 3개 기업 차량 구매 FAQ")
st.divider()

tab1, tab2, tab3 = st.tabs(['현대', '기아', '제네시스'])

with tab1:
    st.write("현대 차량 구매 FAQ")

with tab2:
    st.write("기아 차량 구매 FAQ")

    file_path = 'kia_faq.json'  # 경로설정
    with open(file_path, 'r', encoding='utf-8') as file:
        faq_data = json.load(file)

    # 검색 기능
    search_query = st.text_input("검색어를 입력하세요:")
    if search_query:
        faq_data = [item for item in faq_data if search_query.lower() in item['question'].lower() or search_query.lower() in item['answer'].lower()]

    # 페이지네이션 설정
    items_per_page = 10
    total_pages = (len(faq_data) + items_per_page - 1) // items_per_page

    # 페이지 번호 선택
    if 'page' not in st.session_state or st.session_state.page > total_pages:
        st.session_state.page = 1

    def change_page(page):
        st.session_state.page = page

    page = st.session_state.page
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_page_data = faq_data[start_idx:end_idx]

    for item in current_page_data:
        question = item.get("question", "질문 없음")
        answer = item.get("answer", "답변 없음")

        # 하이퍼링크 처리
        for link in item.get("links", []):
            answer = answer.replace(link["text"], f"[{link['text']}]({link['href']})")

        with st.expander(f"❓ {question}"):
            st.write(answer)

            # 이미지 처리
            for image in item.get("images", []):
                st.image(image["src"], caption=image.get("alt", ""))

    page_numbers = [i for i in range(1, total_pages + 1)]
    
    # 이전, 다음 버튼을 양쪽 끝에 배치하고 가운데에 현재 페이지 표시
    button_container = st.container()
    with button_container:
        col1, col2, col3 = st.columns([1, 6, 1])
        with col1:
            if page > 1 and st.button("이전", key="prev_page"):
                change_page(page - 1)
        with col2:
            st.markdown(f"<div style='text-align: center;'>페이지 {page} / {total_pages}</div>", unsafe_allow_html=True)
        with col3:
            if page < total_pages and st.button("다음", key="next_page"):
                change_page(page + 1)

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