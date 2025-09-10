import discord
from discord import app_commands
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")
intents = discord.Intents.default()  # 必要な場合は intents.message_content = True なども追加
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
Guild = discord.Object(id=1405174680012193944)  # サーバID
@client.event
async def on_ready():
    server_count = len(client.guilds)
    status_message = f"{server_count} サーバーで活躍中！"
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=status_message)
    )
    print(f'{client.user} でログインしています')
    await tree.sync()
    print("コマンド同期完了")
# あいさつコマンド
@tree.command(name="hello", description="あいさつします")
async def hello_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.display_name}さん、こんにちは！")
# おみくじコマンド
@tree.command(name="fortune", description="おみくじ結果を表示します")
async def fortune_command(interaction: discord.Interaction):
    import random
    results = ["大吉", "中吉", "吉", "小吉", "末吉", "凶"]
    result = random.choice(results)
    await interaction.response.send_message(f"おみくじの結果は…『{result}』です！")
# 挨拶コマンド
@tree.command(name="greet", description="好きな名前で挨拶します")
@app_commands.describe(name="呼んでほしい名前")
async def greet_command(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"{name}さん、こんにちは！")
# 足し算コマンド
@tree.command(name="add", description="2つの数字を足します")
@app_commands.describe(a="最初の数字", b="次の数字")
async def add_command(interaction: discord.Interaction, a: int, b: int):
    result = a + b
    await interaction.response.send_message(f"{a} + {b} = {result}")
# コイントスコマンド
@tree.command(name="coin", description="コイントス!")
async def coin_command(interaction: discord.Interaction):
    import random
    side = random.choice(["表", "裏"])
    await interaction.response.send_message(f"コイントスの結果: {side}")
# ランダムカラーコードコマンド
@tree.command(name="randcolor", description="ランダムなカラーコードを教えます")
async def randcolor_command(interaction: discord.Interaction):
    import random
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    await interaction.response.send_message(f"ランダムカラー: {color}")
# 今日の日付コマンド
@tree.command(name="today", description="今日の日付を教えます")
async def today_command(interaction: discord.Interaction):
    from datetime import datetime
    now = datetime.now()
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    weekday = weekdays[now.weekday()]
    await interaction.response.send_message(f"今日は {now.strftime('%Y-%m-%d')}（{weekday}）です。")
# 特定ロール限定コマンド
@tree.command(name="secret", description="特定ロール限定のコマンド")
async def secret_command(interaction: discord.Interaction):
    # '管理者'ロールがあるかチェック
    if any(role.name == "管理者" for role in interaction.user.roles):
        await interaction.response.send_message("特別なメッセージ！")
    else:
        await interaction.response.send_message("あなたには権限がありません。", ephemeral=True)
# メンバー数表示コマンド
@tree.command(name="members", description="サーバーのメンバー数を表示します")
async def members(interaction: discord.Interaction):
    num = interaction.guild.member_count
    await interaction.response.send_message(f"このサーバーのメンバー数は{num}人です")
# ヘルプコマンド
@tree.command(name="help", description="Botコマンド一覧を表示します")
async def help_command(interaction: discord.Interaction):
    lines = ["**Botコマンド一覧**"]
    for cmd in tree.get_commands():
        params = ""
        if cmd.parameters:
            params = " " + " ".join(f"{p.display_name}: {p.description or '引数'}" for p in cmd.parameters)
        lines.append(f"/{cmd.name}{params} - {cmd.description}")
    await interaction.response.send_message("\n".join(lines))
#サイコロコマンド
@tree.command(name="dice", description="1から6のサイコロを振ります")
async def dice_command(interaction: discord.Interaction):
    import random
    num = random.randint(1, 6)
    await interaction.response.send_message(f"サイコロの目は {num} です！")
    # roll
@tree.command(name="roll", description="NdM形式で多面ダイスを振ります（例：2d6）")
@app_commands.describe(ndm="NdM形式（例: 2d6, 1d20 など）")
async def roll_command(interaction: discord.Interaction, ndm: str):
    import re
    import random
    # 正規表現で「数字d数字」を抜き出す
    match = re.fullmatch(r"(\d{1,3})[dD](\d{1,3})", ndm.strip())
    if not match:
        await interaction.response.send_message("NdM形式で入力してね！（例: 2d6, 1d20）", ephemeral=True)
        return
    n, m = int(match.group(1)), int(match.group(2))
    if n < 1 or m < 2 or n > 100 or m > 1000:
        await interaction.response.send_message("個数1-100、面数2-1000の範囲で指定してください", ephemeral=True)
        return
    rolls = [random.randint(1, m) for _ in range(n)]
    total = sum(rolls)
    results = ", ".join(map(str, rolls))
    msg = f"{n}d{m}の出目: [{results}] 合計: {total}"
    await interaction.response.send_message(msg)
