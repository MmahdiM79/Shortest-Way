from graph import Graph, Vertice





if __name__ == "__main__":


    with open('./m1.txt', 'r') as file:
        map_details = file.read().split()

        number_of_vertices = int(map_details[0])
        number_of_edges = int(map_details[1])


        g = Graph(); vertices = {}; edges = {}

        for i in range(2, number_of_vertices*3, 3):
            vertices[map_details[i]] = Vertice(float(map_details[i+2]), float(map_details[i+1]), map_details[i])
            g.add_v(vertices[map_details[i]])
        
        for j in range((3*number_of_vertices + 2), number_of_edges*2, 2):
            edges[(map_details[j], map_details[j+1])] = -1
            edges[(map_details[j+1], map_details[j])] = -1
            g.add_e(vertices[map_details[j]], map_details[j+1], -1)






