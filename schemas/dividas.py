from pydantic import BaseModel
from typing import Optional, List
from model.divida import Divida
from datetime import datetime

class DividaSchema(BaseModel):
    """ Define como uma nova dívida a ser inserida deve ser representada
    """
    descricao: str = "Compra de carro Placa AXY1234"
    valorInicial: float = 100.00
    valorFinal: float = 125.10
    data: datetime = datetime.now()

class DividaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base nos dados da divida.
    """
    descricao: str = "Compra de carro Placa AXY1234"

class ListagemDividasSchema(BaseModel):
    """ Define como uma listagem de dividas será retornada.
    """
    dividas:List[DividaSchema]

def apresenta_dividas(dividas: List[Divida]):
    """ Retorna uma representação da divida seguindo o schema definido em
        DividaViewSchema.
    """
    result = []
    for divida in dividas:
        result.append({
            "id": divida.id,
            "descricao": divida.descricao,
            "valorInicial": divida.valorInicial,
            "valorFinal": divida.valorFinal,
            "data": divida.data,
        })

    return {"dividas": result}

class DividaViewSchema(BaseModel):
    """ Define como uma divida será retornada: 
    """
    id: int = 1
    descricao: str = "Compra de carro Placa AXY1234"
    valorInicial: float = 100.00
    valorFinal: float = 125.10
    data: datetime = datetime.now()

class DividaDelSchema(BaseModel):
    """ Define a estrutura a ser retornada após a deleção de uma divida.
    """
    message: str

def apresenta_divida(divida: Divida):
    """ Retorna uma representação da divida seguindo o schema definido em
        DividaViewSchema.
    """
    return {
        "id": divida.id,
        "descricao": divida.descricao,
        "valorInicial": divida.valorInicial,
        "valorFinal": divida.valorFinal,
        "data": divida.data
    }