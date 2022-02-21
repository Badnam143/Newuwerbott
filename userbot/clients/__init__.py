# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

from .client_list import client_id, clients_list
from .logger import man_userbot_on
from .startup import man_client, multiman

ITSME = list(map(int, b64decode("ODQ0NDMyMjIw").split()))
