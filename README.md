# 🤖 GS 2025.2 - Future Skills Lab

Este projeto é a solução para a Global Solution 2025.2 da disciplina de Pensamento Computacional e Automação com Python.

## 🎯 Propósito do Projeto

O "Future Skills Lab" é uma ferramenta inteligente de orientação de carreiras. O sistema, desenvolvido em Python com orientação a objetos, analisa perfis profissionais com base em competências técnicas e comportamentais (como lógica, criatividade e colaboração).

Com base na análise, a aplicação gera recomendações personalizadas, indicando carreiras futuras e trilhas de aprendizado para aprimoramento.

## 🛠️ Estrutura de Arquivos e Classes

O projeto está organizado da seguinte forma:

- **`models.py`**: Contém as classes principais que modelam o domínio do problema.
  - `Perfil`: Armazena o nome e um dicionário de competências do usuário.
  - `Carreira`: Armazena o nome, descrição e um dicionário de competências requeridas.
  - `SistemaOrientacao`: Classe principal que contém a lógica de análise, cadastra carreiras e compara perfis com requisitos.

- **`main.py`**: Ponto de entrada da aplicação.
  - Contém a interface de usuário textual (CLI).
  - Gerencia o menu principal e a coleta de dados do usuário.
  - Chama o `SistemaOrientacao` para processar os dados e exibe os resultados formatados.

## 🚀 Instruções de Execução

Para executar este projeto, você precisa ter o Python 3.x instalado.

1.  Clone este repositório:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_AQUI]
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
3.  Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```
4.  Siga as instruções no terminal para analisar seu perfil.

## 📸 Demonstração

*(Opcional: Adicione aqui um print da tela do seu terminal executando o programa)*
