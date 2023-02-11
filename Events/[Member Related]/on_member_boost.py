@bot.event
async def on_message(message):
    if message.type == discord.MessageType.premium_guild_subscription:
        print(f"{message.author} Just boosted the server.")