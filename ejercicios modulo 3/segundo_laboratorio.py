#Trabajo realizado por jhonattan florez y deivid bautista

#Ficha: 2470031

#Tu tarea es extender ligeramente las capacidades de la 
#clase Queue. Queremos que tenga un método sin parámetros
#que devuelva True si la cola está vacía y False de lo contrario.


class QueueError(IndexError):
    pass
class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

class MQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0


valor = MQueue()
valor.put(7)
valor.put("vaca")
valor.put(True)
for i in range(4):
    if not valor.isempty():
        print(valor.get())
    else:
        print("Vacio")