import threading
import time
import random
import queue

barberos = 1
clientes = 5
asientos = 3
esperas = 1

def espera():
    time.sleep(esperas * random.random())

class barbero(threading.Thread):
    condicion = threading.Condition()
    alto_completo = threading.Event()

    def __init__(self, ID):
        super().__init__()
        self.ID = ID

    def run(self):
        while True:
            try:
                cliente_actual = sala_espera.get(block=False)
            except queue.Empty:
                if self.alto_completo.is_set():
                    return
                print ("BIENVENIDOS A NUESTRA BARBERIA JENNYFER")
                print ("Colocarse su marcarilla y gel antes de ingresar")
                print ("En 5 momentos iniciamos")

                print("el barbero esta tomando una ciesta de 20 minutos mMMmMmzzZzZzZMzmMZMZm")
                print ("se desperto el barbero y se da cuenta que solo son niños los que atendera ahora")
                with self.condicion:
                    self.condicion.wait()
            else:
                cliente_actual.cortar(self.ID)

class cliente(threading.Thread):
    duracion_corte = 5

    def __init__(self, ID):
        super().__init__()
        self.ID = ID

    def corte(self):
        time.sleep(self.duracion_corte * random.random())

    def cortar(self, id_barbero):
        print(f"el barbero {id_barbero} esta cortando el cabello del cliente del cual es un niño  {self.ID}")
        self.corte()
        print(f"el barbero {id_barbero} termino de cortar el cabello al cliente {self.ID}")
        self.atendido.set()
        
    def run(self):
        self.atendido = threading.Event()

        try:
            sala_espera.put(self, block=False)
        except queue.Full:
            print(f"Nuestras sala de espera esta llena, {self.ID} se fue...... regreso al rato.")
            return

        print(f"el cliente {self.ID} se sento en la sala de espera.")
        with barbero.condicion:
            barbero.condicion.notify(1)

        self.atendido.wait()

if __name__ == "__main__":
    todos_clientes = []
    sala_espera = queue.Queue(asientos)

    for i in range(barberos):
        hilo_barbero = barbero(1)
        hilo_barbero.start()

    for i in range(clientes):
        espera()
        clientes = cliente(i)
        todos_clientes.append(cliente)
        clientes.start()

    for cliente in todos_clientes:
        clientes.join()

    time.sleep(0.1)
    barbero.alto_completo.set()
    with barbero.condicion:
        barbero.condicion.notify_all()

        print ("La barberia esta cerrada")
        print ("comenta el barbero largo dia")
        print ("todos mis clientes satisfechos")
        print ("volvemos a tomar una segunda ciesta si que siiiiiii")
