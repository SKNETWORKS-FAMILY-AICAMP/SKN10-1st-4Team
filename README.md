# SKN10-1st-4Team
<br/>

![](https://cdn.imweb.me/upload/S20240314bd10436a7991a/41a9769cc44e6.png)
<br/>
<br/>

## ⭐ 프로젝트 팀
<br/>

| 좌민서 | 김민혜 | 박예슬 | 신민주 | 홍승표 | 황인호 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 팀장 / 지역별 자동차 등록 현황 (그래프) | ERD 설계 / DB 구현 | ERD 설계 / 현대자동차 FAQ | 화면 설계 / 제네시스 FAQ | 라이브러리 조사 / 연도별 자동차 등록 현황 | 화면 설계 / 기아자동차 FAQ / 지역별 자동차 등록 현황 (지도) / 브랜드별 자동차 판매 현황
| [@INe](https://github.com/INe904) | [@kkminhye](https://github.com/kkminhye) | [@yeseulnim](https://github.com/yeseulnim) | [@sinminju](https://github.com/sinminju) | [@redwin02](https://github.com/redwin-02) | [@HIHO9999](https://github.com/HIHO999) |
<br/>

## 📌 프로젝트 개요
<br/>

### 프로젝트 주제
<br/>

**전국 자동차 등록 현황 및 기업 FAQ 조회 시스템**
<br/>
<br/>

### 프로젝트 목적
<br/>

전국 자동차 등록 현황을 연도별 및 지역별로 분석하여, **자동차 증가 추세와 지역별 특성을 파악**한다.<br/>
이를 통해 **교통 정책 수립 및 지역 발전 전략**에 기여할 수 있는 정보를 제공한다.
<br/>
<br/>

### 프로젝트 필요성
<br/>

1. 자동차 등록 현황은 도시 교통 문제, 환경 정책, 도로 인프라 계획 등과 밀접하게 연관되어 있다.
<br/>

2. 연도별 및 지역별 자동차 등록 현황 데이터를 시각화하여, 공공 및 민간 부분에서 데이터를 기반 정책 결정을 지원한다.
<br/>
<br/>

### 프로젝트 내용
<br/>

 1. **데이터 수집 및 가공**<br/>
- <b>[지표누리](https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1257)</b>에서 제공하는 연도별 및 지역별 자동차 등록 현황 데이터를 수집하여 목적에 맞게 가공한 후, 데이터베이스에 저장한다.
- 다나와의 <b>[자동차 판매 실적](https://auto.danawa.com/auto/?Work=record&pcUse=y)</b> 페이지에서 제공하는 브랜드별 자동차 판매 실적을 수집하여 목적에 맞게 가공한 후 CSV 파일로 저장한다다
<br/>

2. **데이터 시각화**<br/>
- 수집한 데이터를 Python의 **Plotly** 및 **MatPlotLib** 라이브러리를 통해 시각화한다.
<br/>

3. **국내 주요 3개 자동차 회사 FAQ**<br/>
- 국내 판매율이 가장 높은 주요 3개 자동차 회사(현대, 기아, 제네시스)의 차량 구매 FAQ를 수집 및 정리하고, 이를 조회할 수 있게 한다.
<br/>
<br/>

### 프로젝트 기대 효과
<br/>

1. **연도별 및 지역별 자동차 등록 현황의 시각적 자료**를 제공하여 데이터 직관적으로 파악할 수 있다.
<br/>

2. **교통 및 환경 정책 수립**을 위한 기초 데이터를 제공한다.
<br/>

3. **기업 FAQ 조회 시스템**을 통해 소비자의 정보 접근성을 높인다.
<br/>
<br/>

## 📌 설치/사용 방법
<br/>

### 1. GitHub에서 Repository 클론

```python
    git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN10-1st-4Team.git
```
### 2. 라이브러리 설치
```python
    pip install -r requirements.txt
```

### 3. (생략 가능) FAQ 정보 수집 - 웹 크롤링 코드 실행
※ 웹 크롤링 결과물은 data 폴더에 json으로 저장되어 있으므로, 별도 크롤링 없이 바로 실행이 가능함. 다만 신규 데이터 확인을 위해 웹크롤링이 필요한 경우 아래 코드를 사용할 수 있음.
```python
    python kia_faq.py
```
```python
    python hyundai_faq.py
```
### 4. 서비스 실행
```python
    streamlit run 1_연도별_자동차_등록_현황.py
```


## 📌 기술 스택
<br/>

### 화면 설계

![](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
<br/>

### 데이터 가공 및 처리

![](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) &nbsp; ![](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
<br/>

### 화면 구현

![](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white) &nbsp; ![](https://img.shields.io/badge/streamlit-FF0000?style=for-the-badge&logo=streamlit&logoColor=white)
<br/>

### 버전 관리 및 협업

![](https://img.shields.io/badge/github-000000?style=for-the-badge&logo=github&logoColor=white)
<br/>
<br/>

## 💻 화면 설계
<br/>

1. 연도별 자동차 등록 현황
![](/images/figma1.png)

2. 지역별 자동차 등록 현황
![](/images/figma2.png)

3. 주요 3개 기업 차량 구매 FAQ
![](/images/figma3.png)

## 💻 데이터 가공 및 처리
<br/>

### ERD 

![](/images/erd.png)


### 실제 데이터 가공 및 처리

**1. 자동차 등록 현황**
- 자료 출처 : [지표누리 자동차 등록 현황](https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1257)
- 자료 가공 : 개별 Excel 파일 다운로드 -> CSV로 변경 -> MySQL 데이터베이스 테이블로 저장

**2. 주요 3개 기업 차량 구매 FAQ**
- 자료 출처 : 국내 3대 자동차 기업 (<b>[현대](https://www.hyundai.com/kr/ko/e/customer/center/faq)</b>, <b>[기아](https://www.kia.com/kr/customer-service/center/faq)</b>, <b>[제네시스](https://www.genesis.com/kr/ko/support/faq.html)</b>) 홈페이지의 'FAQ' 중 '차량 구매' 항목
- 자료 가공 : Selenium으로 웹크롤링 -> JSON으로 저장 

**3. 브랜드별 자동차 판매 실적**
- 자료 출처 : 다나와의 <b>[자동차 판매 실적](https://auto.danawa.com/auto/?Work=record&pcUse=y)</b> 페이지
- 자료 가공 : Selenium으로 웹크롤링 -> CSV로 저장



## 📌 프로젝트 최종 결과
<br/>

1. 연도별 자동차 등록 현황
![]()

2. 지역별 자동차 등록 현황
![](/images/final_screen2.png)
![](/images/final_screen3.png)

3. 주요 3개 기업 차량 구매 FAQ
![](/images/final_screen4.png)

4. 브랜드별 자동차 판매 순위
![]()
