#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7792141300:AAHMPlMIg4Ij9ni70L2soXx7n0cn5j8qDRw")
    API_ID = int(os.environ.get("API_ID", "27483529"))
    API_HASH = os.environ.get("API_HASH", "c3e9ea6320b861ad11e37c5260288bb3")
    AUTH_USERS = "1411895712"

