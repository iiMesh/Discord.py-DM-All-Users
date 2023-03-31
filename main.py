import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
	  print("Im Ready")

@client.command()
async def dm_all(ctx, *, message = None):
	  if message != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(message)
			      except:
                pass
	  else:
		  await ctx.send("Please provide an message!")

client.run(ODk1MzM0NDQ3MjY2Nzk1NTgy.Gsx4b7.sJEV-_i5ivv9qcr7NYsQXCKEUJcb5b1QxmCkzg)
