import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

page_title = "Airline Passenger Satisfaction Prediction System"
page_icon = ":money_with_wings:"
layout = "wide"


# page configration ---------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.markdown(f'<h1 style="text-align: center;">Airline Passenger Satisfaction Prediction System</h1>', unsafe_allow_html=True)

df = pd.read_csv(r"C:\Users\AR KING\Downloads\ClarityTTC Task\Passenger satisfaction\test.csv")

df.dropna(inplace=True)

df.replace({"Gender": {"Male": 0, 'Female':1}}, inplace=True)
df.replace({"Class": {"Eco": 0, 'Business':1, 'Eco Plus':2}}, inplace=True)
df.replace({"Customer Type": {'Loyal Customer': 0, "disloyal Customer": 1}}, inplace=True)
df.replace({"Type of Travel": {'Business travel': 0, 'Personal Travel': 1}}, inplace=True)
df.replace({"satisfaction": {'satisfied': 0,  'neutral or dissatisfied': 1}}, inplace=True)

# select the feature and target

x = df.drop(columns=['Unnamed: 0', 'id', 'satisfaction', 'Leg room service'], axis=1)
y = df["satisfaction"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

col1, col2, col3 = st.columns(3, gap="large")

with col1:

    Gender = st.selectbox("Gender", options=["Male", "Female"])
    gen_dic = {"Male":0.0, "Female": 1.0}

    cu_type = st.selectbox("Customer Type", options=["Loyal", "Disloyal"])
    cu_dict = {"Loyal":0.0, "Disloyal":1.0}

    time = st.slider("Departure/Arrival time convenient", 0, 5, 1)

    travel = st.selectbox("Type of Travel", options=["Business", "Personal"])
    travel_dic = {"Business":0.0, "Personal":1.0}

    Flight_class = st.selectbox("Class", options=["Eco", "Business", "Eco Plus"])
    dict = {"Eco": 0.0, "Business":1.0, "Eco Plus": 2.0}

    service = st.slider('InFlight service Rating', 0, 5, 1)

    checkin_service = st.selectbox('Checkin service Rating', options=[0, 1, 2, 3, 4, 5])

with col2:

    distance = st.text_input("Flight Distance")

    age = st.text_input("Age")

    wifi = st.slider("InFlight Wifi Service Rating", 0, 5, 1)

    departure_delay = st.text_input('Departure Delay in Minutes')

    arrival_delay = st.text_input('Arrival Delay in Minutes')

    entertainment = st.slider('InFlight entertainment Rating', 0, 5, 1)

    on_board_service = st.selectbox('On-board service Rating', options=[0, 1, 2, 3, 4, 5])


with col3:

    booking = st.selectbox('Ease of Online booking Rating', options=[0, 1, 2, 3, 4, 5])

    gate_location = st.selectbox("Gate location Rating", options=[0, 1, 2, 3, 4, 5])

    food = st.slider('Food and drink Rating', 0, 5, 1)

    boarding = st.selectbox('Online boarding Rating', options=[0, 1, 2, 3, 4, 5])

    seat = st.selectbox('Seat comfort Rating', options=[0, 1, 2, 3, 4, 5])

    handling = st.slider('Baggage handling Rating', 0, 5, 1)

    clean = st.selectbox('Cleanliness Rating', options=[0, 1, 2, 3, 4, 5])


st.write("")
st.write("")
col1, col2 = st.columns([0.438, 0.562])
with col2:
    submit = st.button(label='Submit')


if submit:

    try:

        userdata = np.array([[gen_dic[Gender], cu_dict[cu_type], int(age),travel_dic[travel], dict[Flight_class],
                             int(distance), wifi, time, booking, gate_location, food, boarding, seat, entertainment,
                             on_board_service, handling, checkin_service, service, clean, int(departure_delay),
                             int(arrival_delay)]])

        test_result = model.predict(userdata)
        if test_result[0] == 0:
            st.success(f"The Passenger is Satisfied.")
            st.balloons()
        else:
            st.error(f"The Passenger is  Not Satisfied.")

    except:
        st.warning('Please fill the all required information')

