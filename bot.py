import discord
from discord.ext import commands
from config import token  # Botun tokenini config dosyasından içe aktarma
import random

intents = discord.Intents.default()
intents.members = True  # Botun kullanıcılarla çalışmasına ve onları banlamasına izin verir
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')

@bot.command()
async def start(ctx):
    await ctx.send("Merhaba! Ben bir sohbet yöneticisi botuyum!")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None):
    if member:
        if ctx.author.top_role <= member.top_role:
            await ctx.send("Eşit veya daha yüksek rütbeli bir kullanıcıyı banlamak mümkün değildir!")
        else:
            await ctx.guild.ban(member)
            await ctx.send(f"Kullanızı {member.name} banlandı")
    else:
        await ctx.send("Bu komut banlamak istediğiniz kullanıcıyı işaret etmelidir. Örneğin: `!ban @user`")

@bot.command()
async def hikaye(ctx):
    await ctx.send("Basketbol hikayemiz için takım,numara ve insanların sizi nasıl anması istediğinizi belirtiniz!")

@bot.command()
async def basla(ctx,t1,a1):
    draftyil=[2024,2025,2026,2027]
    drafttur=["1.","2."]
    draftsirasi=["1.","2.","10.","35."]
    xy=random.choice(draftyil)
    xd=random.choices(drafttur,weights=[35,65])[0]
    xs=random.choices(draftsirasi,weights=[15,13,30,42])[0]
    await ctx.send(f'{a1} {xy} yılında {t1} tarafından {xd} turdan {xs} sıradan draft edilmiştir')

@bot.command()
async def devam(ctx,t1,a1):
    po="Point Guard(Oyun Kurucu)"
    po2="Pivot"
    await ctx.send(po)
    await ctx.send(po2)
    tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    kullanici_tahmini = tahmin_mesaji.content
    if kullanici_tahmini==po2:
        await ctx.send("Kariyerin hiç parlak değil ligdeki pivotlara göre kısa ve yeteneksizsin bu yüzden takımın seni kadro dışı bıraktıktan sonra diğer takımlar seni istemedi ve sen Euorleugae transfer oldun ")
    if kullanici_tahmini==po:
        sl="İçeriye girdin ve kendine pozisyonlar üretmeye çalıştın "
        sl2="Setlere uyup takımla haraket ettin"
        await ctx.send(sl)
        await ctx.send(sl2)
        tm = await bot.wait_for("message", check=lambda x: x.author == ctx.author)
        kh = tm.content
        if kh==sl2:
            await ctx.send("Yaz liginde kendini göstermek için set oynadın ve kariyerin boyunca yedek ve ya kadro dışı kaldın")
        elif kh==sl:
            await ctx.send("Çok iyi iş çıkardın 22 pt 10 asist ve takımın 6. adamı oldun")
            await ctx.send("           ***************************          ")
            await ctx.send("İlk maçın başlamak üzere")
            await ctx.send("           ***************************          ")
            await ctx.send(f'Son periodun son dakikaları ve 32 sayısı ile {a1} tekrardan oyuna giriyor ')
            await ctx.send(f'{t1} mola aldı son 3 saniye Lakers {t1}e karşı 2 sayı önde ve top {a1} elinde 3!!!,2!!!!')
            tm2 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            kh2 = tm2.content
            k="Heyecan yap"
            k1="Soğuk kanlılığını korudun"
            await ctx.send(k)
            await ctx.send(k1)
            if kh2==k:
                await ctx.send("Senin yüzünden maçı kaybettiler ve koçla kavga ettin bu yüzden kadro dışı kaldın")
            if kh2==k1:
                await ctx.send(f'son 1 ve {a1} üçlüğü attı ve {t1} maçı kazındı')
                await ctx.send("           ***************************          ")
                await ctx.send("Artık ilk 5 oyuncusu oldun ")
                await ctx.send("           ***************************          ")
                await ctx.send("Bu sezon takımın için çok iç açıçı değil fakat sen çok iyi iş çıkardın")
                await ctx.send("           ***************************          ")
                await ctx.send("Ailen sana baskı yapıyo oğlum artık evlen diyorlar")
                e="Evlen"
                e1="Evlenme"
                await ctx.send(e)
                await ctx.send(e1)
                tm3 = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
                kh3 = tm3.content
                if kh3==e:
                    await ctx.send("Evlenip çoluk çocuğa karıştın ve kariyerin bitti ")
                if kh3==e1:
                    await ctx.send("Evlenmeyerek doğru karar verdin")
                    await ctx.send("           ***************************          ")
                    await ctx.send("Yeni bir mailin var")
                    await ctx.send("NEEEEEEEEE ..... takımdan takas teklifi mi")
                    await ctx.send("........................DEVAM EDİCEK........................")
            else:
                print("Hata")
        else:
            print("hata")
    else:
        print("hata")















@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komutu çalıştırmak için yeterli izniniz yok.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Kullanıcı bulunamadı!")

bot.run(token)
