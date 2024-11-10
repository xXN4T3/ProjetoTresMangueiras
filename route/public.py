from datetime import datetime
from fastapi import APIRouter, Body, Header
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from db import Database
import funcoes as fn
import json
from models.person import GetDoacao, SetDoacao
from funcoes import errorFunction


class Public():
    def __init__(self) -> None:

        self.dictErrorResponse = {
            200: {"mensagem": "Sucesso!"},
            400: {"mensagem": "Erro na requisição!"},
            401: {"mensagem": "Não autorizado!"},
            403: {"mensagem": "Não autenticado!"},
            404: {"mensagem": "Não encontrado!"}
        }

        self.doacao_router = APIRouter(prefix='/public', tags=['Doacao'])

        self.doacao_router.add_api_route('/doacao',
                                         self.get_person,
                                         methods=['GET'],
                                         response_model=GetDoacao,
                                         responses=self.dictErrorResponse)

        self.doacao_router.add_api_route('/doacao',
                                         self.post_person,
                                         methods=['POST'],
                                         response_model=SetDoacao,
                                         responses=self.dictErrorResponse)

        self.doacao_router.add_api_route('/doacao',
                                         self.update_person,
                                         methods=['PUT'],
                                         responses=self.dictErrorResponse)

        self.doacao_router.add_api_route('/doacao',
                                         self.delete_person,
                                         methods=['DELETE'],
                                         responses=self.dictErrorResponse)

    async def get_person(self):
        try:
            with Database() as db:
                sql = """SELECT * FROM doacao"""

                result = db.query(sql)

                if len(result) == 0:
                    raise HTTPException(status_code=404)

                data_float = [
                    [item if isinstance(item, (int, str))
                     else float(item) for item in row]
                    for row in result
                ]

                return JSONResponse(content=json.dumps(data_float), status_code=200)
        except Exception as E:
            errorFunction(self, E)

    async def post_person(self, doacao: SetDoacao = Body(...)):
        try:
            with Database() as db:
                sql = """INSERT INTO doacao (nome, email, telefone, valor) VALUES (%s, %s, %s, %s)"""
                db.execute(sql, (doacao.nome, doacao.email,
                           doacao.telefone, doacao.valor))
                db.commit()
                return JSONResponse(content=json.dumps({"mensagem": "Sucesso!"}), status_code=200)
        except Exception as E:
            errorFunction(self, E)

    async def update_person(self):
        pass

    async def delete_person(self):
        pass
