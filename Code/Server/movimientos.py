import time
from Control import Control
from enum import Enum
import numpy as np

class Command(Enum):
    MOVE = 'CMD_MOVE'
    POSITION = 'CMD_POSITION'
    POSTURA = 'CMD_ATTITUDE'
    RELAX = 'CMD_RELAX'

class GaitMode(Enum):
    MODE_1 = '1'
    MODE_2 = '2'

class bailes:
    def __init__(self):
        self.ctrl = Control()
        self.data = [] 
    
    def altura(self):
        self.ctrl.posittion(0, 0, 40)
    
    def move(self, x: str = '0', y: str = '0', speed: str = '0', angle: str = '0'):
        data = [
            Command.MOVE.value,
            GaitMode.MODE_1.value,
            x, y, speed, angle
        ]
        self.ctrl.run(data)

    # **NUEVOS MÉTODOS PARA MOVIMIENTOS BÁSICOS SEGÚN LAS FLECHAS**
    
    def avanzar(self):
        """Movimiento hacia adelante"""
        steps = 3
        dx, dy, speed, angle = "0", "30", "15", "0"
        for _ in range(steps):
            self.move(dx, dy, speed, angle)

    def retroceder(self):
        """Movimiento hacia atrás"""
        steps = 3
        dx, dy, speed, angle = "0", "-30", "15", "0"
        for _ in range(steps):
            self.move(dx, dy, speed, angle)

    def mover_izquierda(self):
        """Movimiento lateral hacia la izquierda"""
        steps = 3
        dx, dy, speed, angle = "-30", "0", "15", "0"
        for _ in range(steps):
            self.move(dx, dy, speed, angle)

    def mover_derecha(self):
        """Movimiento lateral hacia la derecha"""
        steps = 3
        dx, dy, speed, angle = "30", "0", "15", "0"
        for _ in range(steps):
            self.move(dx, dy, speed, angle)
