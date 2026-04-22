import mysql.connector
from pdf2image import convert_from_path
import ai_backend # Using your existing Gemini connection
import os

def process_handwritten_pdf(pdf_path, semester, stream, subject):
    print(f"⚙️ Extracting handwritten notes for {subject}...")
    
    # 1. Slice the PDF into individual image files
    pages = convert_from_path(pdf_path, poppler_path='/opt/homebrew/bin')
    full_transcription = ""

    for i, page in enumerate(pages):
        temp_img_path = f"temp_page_{i}.jpg"
        page.save(temp_img_path, 'JPEG')
        
        # 2. Ask Gemini to read the handwriting
        # (You will need to add a small function in ai_backend.py that accepts an image path!)
        prompt = "Transcribe all handwritten text, formulas, and diagrams from this page exactly as written. Format it using clean Markdown."
        
        print(f"   Reading page {i+1}...")
        page_text = ai_backend.read_image_with_ai(temp_img_path, prompt) 
        full_transcription += str(page_text) + "\n\n"
        
        os.remove(temp_img_path) # Clean up the temp image

    # 3. Inject the clean text into MySQL
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YourPasswordHere", # <-- Update this
            database="zenith"
        )
        mycursor = mydb.cursor()
        query = "INSERT INTO course_notes (semester, stream, subject, notes_text) VALUES (%s, %s, %s, %s)"
        mycursor.execute(query, (semester, stream, subject, full_transcription))
        mydb.commit()
        mycursor.close()
        mydb.close()
        print(f"✅ Successfully uploaded {subject} to the database!\n")

    except Exception as e:
        print(f"❌ Database Error: {e}")

# Run the pipeline for your subjects!
process_handwritten_pdf("Unit 1.pdf", 4, "CSE", "Operating Systems")
# process_handwritten_pdf("DBMS_Notes.pdf", 4, "CSE", "Database Management Systems")
# process_handwritten_pdf("TOC_Notes.pdf", 4, "CSE", "Theory of Computation")