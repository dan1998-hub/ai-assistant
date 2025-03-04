"""Template base con funciones comunes"""

def get_template_description(template_name: str) -> str:
    """Retorna la descripción de un template"""
    return TEMPLATE_DESCRIPTIONS.get(template_name, "")

TEMPLATE_DESCRIPTIONS = {
    "Hibot Assistant": "Asistente oficial de Hibot con acceso a base de conocimiento",
    "Phone Sales Expert": "Especializado en ventas de teléfonos con sistema de recomendación",
    "Tech Support": "Soporte técnico profesional y solución de problemas",
    "Lead Generation": "Especialista en captación y calificación de leads",
    "RRHH Assistant": "Asistente de recursos humanos y gestión de personal",
    "Education Assistant": "Tutor personalizado para aprendizaje y educación",
    "Personal Assistant": "Ayudante personal para tareas y organización diaria",
    "Health Assistant": "Consejero de salud y bienestar",
    "E-commerce Assistant": "Especialista en compras online y recomendaciones",
    "Personalizado": "Define tus propias instrucciones"
} 