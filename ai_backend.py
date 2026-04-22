import google.generativeai as genai
import PIL.Image 

def read_image_with_ai(image_path, prompt):
    """Uses Gemini Vision to read handwritten text from an image."""
    try:
        # 1. Open the image file
        img = PIL.Image.open(image_path)
        
        # 2. Load the vision-capable model (gemini-1.5-flash is great for this)
        model = genai.GenerativeModel('gemini-1.5-flash')  # pyright: ignore[reportAttributeAccessIssue, reportPrivateImportUsage]
        
        # 3. Send the image and the prompt to the AI
        response = model.generate_content([prompt, img])
        
        return response.text
    except Exception as e:
        return f"Error reading image: {e}"
import warnings
warnings.filterwarnings("ignore")

import os
from google import genai
import os
from google import genai
from dotenv import load_dotenv

# 1. Open the vault and get the secret key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Configure the New Client
client = genai.Client(api_key=api_key)

# 3. Create the function
def get_ai_response(prompt):
    # Using the much older and faster Gemini 1.58b Flash model! for quick responses. For more complex tasks, we can switch to the 8b or 16b models.
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text

# 4. A quick test to make sure it works!
if __name__ == "__main__":
    print("🧠 Waking up Zenith AI (v2.0)...")
    
    test_question = "Explain what a Database Primary Key is in exactly one short sentence."
    answer = get_ai_response(test_question)
    
    print(f"\n✅ AI Successfully Responded:\n{answer}")