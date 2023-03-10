@bot.command()
async def botinfo(ctx):
        a = sum([len(guild.members) for guild in bot.guilds])
        embed = discord.Embed(title=f"Discord Bot Information", colour=0x0ffff)  
        embed.add_field(name="Discord Name:", value=f" {bot.user.mention}", inline=True)
        embed.add_field(name="Discord ID:", value=f" ```{bot.user.id}```", inline=True)
        embed.add_field(name="Bot Created:", value=f'```{bot.user.created_at.strftime("%d/%m/%Y %H:%M:%S")}```', inline=False)
        embed.add_field(name="Server Count:", value=f'```{len(bot.guilds)}```', inline=True)
        embed.add_field(name="Total Members From All Servers:", value=f'```{a}```', inline=True)
        embed.add_field(name="Bot Status:", value=f'```🟢 Online```', inline=False)
        await ctx.send(embed=embed)   