# interface.py

import gradio as gr
import requests

# URL del servidor Flask en localhost
FLASK_SERVER_URL = "http://localhost:5001/execute"

# Función para enviar la tarea al servidor Flask
def run_model(task_input, model_choice):
    if not task_input:
        return "Error: Por favor ingrese una tarea."

    # Preparar los datos para enviar al servidor
    payload = {
        "task": task_input,
        "model": model_choice
    }

    try:
        # Enviar solicitud POST al servidor Flask
        response = requests.post(FLASK_SERVER_URL, json=payload)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP

        # Procesar la respuesta del servidor
        result = response.json().get("result", "No se recibió resultado")
        return format_result(result, model_choice)
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con el servidor: {str(e)}"

# Función auxiliar para formatear el resultado
def format_result(result, model_name):
    if result:
        try:
            # Si el resultado es un string JSON, lo parseamos
            import json
            data = json.loads(result) if isinstance(result, str) else result
            if isinstance(data, dict) and "posts" in data:
                posts = data["posts"]
                output = f"Resultado del modelo {model_name}:\n\n"
                for post in posts:
                    output += f"Título: {post.get('title', 'N/A')}\n"
                    output += f"URL: {post.get('url', 'N/A')}\n"
                    output += f"Likes: {post.get('likes', 'N/A')}\n"
                    output += f"Suscriptores: {post.get('subscriptores', post.get('subscribers', 'N/A'))}\n\n"
                return output
            else:
                return f"Resultado del modelo {model_name}: {str(data)}"
        except Exception as e:
            return f"Error al procesar el resultado del modelo {model_name}: {str(e)}"
    return f"No se obtuvo resultado del modelo {model_name}."

# Crear la interfaz de Gradio
with gr.Blocks(title="Selector de Modelos") as demo:
    gr.Markdown("# Interfaz para Ejecutar Modelos GPT o AWS")
    task_input = gr.Textbox(label="Ingrese la tarea (task)", placeholder="Escriba aquí la tarea...")
    model_choice = gr.Radio(choices=["GPT", "AWS"], label="Seleccione el modelo", value="GPT")
    output = gr.Textbox(label="Resultado", interactive=False)
    submit_btn = gr.Button("Ejecutar")

    # Conectar el botón con la función run_model
    submit_btn.click(
        fn=run_model,
        inputs=[task_input, model_choice],
        outputs=output
    )

# Lanzar la interfaz
demo.launch(server_port=7861)