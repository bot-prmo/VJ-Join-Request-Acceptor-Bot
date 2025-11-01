from os import environ

API_ID = int(environ.get("23231578", ""))
API_HASH = environ.get("6016ef2dc043865f26667d89719b2c7e", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("-1003021119809", ""))
ADMINS = int(environ.get("6960971297", ""))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("mongodb+srv://Phxpardeep233:phx11234@cluster0.oykmvgo.mongodb.net/?appName=Cluster0", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "TeleApproveBot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
