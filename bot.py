import discord
import os
import sqlite3
from dotenv import load_dotenv
from discord.ext import commands, tasks

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Verificação de segurança: Garante que o bot não tente iniciar sem um token.
if not DISCORD_TOKEN:
    print("Erro: O token do Discord não foi encontrado. Verifique suas variáveis de ambiente.")
    exit()

# --- Configuração do Bot ---
# O 'intents' informa ao Discord quais tipos de eventos nosso bot quer receber.
intents = discord.Intents.default()
intents.message_content = True # Precisamos disso para ler o conteúdo das mensagens

bot = commands.Bot(command_prefix="!", intents=intents)

# --- Evento de Conexão ---
# Este evento é acionado quando o bot se conecta com sucesso ao Discord.
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name} (ID: {bot.user.id})')
    print('------')
    # Inicia a tarefa em segundo plano para verificar lembretes
    verificar_lembretes.start()

# --- Tarefa em Segundo Plano (Scheduler) ---
# Esta função rodará a cada 60 segundos para sempre.
@tasks.loop(seconds=60)
async def verificar_lembretes():
    # Aqui virá a lógica para:
    # 1. Consultar o banco de dados por lembretes que já passaram do tempo.
    # 2. Enviar uma mensagem no canal para cada lembrete encontrado.
    # 3. Marcar o lembrete como "enviado" no banco de dados.
    print("Verificando lembretes...") # Apenas para depuração

# Inicia a execução do bot
bot.run(DISCORD_TOKEN)