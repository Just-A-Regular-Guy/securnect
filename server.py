import socket
import threading

# Funzione per la gestione dei client
def handle_client(client_socket, username):
    while True:
        try:
            # Ricevi il messaggio dal client
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                print(f"{username} si è disconnesso.")
                break

            # Analizza il messaggio per determinare il destinatario
            recipient, message_body = message.split(':', 1)

            # Invia il messaggio al destinatario
            if recipient in clients:
                recipient_socket = clients[recipient]
                recipient_socket.send(f"[{username}]: {message_body}".encode("utf-8"))
            else:
                client_socket.send(f"Errore: l'utente {recipient} non esiste.".encode("utf-8"))
        except Exception as e:
            print(f"Errore durante la gestione del client {username}: {e}")
            break

    # Chiudi la connessione col client
    client_socket.close()
    del clients[username]

# Configurazione del server
HOST = '172.31.39.174'
PORT = 12345

# Inizializza il socket del server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server in ascolto su {HOST}:{PORT}")

# Dizionario per tenere traccia dei client connessi
clients = {}

# Loop principale per accettare i client
while True:
    client_socket, address = server.accept()
    print(f"Connessione da {address}.")

    # Ricevi il nome utente dal client
    username = client_socket.recv(1024).decode("utf-8")

    # Aggiungi il client alla lista dei client connessi
    clients[username] = client_socket

    # Avvia un thread per gestire il client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
    client_handler.start()
