# SKN10-1st-4Team
<br/>

![](https://cdn.imweb.me/upload/S20240314bd10436a7991a/41a9769cc44e6.png)
<br/>
<br/>

## ⭐ 프로젝트 팀
<br/>

| 좌민서 | 김민혜 | 박예슬 | 신민주 | 홍승표 | 황인호 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 팀장<br/>지역별 자동차 등록 현황<br/>(그래프) | ERD 설계<br/>DB 구현 | ERD 설계<br/>현대자동차 FAQ | 화면 설계<br/>제네시스 FAQ | 라이브러리 조사br/>연도별 자동차 등록 현황 | 화면 설계<br/>기아자동차 FAQ<br/>지역별 자동차 등록 현황<br/>(지도)<br/>브랜드별 자동차 판매 현황
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

2. 연도별 및 지역별 자동차 등록 현황 데이터를 시각화하여, 공공 및 민간 부분에서 데이터 기반 정책 결정을 지원한다.
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

### 1. GitHub에서 Repository Clone
<br/>

```python
    git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN10-1st-4Team.git
```
### 2. 라이브러리 설치
<br/>

```python
    pip install -r requirements.txt
```

### 3. (생략 가능) FAQ 정보 수집 - 웹 크롤링 코드 실행
<br/>

※ 웹 크롤링 결과물은 data 폴더에 json 파일로 저장되어 있으므로, 별도의 크롤링 없이 바로 실행이 가능하다. 다만, 신규 데이터 확인을 위해 웹 크롤링이 필요한 경우 아래 코드를 사용할 수 있다.
<br/>

```python
    python kia_faq.py
```
```python
    python hyundai_faq.py
```
```python
    python genesis_faq.py
```
```python
    python danawa.py
```
<br/>

### 4. 서비스 실행
<br/>

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

### 0. 메뉴
<br/>

![](images\menu_design.png)
<br/>

### 1. 연도별 자동차 등록 현황
<br/>

![](images\year_design.png)
<br/>

### 2. 지역별 자동차 등록 현황
<br/>

![](images\region_design.png)
<br/>

3. 주요 3개 기업 차량 구매 FAQ
<br/>

![](images\faq_design.png)
<br/>
<br/>

## 💻 데이터 가공 및 처리
<br/>

### ERD 

![](/images/erd.png)


### 실제 데이터 가공 및 처리

**1. 자동차 등록 현황**
- 자료 출처 : <b>[지표누리 자동차 등록 현황](https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1257)</b>
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
![](/images/final_screen1.png)

2. 지역별 자동차 등록 현황
![](/images/final_screen2.png)
![](/images/final_screen3.png)

3. 주요 3개 기업 차량 구매 FAQ
![](/images/final_screen4.png)

4. 브랜드별 자동차 판매 순위
![](/images/final_screen5.png)


## 개발과정에서 발생한 이슈 및 해결방법
- SQL DB 구축
    - MySQL DB는 깃헙으로 동기화되지 않고 각 인원이 각자 구축해야 했기에 그 과정에서 시행착오가 있었음. 이러한 상황 방지를 위해 최종 코드에서는 DB 구축 코드를 함수로 만들어 자동 실행되도록 함.
- 어떤 데이터를 SQL에 저장할것인지
    - 최초 기획한 ERD 구조에는 FAQ가 포함되어 있었으나, 실제 구현시 FAQ를 JSON에 담는 방식이 더 효율적이라 판단되었음. 이에 기획을 수정함.
    - 최초 기획한 ERD 구조에는 (전체자동차통계가 불포함이었으나 최종적으로는 포함함 -> 이거맞나?확인)
- 기능구현 완료후 오류 발생
    - AI의 디버깅 보조로 해결함

****ERD 수정 필요****


## 팀원별 느낀점
- 좌민서 : 지금까지 배운 내용을 바탕으로 응용된 내용을 활용할 수 있었던 좋은 기회가 되었습니다. 그리고 어쩌다 보니까 팀장을 맡게 되었는데 팀원분들이 잘 따라와 주시고 도와주셔서 이번 프로젝트를 무사히 마칠 수 있었던 것 같습니다.
- 신민주 : 체계적인 프로젝트를 처음 진행해봤는데 팀워크의 중요성을 느꼈습니다. 제가 부족한 부분이 많았지만 다들 친절히 알려주셔서 배우면서 프로젝트에 참여할 수 있었습니다. 앞으로의 활동에도 좋은 경험이 될 것 같습니다.
- 박예슬 : 다인 프로젝트 깃 관리의 어려움과 중요성을 체감했습니다. 고생하신 팀장님과 팀원들에게 박수를 보냅니다.
- 김민혜 : 팀장을 맡으신 민서님이 프로젝트 전반적인 과정을 꼼꼼하게 정리하고 원할하게 진행해주셨다고 생각합니다. 각 팀원이 맡은 역할에 충실할 뿐만 아니라 가진 역량을 빛내고 서로 도와 문제를 해결하는 과정을 경험할 수 있어서 정말 좋았습니다.
- 황인호 : 팀프로젝트를  제대로 수행해본적이 처음이었지만 팀장분께서 역할분담 잘해주셔서 맡은바 열심히 그리고 만족스럽게 수행한것같습니다. 앞으로의 협력 업무에 있어서 좋은 경험이 되었습니다.
- 홍승표 : 저는 사람이 아닙니다. 몽키입니다. 아닙니다. 코드도 못치니 그냥 몽키입니다. 열심히 배워서 코드몽키라도 될 수 있도록 노력하겠습니다. 그리고 능력자이신 팀원분들을 만나 너무 좋았습니다. 몽키 한 마리 만나서 고생한 팀원들에게 너무 고맙고 다음 프로젝트때는 버스 타기실 기도하겠습니다. 
