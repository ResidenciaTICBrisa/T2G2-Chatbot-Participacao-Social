class StateMachine:
    def __init__(self, user_id):
        # atributos privados
        self.__state = -2
        self.__id = user_id

    def getstate(self): return self.__state

    def setstate(self, new_state):
        self.__state = new_state

    def get_id(self): return self

    # a princípio não deve-se mudar o id uma vez que ele já foi definido

