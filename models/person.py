from typing import Union, List
from pydantic import Field, BaseModel
from datetime import datetime


class GetDoacao(BaseModel):
    class Doacao(BaseModel):
        id: int = Field(default=-1)
        nome: str = Field(default="")
        email: str = Field(default="")
        telefone: str = Field(default="")
        valor: int = Field(default=1)
    person: List[Doacao] = [Doacao()]


class SetDoacao(BaseModel):
    id: int = Field(default=-1)
    nome: str = Field(default="")
    email: str = Field(default="")
    telefone: str = Field(default="")
    valor: int = Field(default=1)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nome": "",
                "email": "",
                "telefone": "21995430832",
                "valor": 0.00
            }
        }
