import discord
import random2


from discord.ext import commands
import os
from discord.ext.commands import bot
Bot = commands.Bot(command_prefix=".")


 


popal = ["Ты ранил его", "Ты убил его", "Ты не попал в него", "Ты не попал в него"]
popal1 = ["https://cs8.pikabu.ru/post_img/2016/06/08/9/1465396529120943651.jpg", "https://pnevmat24.ru/image/catalog/files/categories/airsoft/avtomatyivintovki2.jpg"]
@Bot.command()
async def стрелять(ctx):
	emb = discord.Embed(title = random2.choice(popal), colour = discord.Color.green())

	emb.set_author(name = Bot.user.name, icon_url = Bot.user.avatar_url)
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	emb.set_image(url = random2.choice(popal1))
	emb.set_thumbnail(url = "http://www.airsoft.kg/forum/uploads/post-80-1231432069_thumb.jpg")

	await ctx.send(embed = emb)

granata = ["Ты кинул гранату и убил одного", "Ты кинул гранату и убил двоих", "Ты кинул гранату и убил троих", "Граната не долетела", "Ты криво кинул гранату" "Граната взорвалась у тебя в руке"]
@Bot.command(pass_context = True)
async def граната(ctx):
	emb = discord.Embed(title = random2.choice(granata), colour = discord.Color.green())

	emb.set_author(name = Bot.user.name, icon_url = Bot.user.avatar_url)
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	emb.set_image(url = "https://i.siteapi.org/l9q5FHblgIocYbq5v2U1RYYY9NM=/fit-in/330x/top/filters:format(webp)/0cef3703d382b3d.s.siteapi.org/img/11a73eb3a7cd0bb6c616222d9a01548fd71aa7ad.jpg")
	emb.set_thumbnail(url = "http://images.aif.ru/007/382/5810c4d77d79c3d828377e1fd3e5f9ed.jpg")

	await ctx.send(embed = emb)

snaiper = ["Ты попал прям в цель", "Ты попал прям в цель", "Ты попал прям в цель", "Ты попал прям в цель", "Ты ранил его", "Ты не попал"]
@Bot.command(pass_context = True)
async def снайпер(ctx):
	emb = discord.Embed(title = random2.choice(snaiper), colour = discord.Color.green())

	emb.set_author(name = Bot.user.name, icon_url = Bot.user.avatar_url)
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	emb.set_image(url = "https://go4.imgsmail.ru/imgpreview?key=50592ce8b177f788&mb=imgdb_preview_766")
	emb.set_thumbnail(url = "http://files.storeland.ru/web/upload/sitefiles/6/513/512843/flag-snajper-chernyje-berety.jpg")

	await ctx.send(embed = emb)

@Bot.command(pass_context = True)
async def clear(ctx, amount = 1000):
	await ctx.channel.purge(limit = amount)





token = os.environ.get("BOT_TOKEN")
Bot.run(str(token))
