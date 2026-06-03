from langchain .chat_models import init_chat_model

GOOGLE_API_KEY = "your api key"

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY
                        )

response = model.invoke("How are you?")
response_str = (response.content[0]["text"])
print(response_str)