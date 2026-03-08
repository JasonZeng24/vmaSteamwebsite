import streamlit as st
import json
from google import genai
import os
from github import Github

# --- 1. 設定與讀取 ---
# 確保這些 KEY 在 Streamlit Cloud 的 Secrets 裡面都有設定
api_key = st.secrets.get("GOOGLE_API_KEY")
github_token = st.secrets.get("GITHUB_TOKEN")
admin_pw = st.secrets.get("ADMIN_PASSWORD")

# 初始化 Gemini Client (使用新版 SDK)
client = genai.Client(api_key=api_key)

# --- 2. 介面 ---
st.title("🚀 STEAM Dept Admin Dashboard")
st.subheader("Manage Activities")

# 密碼檢查
input_pw = st.text_input("Admin Password", type="password")

if input_pw == admin_pw:
    user_request = st.text_area("What do you want to update? (e.g., Add a new hackathon in May)")
    
    if st.button("Update Website"):
        if not user_request:
            st.warning("Please enter a request.")
        else:
            with st.spinner("AI Agent is working..."):
                try:
                    # 1. 從 GitHub 抓檔案
                    g = Github(github_token)
                    repo = g.get_repo("JasonZeng24/vmaSteamwebsite")
                    contents = repo.get_contents("data/events.json")
                    current_json_str = contents.decoded_content.decode()
                    
                    # 2. AI 思考與處理 (使用你指定的 3.1 模型)
                    prompt = f"""
                    Current JSON data: {current_json_str}
                    Request: {user_request}
                    Please process this request. 
                    IMPORTANT: Output the result in ENGLISH only and return valid JSON format ONLY. 
                    No explanation, no markdown backticks.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-3.1-flash-lite-preview', 
                        contents=prompt,
                        config={"response_mime_type": "application/json"}
                    )
                    
                    # 3. 推送回 GitHub
                    repo.update_file(
                        path=contents.path,
                        message="chore: auto-update via Streamlit dashboard",
                        content=response.text,
                        sha=contents.sha
                    )
                    
                    st.success("✅ GitHub updated successfully! Your website will update in a minute.")
                except Exception as e:
                    st.error(f"❌ Error occurred: {e}")
else:
    if input_pw:
        st.error("Wrong password!")
