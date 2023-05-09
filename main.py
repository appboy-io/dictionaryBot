import os
from dotenv import load_dotenv
import requests
import interactions

load_dotenv()

token = os.getenv("dictionary_bot_token")
apiToken = os.getenv("dictionary_api_token")
default_scope_guild = os.getenv("guildid")

bot = interactions.Client(token=token, default_scope=default_scope_guild) if default_scope_guild is None else interactions.Client(token=token)

@bot.command(name="define", description="Lookup a word")
@interactions.option()
async def dictionary(ctx: interactions.CommandContext, text: str):
    try:
        r = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}'.format(text, apiToken))
        json = r.json()
        def_list = ""
        for x in json:
            pos = x['fl']
            for shortdef in x['shortdef']:
                def_list = def_list + "\n" + "(" + pos + ") - " +shortdef

        def_list = def_list 

        await ctx.send(f"""
            Definitions of **{text}**: 
            {def_list}
        """)
    except:
        await ctx.send(f"There was an error trying to find that word") 

bot.start()