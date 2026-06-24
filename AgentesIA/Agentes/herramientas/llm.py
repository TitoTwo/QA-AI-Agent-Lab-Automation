from ollama import chat

def consultar_llm(prompt):

    respuesta = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return respuesta["message"]["content"]