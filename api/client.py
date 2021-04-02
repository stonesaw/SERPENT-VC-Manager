import os
from dotenv import load_dotenv
import discord

load_dotenv(override=True)

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
    # if (before.channel != after.channel):
    alert_channel = client.get_channel(713955978965680148)
    
    if before.channel is None:
        embed = discord.Embed(title=f"{member.name}が {after.channel.name} に参加しました",description="やっほー",color=0xff0000)
        embed.set_thumbnail(url=member.avatar_url)
        await alert_channel.send(embed=embed)
    elif after.channel is None:
        embed = discord.Embed(title=f"{member.name}が {before.channel.name} から抜けました",description="バイバイ",color=0xff0000,)
        embed.set_thumbnail(url=member.avatar_url)
        await alert_channel.send(embed=embed)

client.run(os.environ.get("DISCORD_TOKEN"))
