import sys
import MinHeap




class Vertice(object):


    def __init__(self, x: int, y: int, v_id: str) -> None:
        self.__x = x
        self.__y = y
        self.__v_id = v_id
        self.__distance = sys.maxsize



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







class Graph(object):


    def __init__(self) -> None:
        self.__v = []
        self.__e = {}
        self.__adj = {}



    def add_v(self, v: Vertice) -> None:
        if not v in self.__v:
            self.__v.append(Vertice)
            self.__adj[v.v_id()] = []

    
    def add_e(self, v: Vertice, u: Vertice, wight: float) -> None:
        if not (v.v_id(), u.v_id()) in  self.__e.keys():
            self.__e[(v.v_id, u.v_id)] = wight
            self.__e[(u.v_id, v.v_id)] = wight
            self.__adj[v.v_id()] = (u.v_id(), wight)
            self.__adj[u.v_id()] = (v.v_id(), wight)


    def has_e(self, v: Vertice, u: Vertice) -> bool:
        return ((v.v_id(), u.v_id()) in self.__e.keys())


    def e_wight(self, v: Vertice, u: Vertice) -> float:
        if not self.has_e(v, u):
            return -1
        return self.__adj[v.v_id()]


    
