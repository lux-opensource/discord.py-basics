@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")