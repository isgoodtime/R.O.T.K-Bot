import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("R.O.T.K Bot Start")
    game = discord.Game('R.O.T.K Bot 작동')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!탐사"):
        await message.channel.send("탐사는 다른 세계 즉, 웜홀을 찾아 다른 우주로 가는것입니다.\n다른 우주 공간에서 유물 사이트, 데이터 사이트, 등\n사이트들을 찾아 그 안에 있는 물품으로 돈을 벌수 있습니다.\n주의: 웜홀 안에 들어가면 CONCORD 가 있지 않습니다. 이 말은 즉 당신이 만약 다른 사람들에게 공격 받아도 아무도 안도와준다는 것 입니다. 꼭 디스캔을 보며 탐사를 하시길 바랍니다.\n(자세한 정보는 탐사부에서 얻으실수 있습니다.)")
    if message.content.startswith("!채광"):
        await message.channel.send("채광은 광물을 캐서 돈을 벌수 있습니다. 커나이트, 벨드스파, 등 여러가지 광물이 있으며\n또는 오메가만 캘수있는 아이스가 있습니다. 광물을 압축 시켜서 팔수도 있으며 함선, 무기, 등에 만드는데에 사용할수 있습니다.\n(자세한 정보는 채광부에 들어가셔서 더욱 아실수 있습니다.)")
    if message.content.startswith("!PVE"):
        await message.channel.send("PVE는 Player vs Environment 라는 뜻이며 즉 게임에 있는 적들과 싸우는 것입니다.\n이러한 컨텐츠는 랫질, 이머징, 데드, 어비셜, 미션, 등이 있습니다.\n(자세한 정보는 군사부에 들어가셔서 더욱 알수있습니다.)")
    if message.content.startswith("!PVP"):
        await message.channel.send("PVP는 Player vs Player 라는 뜻이며, 즉 다른 플레이어와 싸우는 것입니다.\nPVP는 전략, 대비, 등 바로바로 대처할 수 있는 능력이 있어야합니다.\n주의: 하이섹에서 다른 플레이어를 공격할시에 CONCORD 가 와서 공격합니다. (1.0 ~ 0.5)\n(자세한 정보는 로얄로더에 들어가시면 알수있습니다!)")
    if message.content.startswith("!산업"):
        await message.channel.send("산업은 블루플린트를 이용해서 함선, 무기, 등을 만듭니다.\n(자세한 정보는 산업부에서 얻으실수 있습니다.)")

client.run("NjYxMTkyMjMxNTIwMDQzMDM3.Xgn12Q.ODP8h0u9pVcwDAFHAA4fl-3YYo0")