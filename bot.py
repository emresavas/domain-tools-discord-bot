import os
import discord
from discord.ext import commands
import requests

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
APILAYER_KEY = os.getenv('APILAYER_KEY')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')


@bot.command(name='whois',
             help='Get domain whois information. Usage: !whois <domain>')
async def whois(ctx, domain: str):
  if not domain:
    await ctx.send('Please provide a domain. Usage: !whois <domain>')
    return

  headers = {
    'apikey': APILAYER_KEY,
  }
  url = f'https://api.apilayer.com/whois/query?domain={domain}'
  response = requests.get(url, headers=headers)
  data = response.json()

  if response.status_code == 200:
    embed = discord.Embed(title="WHOIS Information",
                          description=f"Domain: {domain}",
                          color=0x00FF00)
    for key, value in data.get('result').items():
      embed.add_field(name=key.capitalize(), value=value, inline=False)
    await ctx.send(embed=embed)
  else:
    await ctx.send(
      f"Error: {data['message'] if data and data['message'] else 'Unable to execute request'}"
    )


@bot.command(
  name='dns',
  help='Get domain DNS information. Usage: !dns <domain> <record_type>')
async def dns(ctx, domain: str, record_type: str = 'A'):
  if not domain:
    await ctx.send(
      'Please provide a domain. Usage: !dns <domain> <record_type>')
    return

  headers = {
    'apikey': APILAYER_KEY,
  }
  url = f'https://api.apilayer.com/dns_lookup/api/{record_type}/{domain}'
  response = requests.get(url, headers=headers)
  data = response.json()

  if response.status_code == 200:
    embed = discord.Embed(
      title="DNS Information",
      description=f"Domain: {domain}\nRecord Type: {record_type.capitalize()}",
      color=0x00FF00)
    for record in data.get('results'):
      for key, value in record.items():
        embed.add_field(name=key.capitalize(), value=value, inline=False)
    await ctx.send(embed=embed)
  else:
    await ctx.send(
      f"Error: {data['message'] if data and data['message'] else 'Unable to execute request'}"
    )

bot.run(DISCORD_BOT_TOKEN)
