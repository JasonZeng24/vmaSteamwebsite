import streamlit as st
import json
from google import genai
import os
from github import Github  # <--- 新增這個

# 讀取 Secrets
api_key = st.secrets.get("GOOGLE_API_KEY")
github_token = st.secrets.get("GITHUB_TOKEN")
admin_pw = st.secrets.get("ADMIN_PASSWORD")

client = genai.Client(api_key=api_key)

# 密碼檢查
input_pw = st.text_input("Admin Password", type="password")

if input_pw == admin_pw:
    user_request = st.text_area("Update Request:")
    if st.button("Update Website"):
        with st.spinner("AI is updating GitHub..."):
            # 1. 先用 GitHub API 抓出舊檔案
            g = Github(github_token)
            repo = g.get_repo("JasonZeng24/vmaSteamwebsite")
            contents = repo.get_contents("data/events.json")
            current_json_str = contents.decoded_content.decode()
            
            # 2. 讓 AI 修改
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=f"Update this JSON: {current_json_str} with: {user_request}",
                config={"response_mime_type": "application/json"}
            )
            
            # 3. 寫回 GitHub (這一步直接更新你的 Repo！)
            repo.update_file(
                path=contents.path,
                message="chore: auto-update via Streamlit dashboard",
                content=response.text,
                sha=contents.sha
            )
            st.success("GitHub updated successfully! Your website will update in a minute.")
