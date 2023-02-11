@bot.command()
async def memberid(ctx, *, msg):
    if ctx.author.id != (961281476371046550):  
        await ctx.send("You cannot use this.")
    else:
        await ctx.send("Hello.")