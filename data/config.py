from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
BOT_TOKEN = "5809594635:AAF6FRFLU4d2yBxabyGhAh_2imqwfbtbD4E"
# print(BOT_TOKEN)
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
CHANNEL_ID=env.str("CHANNEL_ID")
# CHANNEL_ID=-1001867869015
CHANNEL_USERNAME=env.str("CHANNEL_USERNAME")
website_url=env.str("website_url")
web_app_url="https://mandat.uzbmb.uz/Home2023/Index"
port=env.str("port")
base_url=env.str("BASE_URL")
username=env.str("username")
password=env.str("password")
university_id=env.str("university_id")