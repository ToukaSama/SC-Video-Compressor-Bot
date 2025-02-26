
from bot.get_cfg import get_config

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "7279728762:AAGOel3zhLLYa5x0v9EOFHmzjvDQ9dmgfV4")
    # The Telegram API things
    APP_ID = int(get_config("APP_ID", 20415731))
    API_HASH = get_config("ef85493cd32eadcb5309b5957d8d1b86")
     # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_USERS = set(
        int(x) for x in get_config(
            "6440021089",
            should_prompt=True
        ).split()
    )
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/DOWNLOADS")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 1572864000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 1572864000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "🟩")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "⬛")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
