# Minha API

MVP da Pós em Full Stack da PucRio - Parte 1 - **Desenvolvimento Full Stack Básico** 

O objetivo aqui é atender aos requisitos do MVP através de um aplicativo para controlar as receitas e dividas.
Foi desenvilvido um aplicativo para permitir o cadastro de Receitas e Dividas, para auxiliar no endimento de onde as dívidas estão localizadas e na capacidade de pagamento das mesmas.

---
# Como executar
Será necessário ter todas as libs python listadas no requirements.txt instaladas. Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

É fortemente indicado o uso de ambientes virtuais do tipo virtualenv.

(env)$ pip install -r requirements.txt
Este comando instala as dependências/bibliotecas, descritas no arquivo requirements.txt.

Para executar a API basta executar:

(env)$ flask run --host 0.0.0.0 --port 5000
Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

(env)$ flask run --host 0.0.0.0 --port 5000 --reload
Abra o http://localhost:5000/#/ no navegador para verificar o status da API em execução."# pucrio_mvp_fs_basico_backEnd" 
