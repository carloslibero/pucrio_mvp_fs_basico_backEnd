#importa as bibliotecas necessárias para o projeto
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
#from flasgger import Swagger

from sqlalchemy.exc import IntegrityError

from model import Session, Receita, Divida
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
receita_tag = Tag(name="Receita", description="Adição, visualização e remoção de receitas à base")
divida_tag = Tag(name="Divida", description="Adição, visualização e remoção de dividas à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

#Rotas para as receitas

#Rota para inserção de receitas
@app.post('/receita', tags=[receita_tag],
          responses={"200": ReceitaViewSchema, "400": ErrorSchema})
def add_receita(form: ReceitaSchema):
    """Adiciona uma nova Receita à base de dados

    Retorna uma representação das receitas
    """
    receita = Receita(
        descricao=form.descricao,
        valorBruto=form.valorBruto,
        valorLiquido=form.valorLiquido,
        data=form.data)
    logger.debug(f"Adicionanda receita de valor: '{receita.valorBruto}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionanda a receita
        session.add(receita)
        # Confirma a alteração no bando de dados
        session.commit()
        logger.debug(f"Adicionada receita de valor: '{receita.valorBruto}'")
        return apresenta_receita(receita), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova receita :/"
        logger.warning(f"Erro ao adicionar a receita '{receita.valorBruto}', {error_msg}")
        return {"message": error_msg}, 400

#Rota para buscar as receitas cadastradas
@app.get('/receitas', tags=[receita_tag],
         responses={"200": ListagemReceitasSchema, "404": ErrorSchema})
def get_receitas():
    """Faz a busca por todos as Receitas cadastradas

    Retorna uma representação da listagem de receitas.
    """
    logger.debug(f"Coletando receitas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    receitas = session.query(Receita).all()

    if not receitas:
        # se não há receitas cadastradas
        return {"receitas": []}, 200
    else:
        logger.debug(f"%d receitas econtradas" % len(receitas))
        # retorna a representação de receitas
        print(receitas)
        return apresenta_receitas(receitas), 200


#Rota para buscar receitas pela descrição
@app.get('/receita', tags=[receita_tag],
         responses={"200": ReceitaViewSchema, "404": ErrorSchema})
def get_receita(query: ReceitaBuscaSchema):
    """Faz a busca por uma Receita a partir da descrição

    Retorna uma representação da Receita relacionada.
    """
    receita_descricao = query.descricao
    logger.debug(f"Coletando dados sobre receita #{receita_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    receita = session.query(Receita).filter(Receita.descricao == receita_descricao).first()

    if not receita:
        # se a receita não foi encontrada
        error_msg = "Receita não encontrada na base :/"
        logger.warning(f"Erro ao buscar a receita '{receita_descricao}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Receita econtrada: '{receita_descricao}'")
        # retorna a representação da receita
        return apresenta_receita(receita), 200


#Rota para deletar receitas pela descrição
@app.delete('/receita', tags=[receita_tag],
            responses={"200": ReceitaDelSchema, "404": ErrorSchema})
def del_receita(query: ReceitaBuscaSchema):
    """Deleta uma Receita a partir da descrição da receita informada

    Retorna uma mensagem de confirmação da remoção.
    """
    receita_descricao = unquote(unquote(query.descricao))
    print(receita_descricao)
    logger.debug(f"Deletando dados sobre receita #{receita_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Receita).filter(Receita.descricao == receita_descricao).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado receita #{receita_descricao}")
        return {"message": "Receita removida", "descrição": receita_descricao}
    else:
        # se a receita não foi encontrada
        error_msg = "Receita não encontrada na base :/"
        logger.warning(f"Erro ao deletar receita #'{receita_descricao}', {error_msg}")
        return {"mesage": error_msg}, 404


#Rotas para as Dividas

#Rota para inserção de dividas
@app.post('/divida', tags=[divida_tag],
          responses={"200": DividaViewSchema, "400": ErrorSchema})
def add_divida(form: DividaSchema):
    """Adiciona uma nova Divida à base de dados

    Retorna uma representação das dividas
    """
    divida = Divida(
        descricao=form.descricao,
        valorInicial=form.valorInicial,
        valorFinal=form.valorFinal,
        data=form.data)
    logger.debug(f"Adicionanda divida de valor: '{divida.valorInicial}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionanda a divida
        session.add(divida)
        # Confirma a alteração no bando de dados
        session.commit()
        logger.debug(f"Adicionada divida de valor: '{divida.valorInicial}'")
        return apresenta_divida(divida), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova divida :/"
        logger.warning(f"Erro ao adicionar a divida '{divida.valorInicial}', {error_msg}")
        return {"message": error_msg}, 400


#Rota para buscar as dividas cadastradas
@app.get('/dividas', tags=[divida_tag],
         responses={"200": ListagemDividasSchema, "404": ErrorSchema})
def get_dividas():
    """Faz a busca por todos as Dividas cadastradas

    Retorna uma representação da listagem de dividas.
    """
    logger.debug(f"Coletando dividas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    dividas = session.query(Divida).all()

    if not dividas:
        # se não há dividas cadastradas
        return {"dividas": []}, 200
    else:
        logger.debug(f"%d dividas econtradas" % len(dividas))
        # retorna a representação de dividas
        print(dividas)
        return apresenta_dividas(dividas), 200

#Rota para buscar dividas pela descricao
@app.get('/divida', tags=[divida_tag],
         responses={"200": DividaViewSchema, "404": ErrorSchema})
def get_divida(query: DividaBuscaSchema):
    """Faz a busca por uma Divida a partir da descrição

    Retorna uma representação da Divida relacionada.
    """
    divida_descricao = query.descricao
    logger.debug(f"Coletando dados sobre divida #{divida_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    divida = session.query(Divida).filter(Divida.descricao == divida_descricao).first()

    if not divida:
        # se a divida não foi encontrada
        error_msg = "Divida não encontrada na base :/"
        logger.warning(f"Erro ao buscar a divida '{divida_descricao}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Divida econtrada: '{divida_descricao}'")
        # retorna a representação da divida
        return apresenta_divida(divida), 200


#Rota para deletar dividas pelo nome
@app.delete('/divida', tags=[divida_tag],
            responses={"200": DividaDelSchema, "404": ErrorSchema})
def del_divida(query: DividaBuscaSchema):
    """Deleta uma Divida a partir do nome da divida informada

    Retorna uma mensagem de confirmação da remoção.
    """
    divida_descricao = unquote(unquote(query.descricao))
    print(divida_descricao)
    logger.debug(f"Deletando dados sobre divida #{divida_descricao}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Divida).filter(Divida.descricao == divida_descricao).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado divida #{divida_descricao}")
        return {"message": "Divida removida", "descrição": divida_descricao}
    else:
        # se a Divida não foi encontrada
        error_msg = "Divida não encontrada na base :/"
        logger.warning(f"Erro ao deletar divida #'{divida_descricao}', {error_msg}")
        return {"mesage": error_msg}, 404