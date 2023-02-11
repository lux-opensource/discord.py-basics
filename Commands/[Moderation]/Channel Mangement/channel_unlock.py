@bot.command()
@has_permissions(manage_channels = True) # Restricts to people who have the Manage Channels permission.
async def unlock(ctx):
   await ctx.message.delete()
   await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)   
   
   await ctx.send(f"{ctx.author.mention} Locked {ctx.channel.mention}")