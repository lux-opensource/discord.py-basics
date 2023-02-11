@bot.event
async def on_guild_channel_delete(channel):
    print(f"{channel} has been deleted.")