import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._model.crea_grafo()
        self._view.lista_visualizzazione_1.clean()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo calcolatao : {self._model.G.number_of_nodes()} nodi, {self._model.G.number_of_edges()} archi"))

        min_p, max_p= self._model.calcola_minimo_massimo()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Massimo peso: {max_p}, minimo : {min_p}"))


        self._view.page.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO


    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO