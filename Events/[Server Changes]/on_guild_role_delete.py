@bot.event
async def on_guild_role_delete(role):
    print(f"{role} has been deleted.")