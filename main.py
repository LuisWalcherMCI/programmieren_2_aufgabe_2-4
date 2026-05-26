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
        fig2 = px.line(
            df.head(2000),
            x=df.index,
            y="Power",
            title="PowerOriginal Verlauf",
        ) 
        fig2.update_xaxes(title_text="Zeit in Sekunden")

        st.plotly_chart(fig2)





