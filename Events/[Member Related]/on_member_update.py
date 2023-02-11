@bot.event
async def on_member_update(before, after):
    if len(before.roles) > len(after.roles):
        role = next(role for role in before.roles if role not in after.roles) # Role Added to client
        note = f"**{role.name}** was removed from **{before.mention}**"

    elif len(after.roles) > len(before.roles):
        role = next(role for role in after.roles if role not in before.roles) # Role Removed from client
        note = f"**{role.name}** was added to **{before.mention}**"

    elif before.nick != after.nick: # Nickname was changed
        note = f"**{before.mention}** Nickname was set to ``{after.nick}`` from ``{before.nick}``"
    else:
        return
    print(note)