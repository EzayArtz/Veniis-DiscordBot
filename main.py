import discord

import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'BotID: {bot.user.id} - Name {bot.user.name}')
    bot.loop.create_task(status_task())


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game('Veniis Discord Server!!'))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game('discord.com/QyN6JS3Hz9'))
        await asyncio.sleep(5)


@bot.command()
async def tiktok(ctx):
    ttembed = discord.Embed(title='Veniis TikTok', description='━━━━━━━━━━━━━━━━━\n\n**Folgst** du **Veni** noch '
                                                               'nicht?\n dann mach das doch einfach '
                                                               '**jetzt**!\nhttps://www.tiktok.com/@veniixd\n\n'
                                                               '━━━━━━━━━━━━━━━━━', color=0xcc00ff, )
    ttembed.set_thumbnail(url=bot.user.avatar_url)
    ttembed.set_image(url='https://i.ibb.co/JCktsMn/standard-1.gif')
    await ctx.send(embed=ttembed)


@bot.command()
async def support(ctx):
    helpembed = discord.Embed(title='Brauchst du hilfe?', description='━━━━━━━━━━━━━━━━━\n\n**Commands**\n\n**➤ !tiktok'
                                                                      '**\n '
                                                                      '**➤ !support**\n\n**Möchtest du was '
                                                                      'melden?**\n\n '
                                                                      'Joine '
                                                                      'einfach '
                                                                      'unsere Support channel wir kümmern uns dann um '
                                                                      'dich\n\n━━━━━━━━━━━━━━━━━', color=0xcc00ff, )
    helpembed.set_thumbnail(url=bot.user.avatar_url)
    helpembed.set_image(url='https://i.ibb.co/JCktsMn/standard-1.gif')
    await ctx.send(embed=helpembed)


bot.run('ODYxMDIxNjkyODY4MDM0NTcw.YODu8A.fsJvx7sBO1V_CTZigtr0EqO-yeg')
