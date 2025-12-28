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

        self._view.btn_conta_edges.disabled = False
        self._view.btn_ricerca.disabled = False
        self._view.page.update()


    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO

        try:
            soglia = float(self._view.txt_name.value)
            if soglia<3 or soglia>7:
                self._view.show_alert("Il valore della soglia deve essere compreso tra 3 e 7")
                return
        except Exception:
            self._view.show_alert("Inserire un valore valido per la soglia")
            return

        self._view.lista_visualizzazione_2.clean()
        inf, sup= self._model.calcola_numero_archi_soglia(soglia)
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {sup}\n"
                                                                   f"Numero archi con peso minore della soglia : {inf} "))
        self._view.page.update()




    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO

        try:
            soglia = float(self._view.txt_name.value)
        except Exception:
            #self._view.show_alert("Inserire un valore valido per la soglia")
            return

        percorso_ottimo, costo_massimo= self._model.get_peso_massimo(soglia)

        self._view.lista_visualizzazione_3.clean()

        self._view.lista_visualizzazione_3.controls.append(
            ft.Text(f"Numero archi percorso più lungo: {len(percorso_ottimo) - 1}\n"
                    f"Peso cammino massimo {costo_massimo}\n"))

        for i in range(len(percorso_ottimo)-1):
            c1 = percorso_ottimo[i]
            c2 = percorso_ottimo[i+1]
            peso= self._model.G[c1][c2]['weight']

            self._view.lista_visualizzazione_3.controls.append(
            ft.Text(f"{c1} --> {c2}: {peso} "))

        self._view.page.update()