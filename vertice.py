



class Vertice(object):


    def __init__(self, x: int, y: int, v_id: str) -> None:
        self.__x = x
        self.__y = y
        self.__v_id = v_id
        self.__distance = sys.maxsize
        self.__p = None



    def x(self) -> int:
        return self.__x

    def y(self) -> int:
        return self.__y

    def v_id(self) -> str:
        return self.__v_id

    def set_distance(self, distance: float) -> None:
        self.__distance = distance

    def distance(self) -> int:
        return self.__distance

    def set_parrent(self, parrent) -> None:
        self.__p = parrent

    def parrent(self):
        return self.__p