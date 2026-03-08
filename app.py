import streamlit as st
import agent # 直接呼叫你寫好的那個 agent.py

st.title("VMA Steam website admin portal")
st.subheader("Add events")

# 輸入欄位
event_info = st.text_input("Input event (ex: 10/30 science fair, welcome)")

if st.button("PUSH UPDATE"):
    if event_info:
        st.write("Calling AI Agent...")
        # 直接呼叫你寫好的函數
        agent.update_events(event_info)
        st.success("Success！Updating to GitHub...")
    else:
        st.warning("PLZ INPUT")
