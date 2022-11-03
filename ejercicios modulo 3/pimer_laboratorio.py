#Trabajo realizado por jhonattan florez y deivid bautista

#Ficha: 2470031

#Tu tarea es extender el comportamiento de la clase Stack
#de tal manera que la clase pueda contar todos los elementos
#que son agregados (push) y quitados (pop).
#Emplea la clase Stack que proporcionamos en el editor.

class Stack:
    def __init__(self):
        self.__stk = []
    def push(self, val):
        self.__stk.append(val)
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val
class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0
    def get_counter(self):
        return self.__counter
    def pop(self):
        self.__counter = self.__counter + 1
        return Stack.pop(self)
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())