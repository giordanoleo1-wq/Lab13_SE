import networkx as nx
from model.gene import Gene
from model.interazione import Interazione
from model.classificazione import Classificazione
from database.dao import DAO


class Model:
    def __init__(self):
        self.lista_interazione = []
        self.G = nx.DiGraph()
        self.lista_geni= []
        self.id_gene= {}
        self.id_interazione= {}
        #self.id_classificazione= {}


    def crea_grafo(self):
        self.G = nx.DiGraph()
        for g in self.lista_geni:
            if g.cromosoma!=0:
                self.G.add_node(g)


        for i in self.lista_interazione:
            g1= i.id_gene1
            g2= i.id_gene2

            gene1= self.id_gene[g1]
            gene2= self.id_gene[g2]

            geni_chiave= gene1, gene2
            lista_geni_chiave= sorted(list(geni_chiave))
            lista_geni_chiave_sd= set(lista_geni_chiave)
            lista_geni_chiave_fine= list(lista_geni_chiave_sd)

            self.id_interazione[lista_geni_chiave_fine]= i
            if lista_geni_chiave in self.id_interazione.keys():
                peso += i.correlazione
            else:
                peso= i.correlazione


            self.G.add_edge(gene1, gene2, weight= peso)
            print(self.G)

    def calcola_minimo_massimo(self):
        print(self.G.edges)
        lista_pesi=[]
        for e in self.G.edges:
            p= self.G[e[0]][e[1]]['weight']
            lista_pesi.append(p)
        return min(lista_pesi), max(lista_pesi)

    def calcola_numero_archi_soglia(self, soglia):
        lista_maggiori=[]
        lista_minori=[]
        for e in self.G.edges:
            if self.G[e[0]][e[1]]['weight']>soglia:
                lista_maggiori.append(e)
            elif self.G[e[0]][e[1]]['weight']<soglia:
                lista_minori.append(e)
        return lista_minori, lista_maggiori















    def load_gene(self):
        self.lista_geni= DAO.read_all_gene()


    def load_interazione(self):
        self.lista_interazione= DAO.read_all_interazione()




