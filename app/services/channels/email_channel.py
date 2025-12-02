import smtplib
from email.message import EmailMessage
from .base import BaseChannel
from app.core import config
from app.services import template_manager
from datetime import datetime
from zoneinfo import ZoneInfo

class EmailChannel(BaseChannel):
    @staticmethod
    def format_date_time(date):
        try:
            if not date:
                return ""
            dt_utc = datetime.fromisoformat(date.replace('Z', '+00:00'))
            dt_br = dt_utc.astimezone(ZoneInfo("America/Sao_Paulo"))
            return dt_br.strftime("%d/%m/%Y às %H:%M")
        except Exception as e:
            print(f"Erro ao formatar data: {e}")
            return date

    def send(self, data: dict):
        recipient = data.get('recipient')
        template_id = data.get('template_id')
        variables = data.get('variables', {})

        if 'date' in variables and variables['date']:
            variables['date'] = self.format_date_time(variables['date'])

        print(f"Processando template '{template_id}' para {recipient}...")

        #Renderiza o HTML
        subject, html_content = template_manager.render_template(template_id, variables)

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = config.SMTP_FROM_EMAIL
        msg['To'] = recipient

        #Define o conteúdo como HTML
        msg.set_content("Seu cliente de e-mail não suporta HTML.")
        msg.add_alternative(html_content, subtype='html')

        try:
            with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT, timeout=10) as server:
                server.starttls()
                if config.SMTP_USER and config.SMTP_PASSWORD:
                    server.login(config.SMTP_USER, config.SMTP_PASSWORD)
                    server.send_message(msg)
                else:
                    print("Credenciais não configuradas.")
        except Exception as e:
            print(f"Erro ao enviar: {e}")