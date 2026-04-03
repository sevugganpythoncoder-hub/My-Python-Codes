# All the python libraries usedin the code:
import os
import json
import base64
import requests
import io
from PIL import Image
import urllib3

# 1. NETWORK & SECURITY
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_image_payload(image_path):
    """Compresses and encodes the blueprint for AI processing."""
    img = Image.open(image_path)
    img.thumbnail((1024, 1024)) 
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG', quality=85)
    return base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

def find_blueprint():
    """Automatically locates the blueprint on Desktop or OneDrive."""
    filename = "blueprint.jpg.jpg"
    base_paths = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    ]
    for bp in base_paths:
        full_path = os.path.join(bp, filename)
        if os.path.exists(full_path):
            return full_path
    return None

def run_universal_engine():
    print("--- 🏗️ UNIVERSAL LAYOUT ANALYZER v3.0 ---")
    
  # STEP 1: FIND FILE
    image_path = find_blueprint()
    if not image_path:
        print("❌ Error: 'blueprint.jpg.jpg' not found on Desktop.")
        return
    print(f"✅ Target Located: {image_path}")

  # STEP 2: CHOOSE PROVIDER
    print("\nSelect AI Provider:")
    print("1. Google Gemini (Flash/Pro)")
    print("2. Anthropic Claude (Coming Soon)")
    choice = input("Enter choice (1): ") or "1"

    api_key = input("🔑 Enter your API Key: ").strip()
    if not api_key:
        print("❌ Error: API Key required.")
        return

  # STEP 3: EXECUTE (GEMINI TRACK)
    if choice == "1":
        model = "gemini-2.0-flash" # The CEO can change this to 2.5-pro if needed
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        
        encoded_image = get_image_payload(image_path)
        
        payload = {
            "contents": [{
                "parts": [
                    {"text": "Analyze this layout. Count every plot. Identify 'Sold' (Green/Crosshatch) vs 'Unsold' (White). Return ONLY JSON: {'total_plots': 271, 'sold': 100, 'unsold': 171}"},
                    {"inline_data": {"mime_type": "image/jpeg", "data": encoded_image}}
                ]
            }]
        }

        print(f"📡 Processing with {model}...")
        try:
            response = requests.post(url, json=payload, verify=False, timeout=60)
            if response.status_code == 200:
                result = response.json()
                text_out = result['candidates'][0]['content']['parts'][0]['text']
                print("\n--- 📊 FINAL ANALYSIS ---")
                print(text_out)
            else:
                print(f"❌ API Error {response.status_code}: {response.text}")
        except Exception as e:
            print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    run_universal_engine()
