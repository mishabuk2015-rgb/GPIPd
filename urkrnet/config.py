import os

from dotenv import load_dotenv

load_dotenv()


TOKEN_UKR_NET = os.getenv('TOKEN_UKR_NET')
USER_UKR_NET = os.getenv('USER_UKR_NET')
SMTP_SERVER = os.getenv('SMTP_SERVER')

print(SMTP_SERVER, USER_UKR_NET)
print(TOKEN_UKR_NET)