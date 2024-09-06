from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    # os.system(f"start {filename}") 
    os.system(f"open {filename}")  # On Windows, use `os.system(f"start {filename}")`; on macOS, use `os.system(f"open {filename}")`

if __name__ == "__main__":
    response_text = "Hello, how can I help you?"
    text_to_speech(response_text)
