class InstrumentoMusical ():
    def tocar (self): 
        return "El intrumento toca musica de manera natral"
    
class Guitarra (InstrumentoMusical):
    
    def tocar (self):
        return "La guitarra toca con un timbre fuerte"

class Piano (InstrumentoMusical):
    
    def tocar (self):
        return "El piano toca con un ritmo de jazz"

instrumento = InstrumentoMusical ()
print(instrumento.tocar())

guitarra = Guitarra()
print(guitarra.tocar())

piano = Piano ()
print(piano.tocar())