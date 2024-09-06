from nlp_voice_assistant.src.speech_recognition_script import recognize_speech_from_mic
from nlp_voice_assistant.src.nlp_processing import get_response_from_gpt
from nlp_voice_assistant.src.text_to_speech import text_to_speech

def main():
    # Capture voice input
    recognized_text = recognize_speech_from_mic()
    print("User said:", recognized_text)

    # Process input text and generate a response
    response_text = get_response_from_gpt(recognized_text)
    print("AI response:", response_text)
    print(response_text)

    # Convert response text to speech and play it
    text_to_speech(response_text)

if __name__ == "__main__":
    main()
