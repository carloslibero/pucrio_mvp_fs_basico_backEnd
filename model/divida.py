#importa as bibliotecas necessárias para a classe
from sqlalchemy import *
from datetime import datetime
from model import Base
from typing import Union

#Classe divida - Não tem relação com usuários nessa versão do projeto
class Divida(Base):
    __tablename__ = 'divida'

    id = Column("pk_divida", Integer, primary_key=True)
    descricao = Column(String(255), unique=True, nullable=False)
    valorInicial = Column(Numeric(10,2), nullable=False)
    valorFinal = Column(Numeric(10,2), nullable=False)
    data = Column(Date, default=datetime.now())

    def __init__(self, descricao:str, valorInicial:float, valorFinal:float, data:Union[DateTime, None] = None):
        """
        Cria uma nova Divida

        Parametros:
            id: assinalada automaticamente pelo banco de dados
            descrição: descrição da divida
            valorInicial: valor do bem ou serviço original
            valorFinal: valor do bem ou serviço com os juros
            data: data da divida, se não for informada, será a data atual
        """
        self.descricao = descricao
        self.valorInicial = valorInicial
        self.valorFinal = valorFinal

        # se não for informada, será o data atual
        if data:
            self.data = data