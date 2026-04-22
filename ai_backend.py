import warnings
warnings.filterwarnings("ignore")

import os
import PIL.Image
from google import genai
from dotenv import load_dotenv

# 1. Open the vault and get the secret key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Configure the New Client
client = genai.Client(api_key=api_key)

# 3. Create the standard chat function
def get_ai_response(prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

# 4. Add back the "Eyes" for the PDF Uploader!
def read_image_with_ai(image_path, prompt):
    try:
        img = PIL.Image.open(image_path)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[prompt, img]
        )
        return response.text
    except Exception as e:
        return f"Error reading image: {e}"

# 5. A quick test to make sure it works!
if __name__ == "__main__":
    print("🧠 Waking up Zenith AI (v2.0)...")
    test_question = "Explain what a Database Primary Key is in exactly one short sentence."
    answer = get_ai_response(test_question)
    print(f"\n✅ AI Successfully Responded:\n{answer}")