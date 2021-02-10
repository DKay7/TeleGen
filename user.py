from enum import Enum, auto


class States(Enum):
    INIT = auto()
    REQUESTING = auto()
    RESPONDED = auto()


class User:
    def __init__(self, id_):
        self.id = id_
        self.state = States.INIT

    def change_state(self, new_state):
        self.state = States[new_state]
