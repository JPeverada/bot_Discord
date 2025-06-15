import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados")
    print("Bot inicializado com sucesso")

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel("ID do Channel")
    await canal.send(f"Seja bem vindo!!! {membro.mention} entrou no servidor!")

@bot.event
async def on_member_join(membro:discord.Member):
    membro
"""""
@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Oi {nome}!")

@bot.command()
async def falar(ctx: commands.Context, *, texto):
    await ctx.send(texto)
"""
@bot.tree.command()
async def ola(interact:discord.Interaction):
    await interact.response.defer()
    await interact.followup.send(f"Olá, {interact.user.name}! Tudo bem?")

@bot.tree.command()
async def falar(interact:discord.Interaction, texto:str):
  await interact.response.send_message(texto)  
    
@bot.tree.command()
async def calcular(interact:discord.Interaction, num1:float,op:str, num2:float):
 if(op == '+' or op =='somar' or 'mais'):
    resultado = num1 + num2
    
    await interact.response.send_message(f"Tá aqui o resultado da soma {resultado}!")

 elif(op == '-' or 'subtrair' or 'diminuir'):
    resultado = num1 - num2
    
    await interact.response.send_message(f"Tá aqui o resultado da subtração {resultado}!")

 elif(op == 'x' or op == '*' or op == 'multiplicar'):
    resultado = num1 * num2
    
    await interact.response.send_message(f"Tá aqui o resultado da multiplicação {resultado}!")

 elif(op == '/' or op == 'dividir'):
    if(num2 != 0):
        resultado = num1 / num2
        
        await interact.response.send_message(f"Tá aqui o resultado da divisão {resultado}!")
    else:
       
       await interact.response.send_message("Não dá pra dividir por zero, né 😅")

 else:
    
    await interact.response.send_message("A opreção é inválida!")

bot.run("Token do BOT")