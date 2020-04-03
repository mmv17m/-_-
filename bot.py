import discord
import asyncio
import requests
import random2
import aiohttp

from discord.ext import commands
from os import listdir
from os.path import isfile, join


DISCORD_BOT_TOKEN = 'NjkwMTk3ODgxNDAzMDgwODM2.XnN64w.vdnUrjUFRrPfKMLt1dCEjEZyy40'              
def get_prefix(bot, message):
    prefixes = ['?']
   
    if not message.guild:      
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)
class SimpleCog:
    def __init__(self, bot):
        self.bot = bot

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')


@bot.event
async def on_ready():   

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')


visadka = ["Вы высадились без проишествий", "Ваш карабль сбили во время перелёта",]
@bot.command(pass_context = True)
@commands.has_role("Отряд Альфа")
async def высадка(ctx):
	emb = discord.Embed(title = random2.choice(visadka), colour = discord.Color.green())

	emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	emb.set_image(url = "http://www.gamer.ru/system/attached_images/images/000/197/947/original/e01c243f7e28.jpg")
	emb.set_thumbnail(url = "http://dreamworlds.ru/uploads/posts/2013-03/1363174882_without-heads.jpg")

	await ctx.send(embed = emb)

tank = ["Выстрелом из танка ты убил одного", "Выстрелом из танка ты убил двоих", "Выстрелом из танка ты убил троих", "Выстрелом из танка ты убил  четверых"]
@bot.command(pass_context = True)
@commands.has_role("Отряд Альфа")
async def танк(ctx):
	emb1 = discord.Embed(title = random2.choice(tank), colour = discord.Color.blue())

	emb1.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
	emb1.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	emb1.set_image(url = "http://img0.reactor.cc/pics/post/Warhammer-40000-%D1%84%D1%8D%D0%BD%D0%B4%D0%BE%D0%BC%D1%8B-Imperium-Librarium-757218.jpeg") 
	emb1.set_thumbnail(url = "http://img1.reactor.cc/pics/post/full/Warhammer-40000-%D1%84%D1%8D%D0%BD%D0%B4%D0%BE%D0%BC%D1%8B-Gray-Skull-artist-4221263.jpeg")

	await ctx.send(embed = emb1)

@bot.command(pass_context = True)
async def clear(ctx, amount = 1000):
	await ctx.channel.purge(limit = amount)

@bot.command(pass_context = True)
@commands.has_role("Отряд Альфа")
async def артиллерия(ctx):
	emb = discord.Embed(title = "Артиллерия дала залп по выданным координатам и уничтожала всё живое в этом квадрате", colour = discord.Color.green())

	emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	emb.set_image(url = "https://whec-assets-live.s3.amazonaws.com/2014/06/37537_3dad3a56eee78a274730855454397eea.jpg")
	emb.set_thumbnail(url = "https://hobbyworld.com.ua/published/publicdata/HOBBYWOR/attachments/SC/products_pictures/99120105047_BasiliskNEW01_enl.jpg")

	await ctx.send(embed = emb)
stroka = ["Ты попал в него", "Не попал в него"]
kartinka = ["https://data.1freewallpapers.com/detail/space-marines-warhammer-40-000.jpg" ]
@bot.command(pass_context = True)
@commands.has_role("Отряд Альфа")
async def стрелять(ctx):
	emb = discord.Embed(title = random2.choice(stroka), colour = discord.Color.green())

	emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	emb.set_image(url = random2.choice(kartinka))
	emb.set_thumbnail(url = "https://data.1freewallpapers.com/detail/space-marines-warhammer-40-000.jpg")

	await ctx.send(embed = emb)

pod = ["http://steammachine.ru/gallery/sh_1859318_3.jpg", "https://gamazavr.ru/media/products/product/14684849/screenshot_1728_1080_3.jpg", "https://s1.1zoom.ru/big3/750/351826-admin.jpg"]
podkrepa = ["Ты вызвал подкрепление и к вам пришли на помощь Космодесантники Крававых Ангелов", "Ты вызвал подкрепление и к вам на помощь пришли Ультрамарины", "Ты вызвал подкрепление и к вам на помощь пришли Тёмные Ангелы", "Ты вызвал подкрепление и к вам на помощь пришли Украинцы"]
@bot.command(pass_context = True)
@commands.has_role("Отряд Альфа")
async def подкрепление(ctx):
    emb = discord.Embed(title = random2.choice(podkrepa), colour = discord.Color.green())

    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
    emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.set_image(url = random2.choice(pod))
    emb.set_thumbnail(url = "https://vignette.wikia.nocookie.net/warhammer40k/images/1/16/The_Legiones_Astartes.png")

    await ctx.send(embed = emb)
 
bot.run(DISCORD_BOT_TOKEN)    
