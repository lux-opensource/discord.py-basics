"""
⛔ lux-opensource Github. Created this masterpiece. Please do not sell this source. You are allowed to share, and use, and edit.

📄 Some basic information: All the main files in folders are snip codes, and are not actually full discord bots. Here in the
basic template.py file you can see how an actual discord bot is coded fully. With some basic commands/events. You should only
use the snip codes to add more into here or you personal discord bot. 

❓ (The snip codes will give you a error that 'bot' is not found, because it is not a full discord bot, just discord.py events)
"""

"""
Help full links for Discord.py

> Discord Developer Portal:https://discord.com/developers/docs/intro
> Discord.py Docs: https://discordpy.readthedocs.io/
> Discord Permissions: https://discordpy.readthedocs.io/en/latest/api.html#discord.Permissions
> Python: https://www.python.org/downloads/
> My Discord: https://discord.gg/jQEeshZ2
"""

# Import Modules - Require for discord.py [Make sure you also follow the requirements.txt file to install all of these]
import discord
from discord import embeds
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.core import has_permissions
from discord.ext.commands.core import has_role
from discord.ext.commands import CommandNotFound
from discord.ext.commands.errors import CommandInvokeError, CommandOnCooldown, MissingPermissions, MissingRequiredArgument, CommandNotFound, NoPrivateMessage, MissingRole

intents = discord.Intents.all() # Make sure to set these in discord developer portal.
bot = commands.AutoShardedBot(command_prefix='!', intents=intents) # Your default prefix (in this instance its !)
bot.remove_command('help')

# Basic Discord Load - Change Status
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Github"))

# Command Errors, Capture
@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, MissingPermissions):
        print("User is missing permissions")

    if isinstance(error, MissingRequiredArgument):
        print("Missing require argument, Example: !user <mention>")

    if isinstance(error, CommandNotFound):
        print("Command not found")

    if isinstance(error, CommandOnCooldown):
        print("Command on cooldown")

    if isinstance(error, MissingRole):
        print("User is missing the role")

    if isinstance(error, CommandInvokeError):
        print(f"{error}")

# Basic Discord Events - Server Related
@bot.event
async def on_guild_role_create(role): # Captures 'Role Created'
    print(f"{role} has been created.")

@bot.event
async def on_guild_role_delete(role): # Captures 'Role Deleted'
    print(f"{role} has been deleted.")

@bot.event
async def on_guild_channel_delete(channel): # Captures 'Channel Created'
    print(f"{channel} has been deleted.")

@bot.event
async def on_guild_channel_create(channel): # Captures 'Channel Created'
    print(f"{channel} has been created.")

@bot.event
async def on_guild_channel_pins_update(channel, last_pin): # Captures 'Pins Updated'
    print(f"{channel.name} Just updated channel pins. {last_pin}")

# Basic Discord Events - Member Related
@bot.event
async def on_message(message):
    print(f"{message.author} Just said '{message.content}'") # Captures 'Message Sent'

@bot.event
async def on_message_delete(m):
    print(f"{m.author} Just deleted '{m.content}'") # Captures 'Message Delete'

@bot.event
async def on_message_edit(message_before, message_after): # Captures 'Message Edited'
    print(f"{message_before.author} Updated his messsage. Before: {message_before.content} # After: {message_after.content}")

@bot.event
async def on_member_update(before, after):
    if len(before.roles) > len(after.roles):
        role = next(role for role in before.roles if role not in after.roles) # Captures 'Role Added'
        note = f"**{role.name}** was removed from **{before.mention}**"

    elif len(after.roles) > len(before.roles):
        role = next(role for role in after.roles if role not in before.roles) # Captures 'Role Removed'
        note = f"**{role.name}** was added to **{before.mention}**"

    elif before.nick != after.nick: # Captures 'Nickname Changed'
        note = f"**{before.mention}** Nickname was set to ``{after.nick}`` from ``{before.nick}``"
    else:
        return
    print(note)

# Basic Discord Commands
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")

@bot.command()
async def say(ctx, *, msg):
    await ctx.send(msg)

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

@bot.command()
async def server(ctx):
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)
        channel_count = len([x for x in ctx.guild.channels if type(x) == discord.channel.TextChannel])
        embed = discord.Embed(title=f"Server Information : {ctx.guild.name}", colour=0xf0000)  
        embed.add_field(name="Server Name:", value=f" ```{ctx.guild.name}```", inline=True)
        embed.add_field(name="Server ID:", value=f" ```{ctx.guild.id}```", inline=True)
        embed.add_field(name="Security Level:", value=f" ```{ctx.guild.verification_level}```", inline=False)
        embed.add_field(name="Creation Date:", value=f" ```{ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')}```", inline=False)
        embed.add_field(name="Total Categorys:", value=f" ```{len(ctx.guild.categories)}```", inline=True)
        embed.add_field(name="Text Channels:", value=f" ```{str(channel_count)}```", inline=True)
        embed.add_field(name="Voice Channels:", value=f" ```{len(ctx.guild.voice_channels)}```", inline=True)
        embed.add_field(name="Total Members:", value=f" ```{ctx.guild.member_count}```", inline=True)
        embed.add_field(name="Total Roles:", value=f' ```{str(role_count)}```', inline=True)
        embed.add_field(name="Total Emojis:", value=f' ```{str(emoji_count)}```', inline=True)
        embed.add_field(name="Total Boosts:", value=f' ```{str(ctx.guild.premium_subscription_count)}```', inline=True)
        embed.set_author(name="Lux - Github Proj")
        await ctx.send(embed=embed)  

@bot.command()
async def user(ctx, member : discord.Member):
        embed = discord.Embed(title=f"Discord User Information : {member.name}", colour=0x0ffff)  
        embed.add_field(name="Discord Name:", value=f" {member.mention}", inline=True)
        embed.add_field(name="Discord ID:", value=f" ```{member.id}```", inline=True)
        embed.add_field(name="Discord Bot?", value="```True```" if member.bot else "```False```", inline=True)
        embed.add_field(name="Top Role:", value=f"```{member.top_role.name}```", inline=True)
        embed.add_field(name="Role Amount:", value=f"```{len(member.roles)}```", inline=True)
        embed.add_field(name="Joined Server:", value=f'```{member.joined_at.strftime("%d/%m/%Y %H:%M:%S")}```', inline=False)
        embed.add_field(name="Account Created:", value=f'```{member.created_at.strftime("%d/%m/%Y %H:%M:%S")}```', inline=False)
        await ctx.send(embed=embed)   

bot.run("token (GET THIS FROM DISCORD DEVELOPER PORTAL > BOT > GENERATE TOKEN)") # [!] Required