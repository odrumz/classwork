class Graph:
    def __init__(self,directed = False):
        self.directed = directed

        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""

        for node, neighbours in self.adj_list.items():
            graph_string += f"{node}=>{neighbours}"

        return graph_string
    def add_node(self,node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node Already Exists")

    def add_edge(self,from_node,to_node,weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add(to_node,weight)

            if not self.directed:
                self.adj_list[to_node].add(from_node,weight)
    def bfs(self,start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in  visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for n in neighbours:
                    if isinstance(n,tuple):
                        n = n[0]
                    if n not in visited:
                        queue.append(n)
        return order

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for n in sorted(neighbours,reverse=True):
                    if isinstance(n, tuple):
                        n = n[0]
                    if n not in visited:
                        stack.append(n)
        return  order
    def obtain_neighbours(self,node):
        return self.adj_list.get(node,set())

if __name__ == '__main__':
    graph_obj = Graph(directed=True)
    graph_obj.add_edge("A","B",2)
    graph_obj.add_edge("A","J",2)
    graph_obj.add_edge("A","C",2)
    graph_obj.add_edge("B","D",2)
    graph_obj.add_edge("D","C",2)

    print(graph_obj)
    print("BFs")
    print("DFs")
    print(graph_obj).bfs("A")
    print(graph_obj).dfs("A")
