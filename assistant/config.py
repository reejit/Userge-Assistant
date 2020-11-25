# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ["Config"]

import os

from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


class Config:
    """ assistant configs """
    APP_ID = int(os.environ.get("APP_ID", 0))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    AUTH_CHATS = set([l-1001382153442])  # @UserGeOt
    if os.environ.get("AUTH_CHATS"):
        AUTH_CHATS.update(map(int, os.environ.get("AUTH_CHATS").split()))
    WHITELIST_CHATS = set([-1001382153442])  # @UserGeSpam
    if os.environ.get("WHITELIST_CHATS"):
        WHITELIST_CHATS.update(map(int, os.environ.get("WHITELIST_CHATS").split()))
    DEV_USERS = (
        1205330619,  # @Krishna_Singhal
        1229057875,  # @PhycoNinja13b
        1083049180,   # @juznem
    )
    ADMINS = {}
    MAX_MSG_LENGTH = 4096
