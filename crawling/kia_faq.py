import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 웹 드라이버 설정 (Chrome 드라이버 사용)
driver = webdriver.Chrome()

# 웹 페이지 열기
url = "https://www.kia.com/kr/customer-service/center/faq"
driver.get(url)

# 페이지가 완전히 로드될 때까지 대기
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

# "TOP 10" 버튼 클릭
top_10_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'TOP 10')]"))
)
top_10_button.click()

# "차량 구매" 버튼 클릭
car_purchase_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//li[button/span[text()='차량 구매']]"))
)
car_purchase_button.click()

# 3초 텀을 둠
time.sleep(3)

# 각 질문 클릭하여 답변 가져오기
faq_data = []

def get_faq_data():
    # FAQ 항목이 로드될 때까지 대기
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cmp-accordion__button")))

    # FAQ 항목들 찾기
    faq_items = driver.find_elements(By.CSS_SELECTOR, ".cmp-accordion__button")

    for i in range(len(faq_items)):
        # 각 질문을 클릭하기 전에 요소를 다시 찾음
        faq_items = driver.find_elements(By.CSS_SELECTOR, ".cmp-accordion__button")
        item = faq_items[i]
        question = item.find_element(By.CSS_SELECTOR, ".cmp-accordion__title").text
        item.click()  # 질문 클릭하여 답변 표시

        # 답변이 로드될 때까지 대기
        panel_id = item.get_attribute("aria-controls")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, panel_id)))
        answer_element = driver.find_element(By.ID, panel_id)
        answer = answer_element.text

        # 하이퍼링크 정보 가져오기
        links = []
        link_elements = answer_element.find_elements(By.TAG_NAME, "a")
        for link in link_elements:
            links.append({
                "href": link.get_attribute("href"),
                "text": link.text
            })

        # 이미지 링크 정보 가져오기
        images = []
        image_elements = answer_element.find_elements(By.TAG_NAME, "img")
        for img in image_elements:
            images.append({
                "src": img.get_attribute("src"),
                "alt": img.get_attribute("alt")
            })

        faq_data.append({
            "question": question,
            "answer": answer,
            "links": links,
            "images": images
        })

    # 스크롤을 맨 위로 올리기
    driver.execute_script("window.scrollTo(0, 0);")

# 첫 페이지의 FAQ 데이터 가져오기
get_faq_data()

# 페이지 넘기기
current_page = 1
while current_page < 4:
    try:
        next_page = str(current_page + 1)

        # 다음 페이지 번호 클릭
        next_page_element = driver.find_element(By.XPATH, f"//ul[@class='paging-list']//a[text()='{next_page}']")
        next_page_element.click()

        # 3초 텀을 둠
        time.sleep(3)

        # 다음 페이지가 로드될 때까지 대기
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cmp-accordion__button")))

        # 각 페이지의 FAQ 데이터를 가져오기 전에 요소를 다시 찾음
        get_faq_data()

        current_page += 1
    except Exception as e:
        print(f"Error: {e}")
        break

# 드라이버 종료
driver.quit()

# 결과를 JSON 파일로 저장
<<<<<<< HEAD
with open("/data/kia_faq.json", "w", encoding="utf-8") as json_file:
=======
with open("data\kia_faq.json", "w", encoding="utf-8") as json_file:
>>>>>>> 09ae3553d1dc6404737e4f1ea5ccdff5d1ecabfb
    json.dump(faq_data, json_file, ensure_ascii=False, indent=4)

# 결과 출력
for faq in faq_data:
    print(f"Question: {faq['question']}")
    print(f"Answer: {faq['answer']}")
    print(f"Links: {faq['links']}")
    print(f"Images: {faq['images']}\n")