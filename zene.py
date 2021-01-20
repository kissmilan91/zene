from typing import List


class zene(object):
    sorszam: int
    eloado: str
    cim: str
    hossz: float
    kiadas_eve: int
    kategoria: str

    def __init__(self, sor: str) -> None:
        z: List[str] = sor.split(';')
        self.sorszam = int(z[0])
        self.eloado = z[1]
        self.cim = z[2]
        self.hossz = float(z[3])
        self.kiadas_eve = int(z[4])
        self.kategoria = z[5]
