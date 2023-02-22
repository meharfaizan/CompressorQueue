#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID",'6534707' default=6, cast=int)
    API_HASH = config("API_HASH",'4bcc61d959a9f403b2f20149cbbe627a')
    BOT_TOKEN = config("BOT_TOKEN",'5142296427:AAGe28CHWVme4OJ4v51xxqvNbnPwD8vxQic')
    DEV = 1322549723
    OWNER = config("OWNER",'1430593323')
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset fast -c:v libx264 -crf 28 -map 0:v -c:a libopus -c:s copy -map 0"{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
