#importa as bibliotecas necessárias para a classe
from sqlalchemy import *
from datetime import datetime
from model import Base
from typing import Union

#Classe receita - Não tem relação com usuários nessa versão do projeto
class Receita(Base):
    __tablename__ = 'receita'

    id = Column("pk_receita", Integer, primary_key=True)
    descricao = Column(String(255), unique=True, nullable=False)
    valorBruto = Column(Numeric(10,2), nullable=False)
    valorLiquido = Column(Numeric(10,2), nullable=False)
    data = Column(Date, default=datetime.now())

    def __init__(self, descricao:str, valorBruto:float, valorLiquido:float, data:Union[DateTime, None] = None):
        """
        Cria uma nova Receita

        Parametros:
            id: assinalada automaticamente pelo banco de dados
            descrição: descrição da receita
            valorBruto: valor bruto da receita
            valorLiquido: valor liquido da receita
            data: data da receita, se não for informada, será a data atual
        """
        self.descricao = descricao
        self.valorBruto = valorBruto
        self.valorLiquido = valorLiquido

        # se não for informada, será o data atual
        if data:
            self.data = data