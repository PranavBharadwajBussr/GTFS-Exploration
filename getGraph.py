import random

def getStop(s):
    stops = open('stops.txt', 'r')
    stop0 = stops.readline()
    stop = stops.readline()
    while (stop != None):
        if (int(stop.split(',')[0]) == s):
            return stop.split(',')[1]
        stop = stops.readline()
    return None

class Graph:
    def __init__(self):
        self.graph = []
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def printGraph(self):
        for i in range(len(self.graph)):
            print(self.graph[i])
    def printMST(self, mst):
        print("Edge \tWeight")
        for i in range(len(mst)):
            print(getStop(mst[i][0]), " -> ", getStop(mst[i][1]), ",", str(mst[i][2]))
    def kruskalMST(self):
        visited = []
        mst = []
        self.graph = sorted(self.graph, key = lambda x: x[2])
        for g in self.graph:
            if g[0] not in visited and g[1] not in visited:
                visited.append(g[0])
                visited.append(g[1])
                mst.append(g)
            elif g[0] in visited and g[1] not in visited:
                visited.append(g[1])
                mst.append(g)
            elif g[0] not in visited and g[1] in visited:
                visited.append(g[0])
                mst.append(g)
            else:
                continue
        self.printMST(mst)

graph = Graph()
gtfs = open('stop_times.txt', 'r')
node0 = gtfs.readline()
node = gtfs.readline()
u = int(node.split(',')[3])
W = [1,2,3,4,5,6,7,8,9,10]
while (node != None):
    node = gtfs.readline()
    if(not node):
        break
    v = int(node.split(',')[3])
    w = random.choice(W)
    graph.addEdge(u,v,w)
    # print(getStop(u)+" -> "+getStop(v))
    u = v
graph.kruskalMST()