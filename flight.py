# need full package
import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_excel(r"C:\Users\AR KING\Downloads\ClarityTTC Task\price prediction\Data_Train.xlsx")

df.dropna(inplace=True)

df.replace(
    {"Airline": {"IndiGo": 0, 'Air India': 1, 'Jet Airways': 2, 'SpiceJet': 3, 'Multiple carriers': 4, 'GoAir': 5,
                 'Vistara': 6, 'Air Asia': 7, 'Vistara Premium economy': 8, 'Jet Airways Business': 9,
                 'Multiple carriers Premium economy': 10, 'Trujet': 11}}, inplace=True)

df.replace({"Source": {"Banglore": 0, "Kolkata": 1, "Chennai": 2, "Delhi": 3, "Mumbai": 4}}, inplace=True)

df.replace({"Destination": {"Banglore": 0, "Kolkata": 1, "Cochin": 2, "New Delhi": 3, "Delhi": 4, "Hyderabad": 5}},
           inplace=True)

df.replace({"Total_Stops": {"non-stop": 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4}}, inplace=True)

df["Journey_day"] = pd.to_datetime(df.Date_of_Journey, format="%d/%m/%Y").dt.day

df["Journey_month"] = pd.to_datetime(df.Date_of_Journey, format="%d/%m/%Y").dt.month

df["Journey_year"] = pd.to_datetime(df.Date_of_Journey, format="%d/%m/%Y").dt.year

df.drop(["Date_of_Journey"], axis=1, inplace=True)

df.drop(["Route"], axis=1, inplace=True)

df.drop(["Additional_Info"], axis=1, inplace=True)

# Departure time is when a plane leaves the gate.
# Similar to Date_of_Journey we can extract values from Dep_Time

# Extracting Hours
df["Dep_hour"] = pd.to_datetime(df["Dep_Time"]).dt.hour

# Extracting min
df["Dep_min"] = pd.to_datetime(df["Dep_Time"]).dt.minute

# Now we can drop Dep_Time as it is of no use
df.drop(["Dep_Time"], axis=1, inplace=True)

# Arrival time is when the plane pulls up to the gate.
# Similar to Date_of_Journey we can extract values from Arrival_Time

# Extracting Hours
df["Arrival_hour"] = pd.to_datetime(df.Arrival_Time).dt.hour

# Extracting minute
df["Arrival_minute"] = pd.to_datetime(df.Arrival_Time).dt.minute

# Now we can drop Dep_Time as it is of no use
df.drop(["Arrival_Time"], axis=1, inplace=True)

df.drop(["Duration"], axis=1, inplace=True)

from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

x = df.drop(columns=["Price"], axis=1)
y = df["Price"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

page_title = "Flight Price Prediction System"
page_icon = ":money_with_wings:"
layout = "wide"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.markdown(f'<h1 style="text-align: center;">Flight Price Prediction System</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    airline = st.selectbox("Airline", options=['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
                                               'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
                                               'Vistara Premium economy', 'Jet Airways Business',
                                               'Multiple carriers Premium economy', 'Trujet'])

    air_dict = {"IndiGo": 0.0, 'Air India': 1.0, 'Jet Airways': 2.0, 'SpiceJet': 3.0, 'Multiple carriers': 4.0,
                'GoAir': 5.0,
                'Vistara': 6.0, 'Air Asia': 7.0,
                'Vistara Premium economy': 8.0, 'Jet Airways Business': 9.0, 'Multiple carriers Premium economy': 10.0,
                'Trujet': 11.0}

    source = st.selectbox("Source", options=['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])

    source_dict = {"Banglore": 0.0, "Kolkata":1.0, "Chennai": 2.0, "Delhi": 3.0, "Mumbai":4.0}

    destination = st.selectbox("Destination", options=['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi',
                                                       'Hyderabad'])

    des_dict = {"Banglore": 0.0, "Kolkata":1.0, "Cochin": 2.0, "New Delhi": 3.0, "Delhi":4.0, "Hyderabad": 5.0}

    day = st.text_input("Day of the Journey", placeholder="EX - 25th day")

    month = st.text_input("Month of the Journey", placeholder="EX - 2th Month")


with col2:

    hour = st.text_input("Departure Time", placeholder="Ex - Only enter the hours")

    minute = st.text_input("Departure Time", placeholder="Ex - Only enter the Minute")

    year = st.text_input("Year of the Journey",  placeholder="EX -2023")

    a_hour = st.text_input("Arrival Time", placeholder="Ex - Only enter the hours")

    a_min = st.text_input("Arrival Time", placeholder="Ex - Only enter the Minute")


stops = st.slider("Total Stops", 0, 5, 1)

st.write("")
st.write("")
col1, col2 = st.columns([0.438, 0.562])
with col2:
    submit = st.button(label='Submit')


if submit:

    try:

        userdata = np.array([[air_dict[airline], source_dict[source], des_dict[destination], stops, int(day), int(month),
                              int(year), int(hour), int(minute), int(a_hour), int(a_min)]])

        result = model.predict(userdata)
        st.success(f"The Price of the Flight Ticket is ( {result[0]:.2f} ).")
        st.balloons()

    except:
        st.warning('Please fill the all required information')












