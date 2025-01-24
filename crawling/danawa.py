from selenium import webdriver
from selenium.webdriver.common.by import By


import pandas as pd
import time

# 크롬 드라이버 설정

driver = webdriver.Chrome()

# 데이터 저장 리스트
domestic_data = []
foreign_data = []

# 2021년 1월부터 2024년 12월까지의 URL 생성 및 데이터 크롤링
for year in range(2021, 2025):
    for month in range(1, 13):
        if year == 2024 and month > 12:
            break
        month_str = f"{year}-{month:02d}-00"
        url = f"https://mauto.danawa.com/auto/?Work=record&Tab=Grand&Month={month_str}&MonthTo="
        driver.get(url)
        time.sleep(0.5)  # 페이지 로딩 대기

        # 국산차 순위 데이터 크롤링
        rank_elements = driver.find_elements(By.CSS_SELECTOR, "ul.sideRankR li")

        for index, rank_element in enumerate(rank_elements):
            rank = rank_element.find_element(By.CSS_SELECTOR, "span.rank").text
            brand = rank_element.find_element(By.CSS_SELECTOR, "span.title").text.strip()
            sales = rank_element.find_element(By.CSS_SELECTOR, "span.sales").text
            rate = rank_element.find_element(By.CSS_SELECTOR, "span.rate").text
            logo_img = rank_element.find_element(By.CSS_SELECTOR, "span.title img").get_attribute("src")
            data = [year, month, rank, brand, sales, rate, logo_img]
            if index < 6:
                domestic_data.append(data)
            else:
                foreign_data.append(data)

# 데이터프레임으로 변환
domestic_df = pd.DataFrame(domestic_data, columns=["연도", "월", "순위", "브랜드", "판매량", "비율", "로고 이미지 링크"])
foreign_df = pd.DataFrame(foreign_data, columns=["연도", "월", "순위", "브랜드", "판매량", "비율", "로고 이미지 링크"])

# 데이터프레임 저장
domestic_df.to_csv("국산차_순위_2021_2024.csv", index=False, encoding='utf-8-sig')
foreign_df.to_csv("해외차_순위_2021_2024.csv", index=False, encoding='utf-8-sig')

# 드라이버 종료
driver.quit()

print("크롤링 완료 및 데이터 저장 완료")
#https://mauto.danawa.com/auto/?Work=record&Tab=Grand&Month=2021-01-00&MonthTo=
#https://mauto.danawa.com/auto/?Work=record&Tab=Grand&Month=2021-01-00&MonthTo= 에서 2021-01은 21년 1월 데이터를 받아온다는 의미
