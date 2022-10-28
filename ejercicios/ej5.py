import hashlib

class Encripta():
    def __init__(self, mensaje):
        self.mensaje = mensaje.split(' ')
        self.mensaje_encriptado = []
    def encriptar(self):
        for palabra in self.mensaje:
            self.mensaje_encriptado.append(hashlib.sha256(str(palabra).encode('utf-8')).hexdigest())
        return ' '.join(self.mensaje_encriptado)