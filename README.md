# Meu Projeto Python

Este é um projeto Python que segue a arquitetura limpa, uma abordagem de organização do código que visa separar as responsabilidades em diferentes camadas para obter um código mais modular, testável e escalável.

## Ferramentas Utilizadas

O projeto utiliza as seguintes ferramentas:

- [Poetry](https://python-poetry.org/): Um gerenciador de dependências e ambientes virtuais para Python que simplifica o gerenciamento de pacotes e as configurações do projeto.

- [Flake8](https://flake8.pycqa.org/): Uma ferramenta de análise estática de código Python que verifica o estilo e a conformidade com as diretrizes definidas pelo guia de estilo PEP 8. Ele ajuda a manter um código Python limpo e legível.

- [Black](https://black.readthedocs.io/): Uma ferramenta de formatação de código Python que segue uma abordagem de "opinião única" para garantir um estilo de código consistente. O Black automatiza a formatação do código, eliminando discussões sobre estilo e mantendo um formato uniforme.

## Configuração e Utilização

Siga as instruções abaixo para configurar e utilizar as ferramentas no projeto:

### Poetry

1. Certifique-se de ter o Poetry instalado em seu ambiente. Caso contrário, siga as instruções na documentação oficial do Poetry.

2. Navegue até o diretório raiz do projeto no terminal ou prompt de comando.

3. Crie e ative um ambiente virtual com o Poetry usando o seguinte comando:
   `poetry shell`

4. Instale as dependências do projeto, incluindo as dependências de desenvolvimento, usando o seguinte comando:
   `poetry install`

Todas as dependências, incluindo o Flake8 e o Black, serão instaladas automaticamente.

### Verificação de Estilo e Qualidade

O projeto já está configurado para utilizar o Flake8 e o Black para verificação de estilo e qualidade de código. As configurações estão definidas no arquivo `pyproject.toml`.

- Para verificar o código Python com o Flake8, execute o seguinte comando:
  `poetry run lint`

O Flake8 irá verificar o código em busca de problemas de estilo e conformidade com as diretrizes do PEP 8.

- Para formatar automaticamente o código Python com o Black, execute o seguinte comando:
  `poetry run format`

O Black irá formatar o código, garantindo um estilo consistente.

Lembre-se de adaptar os comandos acima de acordo com a estrutura do seu projeto.

Aproveite o uso do Poetry, Flake8 e Black para garantir uma melhor organização, estilo e qualidade do código neste projeto
