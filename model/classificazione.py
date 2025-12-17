from dataclasses import dataclass
@dataclass
class Classificazione():
    id_gene : str
    localizzazione : str


    def __str__(self):
        return self.id_gene

    def __hash__(self):
        return hash(self.id_gene)