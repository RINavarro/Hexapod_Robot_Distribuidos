import socket
import time
from bailes import bailes  # Importamos la clase que maneja los movimientos

# Configuración del servidor UDP
UDP_IP = "0.0.0.0"  # Escucha en todas las interfaces
UDP_PORT = 8888      # Puerto donde escuchará el servidor
TIMEOUT = 0.1        # Tiempo de espera antes de considerar que no hay comando activo

# Crear socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(TIMEOUT)  # Configurar tiempo de espera para recibir datos

# Inicializar el controlador de movimientos
hexapod = bailes()

print(f"Servidor UDP escuchando en {UDP_IP}:{UDP_PORT}")

current_command = "STOP"  # Estado inicial

while True:
    try:
        # Intentar recibir datos del cliente (Unity)
        data, addr = sock.recvfrom(1024)  # Tamaño máximo de los datos recibidos
        command = data.decode().strip()
        print(f"Comando recibido: {command}")
        
        # Actualizar el comando actual solo si es diferente
        if command != current_command:
            current_command = command

    except socket.timeout:
        # Si no se recibe ningún comando dentro del tiempo de espera, detener el hexápodo
        current_command = "STOP"

    # Ejecutar el comando actual
    if current_command == "FORWARD":
        hexapod.move("0", "20", "10", "0")  # Avance recto
    elif current_command == "BACKWARD":
        hexapod.move("0", "-20", "10", "0")  # Retroceso
    elif current_command == "LEFT":
        hexapod.move("-20", "0", "10", "0")  # Movimiento lateral izquierda
    elif current_command == "RIGHT":
        hexapod.move("20", "0", "10", "0")  # Movimiento lateral derecha
    elif current_command == "STOP":
        hexapod.altura()  # Volver a la posición inicial

    time.sleep(0.05)  # Pequeño delay para evitar saturar el sistema
