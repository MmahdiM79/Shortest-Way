from Graph import Vertice





class MinHeap(object):


    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__size = -1
        self.__indexes_hash = {}
        self.__vertices = [None for _ in range(capacity)]
        


    def insert(self, v: Vertice) -> None:

        if self.__size+1 >= self.__capacity:
            return

        self.__size += 1
        self.__vertices[self.__size] = v
        self.__indexes_hash[v.v_id()] = self.__size
        self.__pull_up(self.__size)



    def pop_min(self) -> Vertice:
        out = self.__vertices[0]
        last = self.__vertices[self.__size]
        self.__vertices[0] = last
        self.__vertices[self.__size] = None
        self.__indexes_hash[last.v_id()] = 0
        self.__size -= 1
        self.__max_heapify(0)

        return out



    def update(self, v_id: str, distance: float) -> None:
        
        if not v_id in self.__indexes_hash.keys():
            return

        index = self.__indexes_hash[v_id]
        self.__vertices[index].set_distance(distance)
        self.__pull_up(index)
        





    
    def __max_heapify(self, index: int) -> None:

        curr = index
        left = 2 * curr + 1
        right = left + 1

        if left <= self.__size and self.__vertices[curr].distance() > self.__vertices[left].distance():
            curr = left
        if right <= self.__size and self.__vertices[curr].distance() > self.__vertices[right].distance():
            curr = right

        if curr != index:
            self.__indexes_hash[self.__vertices[curr].v_id()] = index
            self.__indexes_hash[self.__vertices[index].v_id()] = curr
            self.__swap(index, curr)
            self.__max_heapify(curr)



    def __swap(self, cur: int, par: int) -> None:
        self.__vertices[cur], self.__vertices[par] = self.__vertices[par], self.__vertices[cur]



    def __pull_up(self, index: int) -> None:

        par = index//2
        cur = index

        while self.__vertices[par].distance() > self.__vertices[cur].distance():
            self.__indexes_hash[self.__vertices[cur].v_id()] = par
            self.__indexes_hash[self.__vertices[par].v_id()] = cur
            self.__swap(cur, par)
            cur = par
            par //= 2


    def __len__(self) -> int:
        return self.__size+1


