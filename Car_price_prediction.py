import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score


car=pd.read_csv('quikr_car.csv') # Upload the file having quickr data...

st.write("Welcome to Car Price Prediction APP :--")

st.write("Enter the name of car model")
car_name=st.text_input('Enter the name of car...',placeholder='Enter the car you want to search')
car_company=st.text_input('Enter the name of car company...',placeholder='Enter the car company you want to search')
car_year=st.number_input('Enter the year of car...',placeholder='Enter the car manufacturing year you want to search')
car_travel=st.number_input('Enter the distance travelled by car...',placeholder='Enter the maximum distance travelled by car you want to search')
car_fuel_type=st.text_input('Enter the fuel type of car...',placeholder='Enter the fuel variant of car you want to search')
st.write(car_fuel_type)

car=car[car['year'].str.isnumeric()]   #to pick only numeric values
car['year']=car['year'].astype(int)   #to convert year data in number form

car=car[car['Price']!='Ask For Price']  # filtering the price column
car['Price']=car['Price'].str.replace(',','').astype(int)   # Price filter and convert into numeric form
car['kms_driven']=car['kms_driven'].str.split(' ').str.get(0).str.replace(',','')
car=car[car['kms_driven'].str.isnumeric()]
car['kms_driven']=car['kms_driven'].astype(int)
car=car[~car['fuel_type'].isna()]
car['name']=car['name'].str.split(' ').str.slice(start=0,stop=3).str.join(' ')
car=car.reset_index(drop=True)  # index reset

clean_car_data=car.to_csv("clean_car_data.csv")
clean_car=pd.read_csv('clean_car_data.csv')
X=clean_car[['name','company','year','kms_driven','fuel_type']]
y=clean_car['Price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=30)

ohe=OneHotEncoder()
ohe.fit(X[['name','company','fuel_type']])
column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),remainder='passthrough')
lr=LinearRegression()
pipe=make_pipeline(column_trans,lr)
pipe.fit(X_train,y_train)
y_pred=pipe.predict(X_test)
result=r2_score(y_test,y_pred)
st.write(result)
d1=pipe.predict(pd.DataFrame(columns=X_test.columns,data=np.array([car_name,car_company,car_year,car_travel,car_fuel_type]).reshape(1,5)))
st.write(d1)

# st.write(car['year'][0]+car['year'][1])


# st.write(car['kms_driven'][0]+car['kms_driven'][1])
