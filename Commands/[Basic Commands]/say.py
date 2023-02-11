@bot.command()
async def say(ctx, *, msg):
    await ctx.send(msg)