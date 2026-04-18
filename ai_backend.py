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