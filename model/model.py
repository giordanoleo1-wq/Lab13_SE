import copy

import networkx as nx
from model.gene import Gene
from model.interazione import Interazione
from model.classificazione import Classificazione
from database.dao import DAO


class Model:
    def __init__(self):
        self.percorso_ottimale = []
        self.costo_massimo= 0
        self.lista_interazione = []
        self.G = nx.DiGraph()
        self.dic_geni= {}




    def load_gene(self):
        self.dic_geni= DAO.read_all_gene()


    def load_interazione(self):
        self.lista_interazione= DAO.read_all_interazione()


    def crea_grafo(self):
        self.G = nx.DiGraph()
        self.load_gene()
        self.load_interazione()

        cromosomi= set()
        coppie_geni_viste= set()
        pesi= {}
        for g in self.dic_geni.values():
            if g.cromosoma!=0:
                cromosomi.add(g.cromosoma)
        for c in cromosomi:
            self.G.add_node(c)


        for i in self.lista_interazione:
            g1= i.id_gene1
            g2= i.id_gene2

            if g1 not in self.dic_geni or g2 not in self.dic_geni:
                continue

            gene1= self.dic_geni[g1]
            gene2= self.dic_geni[g2]

            c1= gene1.cromosoma
            c2= gene2.cromosoma


            if c1==0 or c2==0 or c1==c2:
                continue


            key = tuple(sorted([g1, g2]))
            key_visti= (c1, c2, key)
            if key_visti in coppie_geni_viste:
                continue
            coppie_geni_viste.add(key_visti)

            key_cromosomi= (c1, c2)

            pesi[key_cromosomi]= pesi.get(key_cromosomi, 0) + i.correlazione
            #SCRITTURA CORRISPONDENTE
            #if key_cromosomi in pesi:
                #pesi[key_cromosomi] = pesi[key_cromosomi] + valore
            #else:
                #pesi[key_cromosomi] = valore

        for (c1, c2), peso in pesi.items():
            self.G.add_edge(c1, c2, weight=peso)



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
            if self.G[e[0]][e[1]]['weight'] > soglia:
                lista_maggiori.append(e)
            elif self.G[e[0]][e[1]]['weight'] < soglia:
                lista_minori.append(e)
        return len(lista_minori), len(lista_maggiori)

    def get_peso_massimo(self, soglia):
        self.percorso_ottimale=[]
        self.costo_massimo= 0

        for n in self.G.nodes:
            archi_usati = set()
            self._ricorsione(n,[n], 0, soglia, archi_usati )
        return self.percorso_ottimale, self.costo_massimo


    def _ricorsione(self, cromosoma ,sequenza_parziale, costo_parziale, soglia, archi_usati):
        if costo_parziale> self.costo_massimo:
            self.costo_massimo= costo_parziale
            self.percorso_ottimale= list(sequenza_parziale)

        for vicino in self.G.neighbors(cromosoma):
            peso= self.G[cromosoma][vicino]['weight']
            arco= (cromosoma, vicino)

            if peso > soglia and arco not in archi_usati:
                sequenza_parziale.append(vicino)
                archi_usati.add(arco)

                self._ricorsione(vicino, sequenza_parziale, costo_parziale + peso, soglia, archi_usati)

                archi_usati.remove(arco)
                sequenza_parziale.pop()



















