@bot.event
async def on_guild_channel_pins_update(channel, last_pin):
    print(f"{channel.name} Just updated channel pins. {last_pin}")