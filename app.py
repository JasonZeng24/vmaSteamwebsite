import streamlit as st
import json
from google import genai
from github import Github

# --- 1. 設定 ---
api_key = st.secrets.get("GOOGLE_API_KEY")
github_token = st.secrets.get("GITHUB_TOKEN")
admin_pw = st.secrets.get("ADMIN_PASSWORD")

client = genai.Client(api_key=api_key)

# 檔案路徑對應表
FILE_MAP = {
    "Events": "data/events.json",
    "Courses": "data/courses.json",
    "Faculty": "data/faculty.json"
}

st.title("🚀 STEAM Dept Admin Dashboard")

# 密碼檢查
input_pw = st.text_input("Admin Password", type="password")

if input_pw == admin_pw:
    # 選擇要更新的檔案
    target_category = st.selectbox("Select which section to update:", list(FILE_MAP.keys()))
    file_path = FILE_MAP[target_category]
    
    user_request = st.text_area(f"What do you want to update in {target_category}?")
    
    if st.button("Update Website"):
        if not user_request:
            st.warning("Please enter a request.")
        else:
            with st.spinner(f"Updating {target_category}..."):
                try:
                    g = Github(github_token)
                    repo = g.get_repo("JasonZeng24/vmaSteamwebsite")
                    contents = repo.get_contents(file_path)
                    current_json_str = contents.decoded_content.decode()
                    
                    # AI Prompt 優化：明確告訴模型它在處理哪個檔案
                    prompt = f"""
                    You are a data management assistant for a website.
                    Context: You are updating the '{target_category}' section.
                    Current JSON data: {current_json_str}
                    Request: {user_request}
                    
                    Please process this request.
                    IMPORTANT: 
                    1. Output ONLY valid JSON.
                    2. Keep the original schema/structure.
                    3. Do not include markdown backticks or explanations.
                    """
                    
                    response = client.models.generate_content(
                    model='gemini-3.1-flash-lite-preview', 
                    contents=prompt,
                    config={"response_mime_type": "application/json"}
                    )
                    
                    # 簡單的 JSON 校驗
                    new_data = json.loads(response.text)
                    final_json_str = json.dumps(new_data, indent=4)
                    
                    repo.update_file(
                        path=file_path,
                        message=f"chore: auto-update {target_category} via dashboard",
                        content=final_json_str,
                        sha=contents.sha
                    )
                    
                    st.success(f"✅ {target_category} updated successfully!")
                except Exception as e:
                    st.error(f"❌ Error occurred: {e}")
else:
    if input_pw:
        st.error("Wrong password!")
