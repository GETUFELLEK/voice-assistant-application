
import openai
import os

# Use your actual OpenAI API key, make sure not to expose it in production code.
openai.api_key='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'
def get_response_from_gpt(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide detailed and accurate responses."},
                {"role": "user", "content": text}
            ],
            max_tokens=150,  # Increase max tokens for more detailed responses
            temperature=0.7,  # Adjust temperature for creativity
            top_p=0.9,  # Use top-p sampling
            frequency_penalty=0.5,  # Penalize repeated phrases
            presence_penalty=0.5  # Encourage new topics
        )
        return response['choices'][0]['message']['content']
    except openai.error.RateLimitError:
        return "You have exceeded your API quota. Please check your plan and billing details."
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    user_input = "Please provide a detailed 3-day vacation plan for a family and friends trip. Include activities, places to visit, and any travel tips."
    response_text = get_response_from_gpt(user_input)
    print("AI response:", response_text)


# def get_response_from_gpt(text):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": text}
#             ],
#             max_tokens=20  # Limit the number of tokens to control usage
#         )
#         return response['choices'][0]['message']['content']
#     except openai.error.RateLimitError as e:
#         return "You have exceeded your API quota. Please check your plan and billing details."

# if __name__ == "__main__":
#     user_input = "Hello, how can I help you?"
#     response_text = get_response_from_gpt(user_input)
#     print("AI response:", response_text)
