from pydantic import BaseModel
from typing import Optional, List
from model.receita import Receita
from datetime import datetime

class ReceitaSchema(BaseModel):
    """ Define como uma nova receita a ser inserida deve ser representada
    """
    descricao: str = "Salário Anual"
    valorBruto: float = 100.00
    valorLiquido: float = 125.10
    data: datetime = datetime.now()

class ReceitaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base nos dados da receita.
    """
    descricao: str = "Salário Anual"

class ListagemReceitasSchema(BaseModel):
    """ Define como uma listagem de receitas será retornada.
    """
    receitas:List[ReceitaSchema]

def apresenta_receitas(receitas: List[Receita]):
    """ Retorna uma representação da receita seguindo o schema definido em
        ReceitaViewSchema.
    """
    result = []
    for receita in receitas:
        result.append({
            "id": receita.id,
            "descricao": receita.descricao,
            "valorInicial": receita.valorBruto,
            "valorFinal": receita.valorLiquido,
            "data": receita.data,
        })

    return {"receitas": result}

class ReceitaViewSchema(BaseModel):
    """ Define como uma receita será retornada: 
    """
    id: int = 1
    descricao: str = "Salário Anual"
    valorBruto: float = 100.00
    valorLiquido: float = 125.10
    data: datetime = datetime.now()

class ReceitaDelSchema(BaseModel):
    """ Define a estrutura a ser retornada após a deleção de uma receita.
    """
    message: str

def apresenta_receita(receita: Receita):
    """ Retorna uma representação da receita seguindo o schema definido em
        ReceitaViewSchema.
    """
    return {
        "id": receita.id,
        "descricao": receita.descricao,
        "valorBruto": receita.valorBruto,
        "valorLiquido": receita.valorLiquido,
        "data": receita.data
    }