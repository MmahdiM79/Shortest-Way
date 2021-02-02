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

    
    def add_e(self, v: Vertice, u: Vertice, weight: float) -> None:

        if not self.has_e(v, u):

            if weight == -1:
                weight = self.__weight(v, u, 0);

            self.__e[(v.v_id(), u.v_id())] = weight
            self.__e[(u.v_id(), v.v_id())] = weight
            self.__adj[v.v_id()].append((u.v_id(), weight))
            self.__adj[u.v_id()].append((v.v_id(), weight))

            self.__traffic[(v.v_id(), u.v_id())] = []
            self.__traffic[(u.v_id(), v.v_id())] = []



    def has_e(self, v: Vertice, u: Vertice) -> bool:
        return ((v.v_id(), u.v_id()) in self.__e.keys())


    def set_e_weight(self, v: Vertice, u: Vertice, weight: float) -> None:

        if self.has_e(v, u):
            self.__e[(v.v_id(), u.v_id())] = weight
            self.__e[(u.v_id(), v.v_id())] = weight

            for neighbor in self.__adj[v.v_id()]:
                if neighbor[0] == u.v_id():
                    if neighbor[1] != weight:
                        self.__adj[v.v_id()].remove(neighbor)
                        self.__adj[v.v_id()].append((u.v_id(), weight))
                    break

            for neighbor in self.__adj[u.v_id()]:
                if neighbor[0] == v.v_id():
                    if neighbor[1] != weight:
                        self.__adj[u.v_id()].remove(neighbor)
                        self.__adj[u.v_id()].append((v.v_id(), weight))
                    break


    def e_weight(self, v: Vertice, u: Vertice) -> float:
        if not self.has_e(v, u):
            return -1
        
        for edge in self.__adj[v.v_id()]:
            if edge[0] == u.v_id():
                return edge[1]


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
                    traffic += 1

            v = self.__v[edge[0]]
            u = self.__v[edge[1]]
            self.set_e_weight(v, u, self.__weight(v, u, traffic))
            traffic = 0


        explored = []
        while not destination.v_id() in explored:
            v = unexplored.pop_min()
            explored.append(v.v_id())
            for edge in self.__adj[v.v_id()]:
                if v.distance() + edge[1] < self.__v[edge[0]].distance():
                    unexplored.update(edge[0], v.distance() + edge[1])
                    self.__v[edge[0]].set_distance(v.distance() + edge[1])
                    self.__v[edge[0]].set_parrent(v)



        finded_path = [] 
        curr = destination
        travel_time = 0

        while curr is not start:
            finded_path.append(curr.v_id())
            travel_time += self.e_weight(curr, curr.parrent())
            curr = curr.parrent()
        
        travel_time *= 120

        finded_path.append(curr.v_id())
        for i in range(len(finded_path)-1):
            self.__traffic[(finded_path[i], finded_path[i+1])].append(travel_time)
            self.__traffic[(finded_path[i+1], finded_path[i])].append(travel_time)
        finded_path.append(travel_time)

        return tuple(reversed(finded_path))





    def __weight(self, v: Vertice, u: Vertice, traffic: int) -> float:

        length = ((v.x() - u.x())**2 + (v.y() - u.y())**2)**(0.5)

        return length * (1 + 0.3*traffic)
