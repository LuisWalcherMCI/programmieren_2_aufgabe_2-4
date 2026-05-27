import streamlit as st
import pandas as pd
from read_data import get_data_from_json, get_person_name,find_person_by_name
from PIL import Image
from read_pandas import make_plot, read_csv,set_zones
import plotly.express as px
from create_plot import create_fig


def callback_function():
    print(f"The User has changed to {st.session_state.current_user}")

if __name__ == "__main__":
    tab1, tab2 = st.tabs(['Userselection','Activity-Analysis'])
    with tab1:
        col1, col2 = st.columns(2)
        person = get_data_from_json("data/person_db.json")
        person_name = get_person_name(person)
        with col1:  
            st.write("# EKG APP")
            st.write("## Versuchsperson auswählen")
            st.session_state.current_user = st.selectbox(
                'Versuchsperson',
                options = person_name, key="sbVersuchsperson")
            
        callback_function()
        user = find_person_by_name(st.session_state.current_user,person)

        if user == None:
            st.session_state.picture_path = 'data/pictures/none.jpg'

        elif st.session_state.current_user in person_name:
            st.session_state.picture_path = user['picture_path']

        with col2:
            image = Image.open(st.session_state.picture_path)
            st.image(image,caption=st.session_state.current_user)
    with tab2:
        colnames = ["Duration","HeartRate","PowerOriginal"]
        df = read_csv("data/activities/activity.csv",colnames)
        MaxHR= st.number_input("Maximum Heartrate:",value=df["HR"].max(),step=10, min_value = df["HR"].max())
        df = set_zones(df,MaxHR)
        fig = create_fig(df)
        st.plotly_chart(fig)
        Power_stats = pd.DataFrame(
        {
            "Value": [
                f"{df['Power'].mean().round(2)} mV",
                f"{df['Power'].max()} mV",

                f"{df['Z1'].sum()} s",
                f"{df['Z1'].mean().round(2)} mV",

                f"{df['Z2'].sum()} s",
                f"{df['Z2'].mean().round(2)} mV",

                f"{df['Z3'].sum()} s",
                f"{df['Z3'].mean().round(2)} mV",

                f"{df['Z4'].sum()} s",
                f"{df['Z4'].mean().round(2)} mV",

                f"{df['Z5'].sum()} s",
                f"{df['Z5'].mean().round(2)} mV",
            ]
        },
        index=[
            "Average Power",
            "Max Power",
            "Z1-Average-Power",
            "Z1-Time",
            "Z2-Average-Power",
            "Z2-Time",
            "Z3-Average-Power",
            "Z3-Time",
            "Z4-Average-Power",
            "Z4-Time",
            "Z5-Average-Power",
            "Z5-Time",
        ],
    )

    st.table(Power_stats)





