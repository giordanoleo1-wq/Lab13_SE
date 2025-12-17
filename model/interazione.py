from dataclasses import dataclass
@dataclass
class Interazione:
    id_gene1: str
    id_gene2: str
    tipo: str
    correlazione: float


    def __str__(self):
        return f"{self.id_gene1} {self.tipo} {self.id_gene2}"
    def __hash__(self):
        return hash(self.id_gene1)

