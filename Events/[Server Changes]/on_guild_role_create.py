@bot.event
async def on_guild_role_create(role):
    print(f"{role} has been created.")