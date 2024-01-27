import twitterbot as tb
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
username = os.getenv("USERNAME")

bot = tb.Twitterbot(email, password, username)
bot.login()
bot.goToBookMarks()