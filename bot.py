import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="mitoko ")

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Listen to staff please!"))

mod_role_id = 'role id here'

@bot.command()
@commands.has_role(item = mod_role_id)
async def warn(ctx, member : discord.Member, *, reason=None):
    mem = str(member)
    embed = discord.Embed(title="你被管理员警告了", description="You got warned from moderators", color=discord.Color.red())
    embed.set_author(name=mem+" has been warned from moderators", icon_url=member.avatar_url)
    embed.add_field(name="原因 / Reason", value=reason, inline=True)
    embed.set_footer(text="请自行翻译英文原因 / Please translate the reason if it wrote in Chinese")
    await ctx.send(embed = embed)
    channel = await member.create_dm()
    await channel.send(embed = embed)

@bot.command()
@commands.has_role(item = mod_role_id)
async def kick(ctx, member : discord.Member, *, reason=None):
    mem = str(member)
    embed = discord.Embed(title="你被管理员给予了一张飞机票", description="You got kicked from moderators", color=discord.Color.red())
    embed.set_author(name=mem+" has been kicked from moderators", icon_url=member.avatar_url)
    embed.add_field(name="原因 / Reason", value=reason, inline=True)
    embed.set_footer(text="请自行翻译英文原因 / Please translate the reason if it wrote in Chinese")
    await ctx.send(embed = embed)
    channel = await member.create_dm()
    await channel.send(embed = embed)
    await member.kick(reason=reason)

@bot.command()
@commands.has_role(item = mod_role_id)
async def ban(ctx, member : discord.Member, *, reason=None):
    mem = str(member)
    embed = discord.Embed(title="你被管理员给予了一张单程飞机票", description="You got banned from moderators", color=discord.Color.red())
    embed.set_author(name=mem+" has been banned from moderators", icon_url=member.avatar_url)
    embed.add_field(name="原因 / Reason", value=reason, inline=True)
    embed.set_footer(text="请自行翻译英文原因 / Please translate the reason if it wrote in Chinese")
    await ctx.send(embed = embed)
    channel = await member.create_dm()
    await channel.send(embed = embed)
    await member.ban(reason=reason)

@bot.command()
@commands.has_role(item = mod_role_id)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} have been unbanned sucessfully")
    return

@bot.command()
@commands.has_role(item = mod_role_id)
async def mute(ctx, member : discord.Member, *, reason=None):
    mem = str(member)
    embed = discord.Embed(title="你被管理员给予了一张禁言卡", description="You got muted from moderators", color=discord.Color.red())
    embed.set_author(name=mem+" has been muted from moderators", icon_url=member.avatar_url)
    embed.add_field(name="原因 / Reason", value=reason, inline=True)
    embed.set_footer(text="请自行翻译英文原因 / Please translate the reason if it wrote in Chinese")
    await ctx.send(embed = embed)
    channel = await member.create_dm()
    await channel.send(embed = embed)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    user = member
    await user.add_roles(role)

@bot.command()
@commands.has_role(item = mod_role_id)
async def unmute(ctx, member : discord.Member):
    mem = str(member)
    embed = discord.Embed(title="你被管理员取消禁言了", description="You got unmuted from moderators", color=discord.Color.red())
    embed.set_author(name=mem+" has been unmuted from moderators", icon_url=member.avatar_url)
    embed.set_footer(text="希望您改正错误，重新做更好的自己 / Hope you correct your mistakes and become a better version of yourself")
    await ctx.send(embed = embed)
    channel = await member.create_dm()
    await channel.send(embed = embed)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    user = member
    await user.remove_roles(role)
    

bot.run("token")