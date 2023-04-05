import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21124451"))
    API_HASH = os.environ.get("API_HASH", "d0c75e0e8ae1f79ddad10a033411f9ed")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6139871154:AAFnYgWu80lHB_JhwU8I_-frvNL5nH0fQWM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOH0BuwzxRbPSfgkQkVpcCbSU0eVFfRINfsWMPsysWTfrjvSPsDUxnrOsWfaG-YYPZBKWovfVMnhGYvII5LdlXNshZnsS3xxKt9fltnKf6Y3LwxayruVOXObFZF-t7FR0kiMG7gkTXdVOhVWaN1ObbeZU_jzQlI_wklSDKe9LduD3DMZfQvvC8ZoLphXEz6KwAoCI-qr0JlnmgtUmoGGeeDdkzR0ExKXUE_HDm07gX1c4o57NpqS_O5RzoSmTuyqg-IJm-QN4lzSj3APnPCZDjmySHfjxuomjPecCVp_aDU5c06BNzqSqyTR-xonbAdmG6Sqc_WVS061bSRDjdA13V8lCeaM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@USERTAGERMATHERBOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5986838562")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
