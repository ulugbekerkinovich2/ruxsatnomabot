from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
CHANNEL_ID=env.str("CHANNEL_ID")
CHANNEL_USERNAME=env.str("CHANNEL_USERNAME")
website_url=env.str("website_url")
web_app_url=env.str("web_app_url")
port=env.str("port")
base_url=env.str("BASE_URL")
username=env.str("username")
password=env.str("password")
university_id=env.str("university_id")