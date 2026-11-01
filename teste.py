from dotenv import load_dotenv
load_dotenv()
from google import genai
cliente = genai.Client()
resposta = cliente.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=["explique para mim o que é uma API?"]
)
print(resposta.text)