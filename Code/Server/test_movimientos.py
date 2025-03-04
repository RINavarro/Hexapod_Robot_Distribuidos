import time
from movimientos import bailes  # Importamos la clase bailes desde el archivo donde la guardaste

def main():
    robot = bailes()  # Creamos una instancia del robot
    
    print("Prueba de movimientos básicos del hexápodo:")
    
    while True:
        print("\nOpciones:")
        print("W - Avanzar")
        print("S - Retroceder")
        print("A - Mover Izquierda")
        print("D - Mover Derecha")
        print("Q - Salir")
        
        comando = input("Ingrese un comando: ").strip().upper()

        if comando == "W":
            print("Moviendo hacia adelante...")
            robot.avanzar()
        elif comando == "S":
            print("Moviendo hacia atrás...")
            robot.retroceder()
        elif comando == "A":
            print("Moviendo hacia la izquierda...")
            robot.mover_izquierda()
        elif comando == "D":
            print("Moviendo hacia la derecha...")
            robot.mover_derecha()
        elif comando == "Q":
            print("Saliendo del test.")
            break
        else:
            print("Comando no reconocido, intenta de nuevo.")

        time.sleep(1)  # Pequeña pausa entre movimientos para evitar sobrecargar los motores

if __name__ == "__main__":
    main()
