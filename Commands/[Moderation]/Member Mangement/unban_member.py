@bot.command()
@has_permissions(ban_members = True) # Restricts to people who have the Ban Members permission.
async def unban(ctx, id: int):
   user = await bot.fetch_user(id)
   await ctx.guild.unban(user)

   await ctx.send(f"{ctx.author.mention} Unbanned {user}")