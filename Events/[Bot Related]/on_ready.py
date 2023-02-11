@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Github"))

"""
# Setting `Playing ` status
await bot.change_presence(activity=discord.Game(name="Discord"))

# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))

# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Netflix"))
"""