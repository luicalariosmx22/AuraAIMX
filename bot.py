import openai
from config import OPENAI_API_KEY

# Inicializa la API de OpenAI
openai.api_key = OPENAI_API_KEY

def preguntar_a_gpt(mensaje_usuario):
    try:
        response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=mensaje_usuario, 
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error al preguntar a GPT: {e}")
        return "Lo siento, hubo un problema al procesar tu mensaje."
