@bot.command()
@has_permissions(manage_messages = True) # Restricts to people who have the Manage Messages permission.
async def clear(ctx, amount=1):
   await ctx.message.delete()
   await ctx.channel.purge(limit=amount)      
   
   await ctx.send(f"{ctx.author.mention} Cleared {amount}")