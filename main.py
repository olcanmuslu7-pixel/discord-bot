import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def sa(ctx):
    await ctx.send("as")
 

@bot.command()
async def enguclukim(ctx):
    await ctx.send("tabikide EZOOOOOOO")


ROLE_NAME = "3e3e3e3e"

OWNER_ID = 808768680359100428

AUTO_ROLES = [
    "══▐ Seviye / Rank▐ ══",
    "No Ranked",
    "Unarilian",
    "══▐  Clan Maining▐ ══",
    "⚔️ Clan Wars",
    "══▐  Oyunlar / Games ▐ ══",
    "👊 The Strongest Battlegrounds",
    "══▐  Üye / Members▐ ══",
    "👤 Member",
    "❌ Untagged",
    "══▐ Uyarılar / Warnings▐ ══"
]

@bot.event
async def on_member_join(member):
    # Tek bir handler içinde hem ROLE_NAME hem de AUTO_ROLES ekleniyor.
    try:
        role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
        if role:
            await member.add_roles(role)
    except Exception as e:
        print(f"ROLE_NAME rolü eklenirken hata: {e}")

    for role_name in AUTO_ROLES:
        try:
            role = discord.utils.get(member.guild.roles, name=role_name)
            if role:
                await member.add_roles(role)
        except Exception as e:
            print(f"Otomatik rol '{role_name}' eklenirken hata: {e}")

@bot.command()
async def kilitle(ctx):
    if ctx.author.id != OWNER_ID:
        return

    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, send_messages=False, speak=False)
    await ctx.send("🔒 Sunucu kilitlendi.")

@bot.command()
async def ac(ctx):
    if ctx.author.id != OWNER_ID:
        return

    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, send_messages=True, speak=True)

    await ctx.send("🔓 Sunucu açıldı.")

@bot.command()
async def gir(ctx):
    channel = discord.utils.get(ctx.guild.voice_channels, name="「🗡️」XcX")
    if channel is None:
        await ctx.send("XcX adlı sesli kanal bulunamadı.")
        return

    await channel.connect()

@bot.command()
async def cik(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("🔇 Sesten çıktım.")
    else:
        await ctx.send("Zaten seste değilim.")

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(name="UNİTAS koruyor.")
    )
    print("BOT AKTIF:", bot.user)

    channel_name = "「💬」sohbet-chat"
    startup_message = "sikim kocamn indirecek dm."

    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if channel:
            try:
                await channel.send(startup_message)
            except Exception as e:
                print(f"Hata gönderilirken ({guild.name}): {e}")

# Token güvenliği: ortam değişkeni kullanılması önerilir.
TOKEN = os.getenv("DISCORD_TOKEN", "MTQ1OTg3OTQ0NTY3MzQxNDgyMA.GH7mHA.sNC5XOwKXlbNdoHDImVMBeBSysH9ikEOqaMOKM")
bot.run(TOKEN)
