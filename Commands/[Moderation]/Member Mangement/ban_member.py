@bot.command()
@has_permissions(ban_members = True) # Restricts to people who have the Ban Members permission.
async def ban(ctx, member : discord.Member,*,reason=None):
   await member.ban(reason=reason, delete_message_days=7)

   await ctx.send(f"{ctx.author.mention} Banned {member.name}")