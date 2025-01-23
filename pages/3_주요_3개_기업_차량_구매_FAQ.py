import streamlit as st
import json

# 제목 및 탭 구성
st.title("❓ 주요 3개 기업 차량 구매 FAQ")
st.divider()

tab1, tab2, tab3 = st.tabs(['현대', '기아', '제네시스'])

with tab1:
    st.write("현대 차량 구매 FAQ")

with tab2:
    st.write("기아 차량 구매 FAQ")

with tab3:
    st.write("제네시스 차량 구매 FAQ")

    # JSON 파일 로드
    file_path = 'genesis_faq.json'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            faq_data = json.load(file)
    except Exception as e:
        st.error(f"FAQ 데이터를 로드하는 중 오류 발생: {e}")
        faq_data = []

    # 세션 상태 초기화
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    # FAQ 데이터 확인 및 예외 처리
    if len(faq_data) == 0:
        st.write("FAQ 데이터가 없습니다.")
        st.stop()

    # 한 페이지에 표시할 FAQ 수와 페이지 계산
    faq_per_page = 5
    total_pages = (len(faq_data) - 1) // faq_per_page + 1

    # 현재 페이지에 해당하는 FAQ 가져오기
    start_index = st.session_state.current_page * faq_per_page
    end_index = start_index + faq_per_page
    current_faqs = faq_data[start_index:end_index]

    # 현재 페이지의 FAQ 출력
    for item in current_faqs:
        question = item.get("question", "질문 없음")
        answer = item.get("answer", "답변 없음")
        with st.expander(f"❓ {question}"):
            st.write(answer)

    # 페이지 이동 버튼
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ 이전", key="prev"):
            if st.session_state.current_page > 0:
                st.session_state.current_page -= 1

    with col3:
        if st.button("다음 ➡️", key="next"):
            if st.session_state.current_page < total_pages - 1:
                st.session_state.current_page += 1

    # 페이지 정보 표시
    st.write(f"페이지 {st.session_state.current_page + 1} / {total_pages}")
