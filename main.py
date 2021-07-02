import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.', help_command=None)
embed = discord.Embed()

#---------------------------------------------------------------------------

@client.command()
@commands.has_any_role('CSDBWI')
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)

#---------------------------------------------------------------------------

@client.command()
@commands.has_any_role('🔧 Moderator')
async def ban(ctx, member:discord.Member, *, reason):
    await member.ban(reason = reason)
    await ctx.send(f'{ctx.author} banned {member}.')

@client.command()
@commands.has_any_role('🔧 Moderator')
async def kick(ctx, member:discord.Member, *, reason):
    await member.kick(reason = reason)
    await ctx.send(f'{ctx.author} kicked {member}.')

@client.command()
@commands.has_any_role('🔧 Moderator')
async def mute(ctx, member: discord.Member):
    await member.add_roles(discord.utils.get(ctx.guild.roles, name='Muted'))

@client.command()
@commands.has_any_role('🔧 Moderator')
async def unmute(ctx, member: discord.Member):
    await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))

#---------------------------------------------------------------------------

@client.command()
async def report(ctx, member: discord.Member, *, reason):
    report = client.get_channel(856870848212369448)
    embed.add_field(name='User', value=member, inline=False)
    embed.add_field(name='Reason', value=reason, inline=False)
    embed.add_field(name='Reported by', value=ctx.author, inline=False)
    await report.send(embed=embed)

#---------------------------------------------------------------------------

client.run(TOKEN)
