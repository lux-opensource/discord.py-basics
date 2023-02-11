@bot.event
async def on_message_delete(m):
    print(f"{m.author} Just deleted '{m.content}'")