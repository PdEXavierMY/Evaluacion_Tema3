import hashlib

class Encripta():
    def _init_(self, mensaje):
        self.mensaje = mensaje.split(' ')
        self.mensaje_encriptado = []
    def encriptar(self):
        for palabra in self.mensaje:
            self.mensaje_encriptado.append(hashlib.sha256(str(palabra).encode('utf-8')).hexdigest())
        with open('mensaje_encriptado.txt', 'w') as archivo:
            archivo.write(' '.join(self.mensaje_encriptado))
        return self.mensaje_encriptado