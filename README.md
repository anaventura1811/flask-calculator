# Flask Calculator

**Flask Calculator** é uma aplicação de calculadora desenvolvida com Python e Flask, com o objetivo de consolidar os conceitos de Programação Orientada a Objetos (OOP) e implementar princípios de design de código e arquitetura de software. Este projeto serve como prática para estruturar um projeto de forma mais profissional, tendo como objetivos principais refinar skills de organização e de clareza do código.
Sendo assim, a ideia era praticar a aplicação de alguns princípios e boas práticas relativos ao SOLID e clean code.

## Sobre o Projeto

Este projeto foi criado para aprofundar o conhecimento em OOP e em boas práticas de desenvolvimento com Flask, incluindo a separação de responsabilidades, a organização de pastas e módulos, e o uso de classes para estruturar a lógica de operações matemáticas. A aplicação calcula operações básicas e demonstra como uma arquitetura bem definida facilita o desenvolvimento e manutenção do código. 

## Funcionalidades

- **Operações Básicas**: Suporta operações como cálculo de média, desvio padrão e etc.
- **Design Modular**: Cada operação é organizada em módulos específicos, facilitando a manutenção e escalabilidade do projeto.
- **Interface Web Simples**: A aplicação Flask oferece uma interface web para que os usuários possam realizar cálculos diretamente no navegador.
- **Error handling**: Criação de um controller para customizar respostas de erro e apresentá-las de forma mais amigável ao usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web utilizado para criar a API da calculadora.
- **NumPy**: Biblioteca utilizada para lidar com algumas operações matemáticas mais complexas.
- **PyTest**: Biblioteca utilizada para implementação de testes unitários e de integração das funcionalidades da calculadora, englobando tanto o "caminho feliz" da aplicação quanto os casos de erro.
- **OOP**: Abordagem utilizada para estruturar o projeto e as operações matemáticas.

<img width="1153" alt="Captura de Tela 2024-11-03 às 20 42 49" src="https://github.com/user-attachments/assets/bcf4831a-08aa-4d50-9c46-6e54d968e014">


## Estrutura do Projeto

O projeto segue uma estrutura organizada e modular, com classes e funções separadas para cada operação, além de uma arquitetura que facilita a extensão do código e a integração de novas funcionalidades. Essa abordagem ajuda a compreender a importância de um código bem estruturado e das boas práticas no desenvolvimento de aplicações.

## Rotas
- POST - /calculator/1 
- POST - /calculator/2
- POST - /calculator/3
- POST - /calculator/4

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/flask-calculator.git
    cd flask-calculator
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor:
    ```bash
    flask run
    ```

5. Acesse a calculadora no navegador:
    ```
    http://127.0.0.1:3000
    ```

## Licença

Este projeto é licenciado sob a Licença MIT.
