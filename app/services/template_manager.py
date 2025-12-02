import os
from jinja2 import Environment, FileSystemLoader

#Configuração do Jinja2 para ler da pasta app/templates
template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
env = Environment(loader=FileSystemLoader(template_dir))

# Configuração dos Templates (Mapeamento ID -> Arquivo e Assunto)
TEMPLATE_MAP = {
    "REGISTRATION": {
        "file": "registration.html",
        "subject": "Confirmação de Inscrição"
    },
    "REGISTRATION_CANCEL": {
        "file": "registration_cancel.html",
        "subject": "Cancelamento de Inscrição"
    },
    "REGISTRATION_CHECKIN": {
        "file": "registration_checkin.html",
        "subject": "Obrigado por comparecer!"
    }
}

def render_template(template_id: str, variables: dict):
    print("DADOSSSSSSSSSSSS -> ",variables)
    config = TEMPLATE_MAP.get(template_id.upper())

    if not config:
        # Se o template não existir manda texto simples
        return "Nova Notificação", str(variables)

    template = env.get_template(config["file"])
    html_content = template.render(**variables)

    return config["subject"], html_content