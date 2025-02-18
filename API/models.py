from pydantic import BaseModel
from datetime import date

class Ingreso(BaseModel):
    id: int
    titol: str
    descripcio: str
    quantitat: float
    data: date

class Despesa(BaseModel):
    id: int
    titol: str
    descripcio: str
    quantitat: float
    data: date
