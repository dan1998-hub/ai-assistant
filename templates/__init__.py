"""Inicializador del paquete templates"""

from .base import get_template_description
from .hibot import INSTRUCTION as HIBOT_INSTRUCTION
from .phone_sales import INSTRUCTION as PHONE_SALES_INSTRUCTION
from .tech_support import INSTRUCTION as TECH_SUPPORT_INSTRUCTION
from .leads import INSTRUCTION as LEADS_INSTRUCTION
from .rrhh import INSTRUCTION as RRHH_INSTRUCTION
from .education import INSTRUCTION as EDUCATION_INSTRUCTION
from .personal import INSTRUCTION as PERSONAL_INSTRUCTION
from .health import INSTRUCTION as HEALTH_INSTRUCTION
from .ecommerce import INSTRUCTION as ECOMMERCE_INSTRUCTION

INSTRUCTION_TEMPLATES = {
    "Hibot Assistant": HIBOT_INSTRUCTION,
    "Phone Sales Expert": PHONE_SALES_INSTRUCTION,
    "Tech Support": TECH_SUPPORT_INSTRUCTION,
    "Lead Generation": LEADS_INSTRUCTION,
    "RRHH Assistant": RRHH_INSTRUCTION,
    "Education Assistant": EDUCATION_INSTRUCTION,
    "Personal Assistant": PERSONAL_INSTRUCTION,
    "Health Assistant": HEALTH_INSTRUCTION,
    "E-commerce Assistant": ECOMMERCE_INSTRUCTION,
    "Personalizado": ""
} 