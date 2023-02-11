@bot.command()
@has_permissions(manage_nicknames = True)
async def setnickname(ctx, member: discord.Member, *, name=None):
    await member.edit(nick=name)
    await ctx.send(f"{ctx.author} Changed {member}'s nickname to {name}")