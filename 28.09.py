import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def member(ctx, member: discord.Member):
    await ctx.send(f'{member.name} {member.display_name} {member.created_at} {member.guild.name}')

@bot.command()
async def message(ctx):
    await ctx.send(ctx.message.author.name)
        
bot.run("TOKEN")
