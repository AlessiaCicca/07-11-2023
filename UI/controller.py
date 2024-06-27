import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        anno = self._view.dd_anno.value
        if anno is None:
            self._view.create_alert("Selezionare un Anno")
            return
        grafo = self._model.creaGrafo(int(anno))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        self._view.update_page()


    def handle_dettagli(self, e):
        squadra = self._view.dd_squadra.value
        if squadra is None:
            self._view.create_alert("Selezionare una squadra")
            return
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti per la squadra {squadra}"))
        dizionario = self._model.analisi(squadra)
        for (nodo, peso) in dizionario:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}         {peso}"))
        self._view.update_page()

    def fillDD(self):
        anni=self._model.anni
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(
                text=anno))

    def getSquadre(self,e):
        anno = int(self._view.dd_anno.value)
        squadre=self._model.getSquadre(anno)
        self._view.txt_result.controls.append(ft.Text(f"Squadre presenti nell'anno {anno}= {len(squadre)}"))
        for squadra in squadre:
            self._view.txt_result.controls.append(ft.Text(f"{squadra}"))
            self._view.dd_squadra.options.append(ft.dropdown.Option(
                text=squadra))
        self._view.update_page()


