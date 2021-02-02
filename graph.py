from min_heap import MinHeap, Vertice



class Graph(object):


    def __init__(self) -> None:
        self.__v = {}
        self.__e = {}
        self.__adj = {}
        self.__traffic = {}



    def add_v(self, v: Vertice) -> None:
        if not v in self.__v:
            self.__v[v.v_id()] = v
            self.__adj[v.v_id()] = []

    
    def add_e(self, v: Vertice, u: Vertice, wight: float) -> None:

        if not self.has_e(v, u):

            if wight == -1:
                wight = self.__weight(v, u, 0);

            self.__e[(v.v_id(), u.v_id())] = wight
            self.__e[(u.v_id(), v.v_id())] = wight
            self.__adj[v.v_id()].append((u.v_id(), wight))
            self.__adj[u.v_id()].append((v.v_id(), wight))

            self.__traffic[(v.v_id(), u.v_id())] = []
            self.__traffic[(u.v_id(), v.v_id())] = []



    def has_e(self, v: Vertice, u: Vertice) -> bool:
        return ((v.v_id(), u.v_id()) in self.__e.keys())


    def set_e_wight(self, v: Vertice, u: Vertice, wight: float) -> None:

        if self.has_e(v, u):
            self.__e[(v.v_id(), u.v_id())] = wight
            self.__e[(u.v_id(), v.v_id())] = wight

            for neighbor in self.__adj[v.v_id()]:
                if neighbor[0] == u.v_id():
                    if neighbor[1] != wight:
                        self.__adj[v.v_id()].remove(neighbor)
                        self.__adj[v.v_id()].append((u.v_id(), wight))
                    break

            for neighbor in self.__adj[u.v_id()]:
                if neighbor[0] == v.v_id():
                    if neighbor[1] != wight:
                        self.__adj[u.v_id()].remove(neighbor)
                        self.__adj[u.v_id()].append((v.v_id(), wight))
                    break


    def e_wight(self, v: Vertice, u: Vertice) -> float:
        if not self.has_e(v, u):
            return -1
        return self.__adj[v.v_id()]


    def shortest_path(self, start: Vertice, destination: Vertice, time: float) -> tuple:
        for v in self.__v.values():
            v.set_distance(-1)
            v.set_parrent(None)

        
        unexplored = MinHeap(len(self.__v))
        for v in self.__v.values():
            unexplored.insert(v)
        unexplored.update(start.v_id(), 0)
        self.__v[start.v_id()].set_distance(0)


        traffic = 0
        for edge in self.__traffic.keys():
            for t in self.__traffic[edge]:
                if time <= t:
                    traffic += 0.5

            v = self.__v[start.v_id()]
            u = self.__v[destination.v_id()]
            self.set_e_wight(v, u, self.__weight(v, u, traffic))


        explored = []
        while not destination.v_id() in explored:
            v = unexplored.pop_min()
            explored.append(v.v_id())
            for edge in self.__adj[v.v_id()]:
                if v.distance() + edge[1] < self.__v[edge[0]].distance():
                    unexplored.update(edge[0], v.distance() + edge[1])
                    self.__v[edge[0]].set_distance(v.distance() + edge[1])
                    self.__v[edge[0]].set_parrent(v)


        finded_path = []; curr = destination
        while curr is not start:
            finded_path.append(curr.v_id())
            curr = curr.parrent()
        finded_path.append(curr.v_id())

        return tuple(reversed(finded_path))





    def __weight(self, v: Vertice, u: Vertice, traffic: int) -> float:

        length = ((v.x() - u.x())**2 + (v.y() - u.y())**2)**(0.5)

        return length * (1 + 0.3*traffic)
