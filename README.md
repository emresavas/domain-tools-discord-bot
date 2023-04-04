# Domain Tools Discord Bot
This project is a simple Discord bot that can fetch domain WHOIS and DNS information using the APILayer API. The bot uses the discord.py library and provides two main commands:

- `!whois <domain>`: Gets the domain's WHOIS information.
- `!dns <domain> <record_type>`: Gets the domain's DNS information for a specific record type (defaults to 'A' record).

## Requirements
- Python 3.6 or higher
- A Discord bot token
- An APILayer API key. [Create Free APILayer Account](https://apilayer.com/)

## Dependencies
- requests
- discord.py

## Installation
- Clone the repository:
```
git clone https://github.com/emresavas/domain-tools-discord-bot.git
```
- Change to the project directory:
```
cd domain-tools-discord-bot
```
- Install the required packages:
```
pip install discord.py requests
```
- Create a .env file in the project directory and add your Discord bot token and apilayer API key:
```
DISCORD_BOT_TOKEN=your_discord_bot_token_here
APILAYER_KEY=your_apilayer_key_here
```
- Remember to replace your_discord_bot_token_here and your_apilayer_key_here with your actual Discord bot token and apilayer API key, respectively.

# Running the bot
Execute the script using Python:
`python bot.py`
Once the bot is running, you can use the !whois and !dns commands in your Discord server to get domain WHOIS and DNS information.
