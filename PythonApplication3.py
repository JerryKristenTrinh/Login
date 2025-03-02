#streamlit run login.py
import streamlit as st
import time
import random

ten_kt = "admin"
mk_kt = "123456"
cheat = "█¶◙è"

ran = random.uniform(0.01, 0.4)
st.title("████████████████████████████████████████████████████")
st.title("Login your account")

kiem = st.text_input("Câu lệnh:")
ten = st.text_input("Name:")
mk = st.text_input("Password:")
nhap = st.button("Login")

if nhap:
    if ten == ten_kt and mk == mk_kt:
        st.write("Your account has been login successfully")
        if kiem == cheat:
            for i in range(4):
                st.balloons()

        else:
            for i in range(100):
                if i == 96:
                    st = st.progress(i+4)
                    break
                st = st.progress(i+4)
                time.sleep(ran)
        
            for i in range(4):
                st.balloons()
    else:
        st.write("Check your account name or password")
