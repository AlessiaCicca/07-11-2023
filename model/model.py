import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.anni=DAO.getAnni()
        self.grafo = nx.Graph()
        self._idMap = {}
    def getSquadre(self,anno):
        return DAO.getSquadre(anno)

    def creaGrafo(self,anno):
        self.nodi = DAO.getNodi(anno)
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[f"{v.teamCode} ({v.name})"] = v
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                    self.grafo.add_edge(nodo1, nodo2, weight=abs(nodo1.salario+nodo2.salario))

    def analisi(self,squadrastr):
        squadra=self._idMap[squadrastr]
        dizio={}
        for nodo in self.grafo.neighbors(squadra):
            dizio[f"{nodo}"]=self.grafo[nodo][squadra]["weight"]
        dizioOrder=sorted(dizio.items(),key=lambda item:item[1],reverse=True)
        return dizioOrder