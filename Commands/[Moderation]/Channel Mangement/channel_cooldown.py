@bot.command()
@has_permissions(manage_channels = True) # Restricts to people who have the Manage Channels permission.
async def unlock(ctx, seconds=0):
   await ctx.message.delete()
   await ctx.channel.edit(slowmode_delay=seconds)
   
   await ctx.send(f"{ctx.author.mention} Set cooldown to {seconds} Seconds")