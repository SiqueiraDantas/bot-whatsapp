import requests
import schedule
import time
from datetime import datetime
import os

TOKEN = os.environ.get("WA_TOKEN")
INSTANCE = os.environ.get("WA_INSTANCE")
NUMERO = os.environ.get("WA_NUMERO")  # ex: 5585999999999

def enviar_mensagem(texto):
    url = f"https://api.ultramsg.com/{INSTANCE}/messages/chat"
    payload = {
        "token": TOKEN,
        "to": NUMERO,
        "body": texto
    }
    requests.post(url, data=payload)

def mensagem_manha():
    dia = datetime.now().weekday()
    aulas_por_dia = {
        0: "• 18h — Matéria 1\n• 19:30 — Matéria 2",
        1: "• 18h — Matéria 3\n• 19:30 — Matéria 4",
        2: "• 18h — Matéria 5\n• 19:30 — Matéria 6",
        3: "• 18h — Matéria 7\n• 19:30 — Matéria 8",
        4: "• 18h — Matéria 9\n• 19:30 — Matéria 10",
        5: "Sem aulas hoje! 🎉",
        6: "Sem aulas hoje! 🎉",
    }
    grade = aulas_por_dia.get(dia, "Sem aulas.")
    texto = f"📚 *Bom dia!* Aulas de hoje:\n\n{grade}\n\nBora lá! 💪"
    enviar_mensagem(texto)

def aula_18h():
    enviar_mensagem("✅ Aula das 18h encerrada.")

def aula_1930():
    enviar_mensagem("✅ Aula das 19:30 encerrada.")

schedule.every().day.at("07:00").do(mensagem_manha)
schedule.every().day.at("18:20").do(aula_18h)
schedule.every().day.at("20:50").do(aula_1930)

print("✅ Bot rodando na nuvem!")
while True:
    schedule.run_pending()
    time.sleep(30)