
# 제네시스 크롤링
from selenium import webdriver
from bs4 import BeautifulSoup
import json

# 웹 드라이버 설정 (Chrome 드라이버 사용)
driver = webdriver.Chrome()

# 웹 페이지 열기
url = "https://www.genesis.com/kr/ko/support/faq/vehicle-purchase.html?anchorID=faq_tab"
driver.get(url)

# 페이지 소스 가져오기
html_source = driver.page_source

# HTML 파일로 저장
with open("genesis_faq.html", "w", encoding="utf-8") as file:
    file.write(html_source)

# 드라이버 종료
driver.quit()

# BeautifulSoup을 사용하여 페이지 소스 파싱
soup = BeautifulSoup(html_source, 'html.parser')

# FAQ 질문과 답변 추출
faqs = []
faq_items = soup.select('.cp-faq__accordion-item')  # FAQ 항목을 감싸는 클래스 이름을 사용하여 선택

for item in faq_items:
    question = item.select_one('.accordion-title').get_text(strip=True)
    answer = item.select_one('.accordion-panel-inner').get_text(strip=True)
    faqs.append({'question': question, 'answer': answer})

# 추출한 FAQ를 파일로 저장
with open("genesis_faq.json", "w", encoding="utf-8") as file:
    json.dump(faqs, file, ensure_ascii=False, indent=4)