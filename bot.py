import requests
import schedule
import time
import json
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import os

# Configurações da Evolution API
API_URL = "https://evolution-api-nde1.onrender.com"
API_KEY = "minhaChaveSecreta123"
INSTANCE = "bot-aulas"
GRUPO_ID = "120363421690391111@g.us"

def enviar_mensagem(texto):
    url = f"{API_URL}/message/sendText/{INSTANCE}"
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json; charset=utf-8"
    }
    payload = {
        "number": GRUPO_ID,
        "text": texto
    }
    try:
        response = requests.post(
            url,
            data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
            headers=headers
        )
        print(f"[{datetime.now()}] Mensagem enviada: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

def mensagem_manha():
    dia = datetime.now().weekday()
    
    if dia == 0:  # Segunda
        texto = """Bom dia!!!
Uma semana abençoada e bastante produtiva a todos nós!!!

Hoje teremos aula para as Turmas:

18:00h

Bateria 1
Clarinete 2
Flauta Doce 1
Flauta Doce 2


19:30h

Flauta Transversal
Percussão
Trombone"""
    elif dia == 1:  # Terça
        texto = """Bom dia!!!
Que estejamos todos na paz!!!

Hoje teremos aula para as turmas de:

18:00h

Bateria 3
Clarinete 1
Trompete 1


19:30h

Bateria 4
Sax
Trompete 2"""
    elif dia == 2:  # Quarta
        texto = """Bom dia!!!
Que estejamos todos na paz!!!

Hoje teremos aula para as Turmas:

18:00h

Bateria 1
Clarinete 2
Flauta Doce 1
Flauta Doce 2


19:30h

Flauta Transversal
Percussão
Trombone"""
    elif dia == 3:  # Quinta
        texto = """Bom dia!!!
Que estejamos todos na paz!!!

Hoje teremos aula para as turmas de:

18:00h

Bateria 3
Clarinete 1
Flauta Doce 2


19:30h

Bateria 4
Sax
Trompete 2"""
    else:
        return
    
    enviar_mensagem(texto)

def aula_18h():
    dia = datetime.now().weekday()
    if dia <= 3:
        enviar_mensagem("Aula das 18h encerrada.")

def aula_1930():
    dia = datetime.now().weekday()
    if dia <= 3:
        enviar_mensagem("Aula das 19:30 encerrada.")

# Servidor HTTP fake (pra Render não derrubar)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot rodando!")
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
    def log_message(self, format, *args):
        return

def start_server():
    port = int(os.environ.get('PORT', 10000))
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()

# Inicia servidor fake numa thread separada
threading.Thread(target=start_server, daemon=True).start()

# Agendamento
schedule.every().day.at("07:00").do(mensagem_manha)
schedule.every().day.at("19:20").do(aula_18h)
schedule.every().day.at("20:50").do(aula_1930)

print("✅ Bot rodando!")
while True:
    schedule.run_pending()
    time.sleep(30)
