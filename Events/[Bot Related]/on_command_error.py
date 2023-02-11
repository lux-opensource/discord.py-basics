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
