import os
import json
import sys
from dotenv import load_dotenv
from google import genai # 使用新的套件

# 讀取環境變數
load_dotenv()

# 初始化新的 Client
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def update_events(user_request):
    # 讀取目前的 JSON
    try:
        with open('data/events.json', 'r', encoding='utf-8') as f:
            current_data = json.load(f)
    except FileNotFoundError:
        print("錯誤：找不到 data/events.json")
        return

    # 準備提示詞
    prompt = f"""
    這是目前的網站活動 JSON 資料:
    {json.dumps(current_data, indent=2, ensure_ascii=False)}

    用戶的需求是: "{user_request}"
    請更新資料並回傳「完整的 JSON 格式」。
    注意：不要輸出任何解釋文字，只要輸出 JSON 本身。
    """

    # 使用新的 Client 呼叫模型
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite-preview',
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )
    
    # 寫回 JSON 檔案
    try:
        new_data = json.loads(response.text)
        with open('data/events.json', 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=4, ensure_ascii=False)
        print("✅ 檔案已更新成功！ (使用最新 SDK)")
    except Exception as e:
        print("❌ 更新失敗，AI 輸出的格式可能有錯：")
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        update_events(sys.argv[1])
    else:
        print("請提供更新指令")