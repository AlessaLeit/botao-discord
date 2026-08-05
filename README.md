# Bot de Lembretes para Discord

Este é um bot simples para Discord projetado para funcionar como um agente pessoal de lembretes. Você pode agendar eventos e o bot enviará uma mensagem no canal designado quando a hora chegar.

## Estrutura do Projeto

```
├── .env.example
├── .gitignore
├── bot.py
├── carregar-env.ps1
└── requirements.txt
```

- **`bot.py`**: O código principal do bot em Python. Ele se conecta ao Discord, ouve por comandos e gerencia os lembretes.
- **`requirements.txt`**: Lista as dependências Python necessárias para rodar o projeto.
- **`.env.example`**: Um arquivo de exemplo mostrando quais variáveis de ambiente são necessárias.
- **`.gitignore`**: Garante que o arquivo `.env` com as chaves secretas não seja enviado para o Git.
- **`carregar-env.ps1`**: Um script PowerShell para carregar as variáveis de ambiente em um terminal local para fins de teste.

## Como Configurar e Rodar

1.  **Clone o Repositório**
    ```bash
    git clone <url-do-seu-repositorio>
    cd <nome-da-pasta>
    ```

2.  **Crie o Arquivo de Ambiente**
    - Copie o arquivo `.env.example` para um novo arquivo chamado `.env`.
    - Preencha o arquivo `.env` com suas chaves e IDs do Discord.

3.  **Instale as Dependências**
    - É recomendado criar um ambiente virtual primeiro.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Bot**
    ```bash
    python bot.py
    ```

O terminal deverá mostrar uma mensagem "Conectado como..." se tudo estiver correto.