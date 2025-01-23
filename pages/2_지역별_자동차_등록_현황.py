import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px

st.title("📊 지역별 자동차 등록 현황")
st.divider()

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

selected_year = st.selectbox("Year", year_list, index=year_list.index('2022'))

st.divider()

car_data = f"""
SELECT City.CityName, Car.CarCount
FROM Car
JOIN City ON Car.CityID = City.CityID
WHERE Car.Year = {selected_year}
ORDER BY City.CityID
;
"""
cursor.execute(car_data)
result = cursor.fetchall()

df = pd.DataFrame(result)

city_order = df['CityName'].tolist()

fig = px.pie(df, names = "CityName", values="CarCount",
             hover_data={'CarCount': True}, labels={'CarCount': 'CarCount'},
             category_orders={'CityName': city_order})
fig.update_traces(textposition='outside', textinfo='label+value+percent', textfont_color="black",
                  hole=.4, direction='counterclockwise', rotation=-30)
fig.add_annotation(dict(text=f"{selected_year}", x=0.5, y=0.5, font_color="black", font_size=25, showarrow=False))
fig.update_layout(
    height=600
)
st.plotly_chart(fig)