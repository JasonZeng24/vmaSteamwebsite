import streamlit as st
import json
from google import genai
import os

# 讀取 Secret
api_key = st.secrets.get("GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

st.title("STEAM Dept Admin Dashboard")
st.subheader("Manage Activities")

# 簡單密碼保護
admin_pw = st.text_input("Admin Password", type="password")
secret_pw = st.secrets.get("ADMIN_PASSWORD") or "default_pw"

if admin_pw == secret_pw:
    user_request = st.text_area("What do you want to update? (e.g., Add a new hackathon in May)")
    
    if st.button("Update Website"):
        with st.spinner("AI Agent is working..."):
            with open('data/events.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 強制要求英文輸出
            prompt = f"""
            Current JSON: {json.dumps(data)}
            Request: {user_request}
            Please process this request. IMPORTANT: Output the result in ENGLISH only and return valid JSON.
            """
            
            response = client.models.generate_content(
                model='gemini-3.1-flash-lite-preview', # 用這個最新的模型
                contents=prompt,
                config={"response_mime_type": "application/json"}
            )
            
            new_data = json.loads(response.text)
            with open('data/events.json', 'w', encoding='utf-8') as f:
                json.dump(new_data, f, indent=4, ensure_ascii=False)
            
            st.success("Success! Data updated locally.")
else:
    if admin_pw:
        st.error("Wrong password!")
