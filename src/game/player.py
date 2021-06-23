

class Player:

    score = 0
    def __init__(self, nombre, id) -> None:
        """
        Contructor.
        IMPORTANT: Todo metodo lleva como primer
        parametro self
        """
        self.nombre = nombre
        self.id = id
    

    def __str__(self) -> str:
        """
        Convierto a String my metodo
        """
        return f"Player name:{self.nombre}, id:{self.id}, score: {self.score}"