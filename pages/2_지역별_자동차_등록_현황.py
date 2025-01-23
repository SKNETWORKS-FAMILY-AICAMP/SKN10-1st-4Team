import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px
from common.insert_data import insert_data
from common.insert_data_city import insert_data_city

st.set_page_config(layout="wide")

insert_data()
insert_data_city()
st.success("Database initialized successfully!")

st.title("📊 지역별 자동차 등록 현황")
st.divider()

# Database 연결
connection = pymysql.connect(
    host = "localhost",
    user = "SKN10_4team",
    password = "skn1234",
    database = "SKN10_4team_1st",
    charset = "utf8"
)

cursor = connection.cursor(pymysql.cursors.DictCursor)

year_data = """
SELECT DISTINCT year
FROM Car
;
"""
cursor.execute(year_data)
years = cursor.fetchall()
year_list = [year['year'] for year in years]

with st.container(border=True):
    st.subheader("Year")
    selected_year = st.selectbox("Year", year_list, index=year_list.index('2022'), label_visibility="collapsed")

car_data = f"""
SELECT City.CityName, Car.CarCount, Car.CityID
FROM Car
JOIN City ON Car.CityID = City.CityID
WHERE Car.Year = {selected_year}
;
"""
cursor.execute(car_data)
result = cursor.fetchall()

df = pd.DataFrame(result)

df['CityID_Number'] = df['CityID'].str.extract(r'(\d+)').astype(int)
df = df.sort_values(by='CityID_Number')

fig = px.pie(df, names = "CityName", values="CarCount",
             hover_data={'CarCount': True}, labels={'CarCount': 'CarCount'})
fig.update_traces(textposition='outside', textinfo='label+value+percent', textfont_color="black", hole=.4,
                  direction='counterclockwise')
fig.add_annotation(dict(text=f"{selected_year}", x=0.5, y=0.5, font_color="black", font_size=25, showarrow=False))
fig.update_layout(width=1600, height=850, legend=dict(
    yanchor="top",
    y=1.05
))
st.plotly_chart(fig)