# user-info
@tree.command(name="userinfo", description="あなたのDiscordユーザー情報を表示します")
async def userinfo(interaction: discord.Interaction):
    user = interaction.user
    text = (
        f"【ユーザー情報】\n"
        f"名前: {user.display_name}\n"
        f"ID: {user.id}\n"
        f"アカウント作成日: {user.created_at.strftime('%Y-%m-%d')}"
    )
    await interaction.response.send_message(text)
# じゃんけんコマンド
@tree.command(name="janken", description="じゃんけんをします")
@app_commands.describe(choice="あなたの選択（グー、チョキ、パー）")
async def janken_command(interaction: discord.Interaction, choice: str):
    import random
    choices = ["グー", "チョキ", "パー"]
    if choice not in choices:
        await interaction.response.send_message("選択はグー、チョキ、パーのいずれかでお願いします。", ephemeral=True)
        return
    bot_choice = random.choice(choices)
    result = ""
    if choice == bot_choice:
        result = "引き分け！"
    elif (choice == "グー" and bot_choice == "チョキ") or \
        (choice == "チョキ" and bot_choice == "パー") or \
        (choice == "パー" and bot_choice == "グー"):
        result = "あなたの勝ち！"
    else:
        result = "あなたの負け！"
    await interaction.response.send_message(f"あなたの選択: {choice}\nBotの選択: {bot_choice}\n結果: {result}")
    # aboutコマンド
@tree.command(name="about", description="このBotの概要・説明を表示します")
async def about_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📋 Discord Bot Sample について",
        description="**Python + discord.py（v2.x）で作られたサンプルDiscord Bot**",
        color=0x00FF7F
    )
    
    # プロジェクト概要
    embed.add_field(
        name="🎯 プロジェクトの趣旨",
        value="Discord.pyを学習したい方、Bot開発の参考にしたい方に向けた\n教育・学習目的のサンプルコードです。",
        inline=False
    )
    
    # 主要コマンド
    embed.add_field(
        name="🔥 主なコマンド",
        value="• `/hello` - あいさつ\n• `/fortune` - おみくじ\n• `/greet [名前]` - カスタム挨拶\n• `/add [a] [b]` - 計算機能\n• `/dice` - サイコロ\n• `/janken [選択]` - じゃんけん\n• `/userinfo` - ユーザー情報\n• `/help` - 全コマンド一覧",
        inline=False
    )
    
    # 技術情報
    embed.add_field(
        name="⚙️ 技術スタック",
        value="• Python 3.8+\n• discord.py 2.x\n• python-dotenv\n• スラッシュコマンド対応",
        inline=True
    )
    
    # リンク情報
    embed.add_field(
        name="🔗 プロジェクトリンク",
        value="[📂 GitHub Repository](https://github.com/gamesken29suki/discord-bot-sample)\n[📖 Wiki・ドキュメント](https://github.com/gamesken29suki/discord-bot-sample/wiki)\n[🐛 Issues・要望](https://github.com/gamesken29suki/discord-bot-sample/issues)",
        inline=True
    )
    
    # リリース情報
    embed.add_field(
        name="🆕 最新リリース",
        value="**v1.0.0** - 初回リリース\n2025/09/10 リリース済み\n[📦 リリース詳細](https://github.com/gamesken29suki/discord-bot-sample/releases/tag/v1.0.0)",
        inline=False
    )
    
    # フッター
    embed.set_footer(text="💡 開発・要望はGitHub Issues/PRでお気軽に！ | MIT License")
    
    await interaction.response.send_message(embed=embed)
    # pingコマンド
@tree.command(name="ping", description="Botの応答速度を表示します")
async def ping_command(interaction: discord.Interaction):
    # レイテンシはClient.latency（秒）で取得、そのままms化！
    latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong! 応答速度: {latency} ms")
# その他のコマンドも同様に追加可能
@client.event
async def on_guild_join(guild):
    await tree.sync(guild=Guild)
# サーバー参加時にコマンドを同期
@client.event
async def on_guild_remove(guild):
    print(f"Left guild: {guild.name}")
client.run(token)
