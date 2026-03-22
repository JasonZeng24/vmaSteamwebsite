import streamlit as st
import json
import time
from google import genai
from github import Github

# --- 1. 設定 ---
api_key = st.secrets.get("GOOGLE_API_KEY")
github_token = st.secrets.get("GITHUB_TOKEN")
admin_pw = st.secrets.get("ADMIN_PASSWORD")

client = genai.Client(api_key=api_key)

# 檔案路徑與提示範例
FILE_MAP = {
    "Events": "data/events.json",
    "Courses": "data/courses.json",
    "Faculty": "data/faculty.json"
}

EXAMPLES = {
    "Events": "Add a new hackathon in May, location: Main Hall, time: 2:00 PM, category: Competition",
    "Courses": "Add a new course 'Mobile App Dev', description: Learn Swift/Kotlin, duration: Semester, prereq: Web Development, language: Swift",
    "Faculty": "Add a new faculty 'Dr. Smith', role: Physics Teacher, bio: Expert in quantum mechanics, education: PhD Physics, email: smith@school.edu"
}

st.set_page_config(page_title="STEAM Admin", page_icon="🚀")
st.title("🚀 STEAM Dept Admin Dashboard")

# --- 2. 介面 ---
input_pw = st.text_input("Admin Password", type="password")

if input_pw == admin_pw:
    target_category = st.selectbox("Select which section to update:", list(FILE_MAP.keys()))
    file_path = FILE_MAP[target_category]
    
    # 使用 placeholder 直接在输入框内引导用户
    user_request = st.text_area(
        f"What do you want to update in {target_category}?",
        placeholder=EXAMPLES[target_category],
        height=150
    )
    
    if st.button("Update Website"):
        if not user_request:
            st.warning("Please enter a request.")
        else:
            with st.spinner("AI Agent is processing..."):
                try:
                    # 1. 抓取 GitHub 檔案
                    g = Github(github_token)
                    repo = g.get_repo("JasonZeng24/vmaSteamwebsite")
                    contents = repo.get_contents(file_path)
                    current_json_str = contents.decoded_content.decode()
                    
                    # 2. AI 處理 (使用 Preview 版本模型)
                    prompt = f"""
                    You are a website data manager. 
                    Current JSON data for '{target_category}': {current_json_str}
                    Request: {user_request}
                    
                    Instructions:
                    - Update the JSON data based on the request.
                    - If it's a new entry, append it to the list.
                    - Maintain the exact field structure (keys, types, icon patterns) of the existing JSON.
                    - IMPORTANT: Return VALID JSON ONLY. No markdown backticks, no text explanations.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-3.1-flash-lite-preview', 
                        contents=prompt,
                        config={"response_mime_type": "application/json"}
                    )
                    
                    # 3. 校驗與寫入
                    new_data = json.loads(response.text)
                    final_json_str = json.dumps(new_data, indent=4)
                    
                    repo.update_file(
                        path=file_path,
                        message=f"chore: auto-update {target_category} via dashboard",
                        content=final_json_str,
                        sha=contents.sha
                    )
                    
                    st.success(f"✅ Successfully updated {target_category}!")
                    st.balloons()
                    
                except json.JSONDecodeError:
                    st.error("AI returned invalid JSON. Please try again or refine your request.")
                except Exception as e:
                    st.error(f"❌ Error occurred: {e}")
                    if "429" in str(e):
                        st.info("Quota exceeded. Please wait a few minutes before trying again.")
else:
    if input_pw:
        st.error("Wrong password!")
