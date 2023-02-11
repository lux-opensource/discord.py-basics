@bot.event
async def on_guild_channel_create(channel):
    print(f"{channel} has been created.")