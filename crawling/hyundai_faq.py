from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from time import sleep

#import pandas as pd
import json


URL = "https://www.hyundai.com/kr/ko/e/customer/center/faq"

driver = webdriver.Chrome()
driver.get(URL)
# 리스트에 딕셔너리로 내용 저장
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
            sleep(0.5)

            #질문타이틀 클릭하기
            faq_title[0].click()
            sleep(0.5)

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
                link_whole = faq_answer.find_elements(By.TAG_NAME, "a")
                link = {
                    "url" : link_whole[0].get_attribute("href"),
                    "text" : link_whole[0].text
                    }
            except:
                link = ""
            #print("링크 URL:", url)
            
            qna_list.append({"question": faq_question_text, "answer": faq_answer_text, "link": link})

        except TimeoutException:
            print("Timed out waiting for page to load")
        except NoSuchElementException:
            print("Could not find the element")
        except IndexError:
            pass

    next_button = driver.find_element(By.CSS_SELECTOR, "button.btn-next")
    next_button.click()
    sleep(1)
 
#qna_df = pd.DataFrame(qna_list, columns = ["page_num","question_num","question","answer","link"])
#qna_df.to_csv(path_or_buf="data/hyundai_qna.csv")

# 결과를 JSON 파일로 저장
with open("data\hyundai_faq.json", "w", encoding="utf-8") as json_file:
    json.dump(qna_list, json_file, ensure_ascii=False, indent=4)