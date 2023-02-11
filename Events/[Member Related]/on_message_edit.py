@bot.event
async def on_message_edit(message_before, message_after):
    print(f"{message_before.author} Updated his messsage. Before: {message_before.content} # After: {message_after.content}")