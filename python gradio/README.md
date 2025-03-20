# **Proyecto: Interfaz Gradio con Flask y Modelos GPT/AWS**

Este proyecto implementa una interfaz de usuario basada en **Gradio** que permite ejecutar tareas en dos modelos distintos (**GPT** y **AWS Bedrock**) a través de un servidor **Flask**. La aplicación está diseñada para pruebas locales en `localhost`, con **Gradio** corriendo en el puerto `7861` y **Flask** en el puerto `5000`.

---

## **Descripción**

- **Interfaz Gradio (`interface.py`)**:  
    Proporciona una interfaz web donde los usuarios pueden ingresar una tarea (*task*) y seleccionar un modelo (**GPT** o **AWS**). Envía solicitudes al servidor Flask.

- **Servidor Flask (`server.py`)**:  
    Recibe las solicitudes de Gradio, ejecuta la tarea en el modelo seleccionado usando las funciones definidas en `init.py`, y devuelve los resultados.

- **Lógica de modelos (`init.py`)**:  
    Contiene las funciones `mainGPT` y `mainAws` que procesan las tareas usando **ChatOpenAI (GPT)** y **ChatBedrock (AWS)**, respectivamente.

---

## **Requisitos**

- **Python** 3.8 o superior  
- Un entorno virtual (**recomendado**)  
- Dependencias listadas en `requirements.txt` (ver más abajo)

---

## **Instalación**

1. **Clonar o descargar el proyecto**  
     Asegúrate de tener los archivos `interface.py`, `server.py` e `init.py` en el mismo directorio.

2. **Crear y activar un entorno virtual**  
     ```bash
     python -m venv .venv
     .venv\Scripts\activate  # En Windows
     source .venv/bin/activate  # En Linux/Mac
     ```

3. **Instalar dependencias**  
     Ejecuta el siguiente comando para instalar las librerías necesarias:  
     ```bash
     pip install flask waitress requests gradio langchain-openai langchain-aws nest_asyncio pydantic
     ```

     > **Nota:** Asegúrate de tener configuradas las claves de API para **OpenAI** y **AWS Bedrock** en un archivo `.env` si es necesario.

4. **Verificar el puerto**  
     - **Flask** usa el puerto `5000` por defecto.  
     - **Gradio** usa el puerto `7861`.  
     Asegúrate de que estos puertos estén libres.

---

## **Uso**

1. **Iniciar el servidor Flask**  
     En una terminal, navega al directorio del proyecto y ejecuta:  
     ```bash
     python server.py
     ```
     Verás un mensaje como:  
     `Serving on http://localhost:5000`.

2. **Iniciar la interfaz Gradio**  
     En otra terminal, en el mismo directorio, ejecuta:  
     ```bash
     python interface.py
     ```
     Abre tu navegador en `http://127.0.0.1:7861` para acceder a la interfaz.

3. **Probar la aplicación**  
     - Ingresa una tarea en el campo de texto (ejemplo: `"Visit youtube.com, search for 'Madeon - Finale'"`).  
     - Selecciona un modelo (**GPT** o **AWS**).  
     - Haz clic en **"Ejecutar"** para ver los resultados en la interfaz.

---

## **Estructura del proyecto**

```plaintext
python-gradio/
│
├── .venv/              # Entorno virtual (creado con `python -m venv .venv`)
├── interface.py        # Interfaz Gradio que se conecta al servidor Flask
├── server.py           # Servidor Flask con Waitress que ejecuta las tareas
├── init.py             # Lógica de los modelos GPT y AWS
├── .env                # (Opcional) Archivo para claves de API
└── README.md           # Este archivo
```

---

## **Notas**

- **Configuración local:**  
    Actualmente, todo está configurado para ejecutarse en `localhost`. Si deseas usar dos PCs, ajusta `FLASK_SERVER_URL` en `interface.py` con la IP del servidor Flask.

- **Dependencias externas:**  
    Asegúrate de que las librerías `browser_use` y otras específicas de `init.py` estén disponibles o instaladas.

- **Producción:**  
    **Waitress** se usa como servidor WSGI para Flask, lo que lo hace más adecuado para entornos de producción que el servidor de desarrollo por defecto.

---

## **Solución de problemas**

- **Puerto ocupado:**  
    Si el puerto `5000` o `7861` está en uso, cámbialos en `server.py` (`port=5000`) o `interface.py` (`server_port=7861`).

- **Errores de conexión:**  
    Verifica que `server.py` esté corriendo antes de iniciar `interface.py`.

- **Dependencias faltantes:**  
    Asegúrate de instalar todas las librerías mencionadas.

---

## **Contribuir**

Si deseas contribuir, crea un **fork** del proyecto, realiza tus cambios y envía un **pull request**.

---

## **Licencia**

Este proyecto no tiene una licencia específica definida. Úsalo bajo tu propio riesgo.

---

## **Personalización**

- Si tienes un nombre específico para el proyecto, reemplaza **"Proyecto: Interfaz Gradio con Flask y Modelos GPT/AWS"** por el nombre que prefieras.  
- Agrega más detalles en **"Solución de problemas"** si encuentras errores comunes al probarlo.  
- Si usas un archivo `.env` para claves de API, incluye instrucciones específicas en **"Instalación"**.

