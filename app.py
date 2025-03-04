import streamlit as st
import requests
import os
from dotenv import load_dotenv
from templates import INSTRUCTION_TEMPLATES, get_template_description
from uuid import uuid4  # Para generar conversation_ids únicos

# Cargar variables de entorno
load_dotenv()
TENANT_ID = os.getenv("TENANT_ID")
API_KEY = os.getenv("API_KEY")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
ORCHESTRATOR_URL = os.getenv("ORCHESTRATOR_URL")
PROMPT_CONFIG_URL = os.getenv("PROMPT_CONFIG_URL")

# Inicializar sesión de chat y conversation_id
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    st.session_state["conversation_id"] = str(uuid4())

# Definir avatares para cada asistente
ASSISTANT_AVATARS = {
    "Hibot Assistant": {"emoji": "💚", "name": "Andrés"},
    "Phone Sales Expert": {"emoji": "📱", "name": "Pedro"},
    "Tech Support": {"emoji": "🔧", "name": "Carlos"},
    "Lead Generation": {"emoji": "🎯", "name": "Sofía"},
    "RRHH Assistant": {"emoji": "👥", "name": "Ana"},
    "Education Assistant": {"emoji": "📚", "name": "Laura"},
    "Personal Assistant": {"emoji": "✨", "name": "María"},
    "Health Assistant": {"emoji": "🌿", "name": "Daniel"},
    "E-commerce Assistant": {"emoji": "🛍️", "name": "Lucas"},
    "Personalizado": {"emoji": "🤖", "name": "Asistente"}
}

# Configurar instrucciones del agente - Simple llamada al endpoint
def set_orchestrator_instructions():
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    payload = {
        "tenant": TENANT_ID,
        "instruction": st.session_state.instruction
    }
    response = requests.patch(PROMPT_CONFIG_URL, json=payload, headers=headers)
    if response.status_code == 200:
        # Generar nuevo conversation_id y limpiar mensajes
        st.session_state["conversation_id"] = str(uuid4())
        st.session_state["messages"] = []
        st.success("✅ Instrucciones actualizadas")
    else:
        st.error("❌ Error al actualizar instrucciones")

# Chat con el agente - Simple llamada al endpoint
def chat_with_agent(user_input):
    headers = {"x-api-key": API_KEY}
    payload = {
        "tenant_id": TENANT_ID,
        "conversation_id": st.session_state["conversation_id"],
        "content": user_input
    }
    response = requests.post(ORCHESTRATOR_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("response", "Sin respuesta")
    return "Error al procesar el mensaje"

# UI
st.title("🤖 AI Assistant")

# Sidebar con instrucciones
with st.sidebar:
    st.header("💭 Instrucciones")
    
    template_choice = st.selectbox(
        "Seleccionar Asistente",
        options=list(INSTRUCTION_TEMPLATES.keys())
    )
    
    # Mostrar avatar del asistente actual con mejor diseño
    current_assistant = ASSISTANT_AVATARS[template_choice]
    st.write(
        f"""
        <div style="
            padding: 0.7rem;
            border-radius: 0.5rem;
            background: #1E1E1E;
            margin: 0.5rem 0;
            text-align: center;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            <div style="
                font-size: 1.5rem;
                background: #2E2E2E;
                padding: 0.3rem;
                border-radius: 0.3rem;
                min-width: 2.5rem;
            ">
                {current_assistant['emoji']}
            </div>
            <div style="
                flex-grow: 1;
                text-align: left;
            ">
                <div style="
                    color: #FFFFFF;
                    font-weight: bold;
                    font-size: 0.9rem;
                    margin-bottom: 0.1rem;
                ">
                    {current_assistant['name']}
                </div>
                <div style="
                    color: #A0A0A0;
                    font-size: 0.7rem;
                ">
                    {get_template_description(template_choice)}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    instruction_text = "" if template_choice == "Personalizado" else INSTRUCTION_TEMPLATES[template_choice]
    
    st.text_area(
        "Personalizar Instrucciones",
        value=instruction_text,
        key="instruction",
        height=150
    )
    
    st.button("Guardar Instrucciones", type="primary", on_click=set_orchestrator_instructions)

# Chat
current_emoji = ASSISTANT_AVATARS[template_choice]["emoji"]
for msg in st.session_state["messages"]:
    with st.chat_message(
        msg["role"],
        avatar=current_emoji if msg["role"] == "assistant" else None
    ):
        st.markdown(msg["content"])

if user_input := st.chat_input("Envía un mensaje..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    response = chat_with_agent(user_input)
    
    with st.chat_message("assistant", avatar=current_emoji):
        st.markdown(response)
    st.session_state["messages"].append({"role": "assistant", "content": response})
