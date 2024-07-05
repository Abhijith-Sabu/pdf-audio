from gtts import gTTS
import PyPDF2
import os

def pdf_audio(pdf, output):
    with open(pdf, 'rb') as file:  # Change 'wb' to 'rb' for reading
        pypdf = PyPDF2.PdfReader(file)

        full_text = ""
        for page in pypdf.pages:
            full_text += page.extract_text() + ' '

    tts = gTTS(text=full_text, lang='en')
    tts.save(output)
    print("Audio file created...")
    os.startfile(output)  # On Windows

path = r"C:\Users\abhij\Documents\pdf-test2.pdf"
audio = "audio_file.mp3"

pdf_audio(pdf=path, output=audio)
