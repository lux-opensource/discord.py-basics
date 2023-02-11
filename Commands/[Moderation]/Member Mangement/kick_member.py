@bot.command()
@has_permissions(kick_members = True) # Restricts to people who have the Kick Members permission.
async def kick(ctx, member : discord.Member,*,reason=None):
   await member.kick(reason=reason)

   await ctx.send(f"{ctx.author.mention} Kicked {member.name}")