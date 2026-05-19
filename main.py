import streamlit as st
import pandas as pd
from read_data import get_data_from_json, get_person_name,find_person_by_name
from PIL import Image

def callback_function():
    print(f"The User has changed to {st.session_state.current_user}")

if __name__ == "__main__":
    tab1, tab2 = st.tabs(['Userauswahl','EKG-Daten'])
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
        st.header('EKG-Daten')
        df_activity = pd.read_csv('data/activities/activity.csv', sep=';')
        
        print(df_activity)


    



