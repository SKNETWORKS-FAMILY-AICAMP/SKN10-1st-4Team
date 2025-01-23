from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from time import sleep

import pandas as pd


URL = "https://www.hyundai.com/kr/ko/e/customer/center/faq"

driver = webdriver.Chrome()
driver.get(URL)
# 딕셔너리에 페이지넘버, 질문넘버 저장
qna_list = []

for page_id in range(4):
    for question_id in range(1,11):
        try:
            print(question_id)
            #엘리먼트 찾기
            faq_list = driver.find_element(By.CSS_SELECTOR, "div[data-v-28d34f54].list-wrap")

            try:
                # 플로팅 메뉴 제거
                floating_menu = driver.find_element(By.CSS_SELECTOR, "div[data-v-1ea4ba2d].inner_wrap")
                driver.execute_script("arguments[0].remove();", floating_menu)
            except:
                pass
            faq_title = faq_list.find_elements(By.CSS_SELECTOR,f"div[data-id='{question_id}'] button.list-title")
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});",faq_title[0])
            sleep(1)

            #질문타이틀 클릭하기
            faq_title[0].click()
            sleep(1)

            #질문타이틀 텍스트 받아오기
            faq_question = faq_title[0].find_element(By.CSS_SELECTOR, "span.list-content[data-v-28d34f54]")
            faq_question_text = faq_question.text
            #print(faq_question_text)

            #질문답변 텍스트 받아오기
            faq_answer = driver.find_element(By.CLASS_NAME, "conts")
            faq_answer_text = faq_answer.text
            #print("전체 답변:", faq_answer_text)

            # 링크 URL 가져오기
            try:
                link = faq_answer.find_element(By.CSS_SELECTOR, "a")
                url = link.get_attribute("href")
            except:
                url = None
            #print("링크 URL:", url)
            
            # 질문 다시 클릭 (아래질문 보이도록록)
            faq_title[0].click()
            sleep(1)
            qna_list.append([page_id,question_id,faq_question_text,faq_answer_text,url])

        except TimeoutException:
            print("Timed out waiting for page to load")
        except NoSuchElementException:
            print("Could not find the element")
        except IndexError:
            pass

    next_button = driver.find_element(By.CSS_SELECTOR, "button.btn-next")
    next_button.click()
    sleep(1)
 
qna_df = pd.DataFrame(qna_list, columns = ["page_num","question_num","question","answer","link"])
qna_df.to_csv(path_or_buf="../data/hyundai_qna.csv")