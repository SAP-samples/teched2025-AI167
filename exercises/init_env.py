import os
import json

import variables as variables

ROOT_PATH_DIR = os.path.dirname(os.getcwd())
AICORE_CONFIG_FILENAME = '.aicore-config.json'
OBJECTSTORE_CONFIG_FILENAME = '.objectstore-config.json'
OBJECTSTORE_CONFIG_PATH = os.path.join(ROOT_PATH_DIR, OBJECTSTORE_CONFIG_FILENAME)

# If file does not exist, do nothing

def set_environment_variables() -> None:
    with open(os.path.join(ROOT_PATH_DIR, AICORE_CONFIG_FILENAME), 'r') as config_file:
        config_data = json.load(config_file)

    os.environ["AICORE_AUTH_URL"]=config_data["url"]+"/oauth/token"
    os.environ["AICORE_CLIENT_ID"]=config_data["clientid"]
    os.environ["AICORE_CLIENT_SECRET"]=config_data["clientsecret"]
    os.environ["AICORE_BASE_URL"]=config_data["serviceurls"]["AI_API_URL"]

    os.environ["AICORE_RESOURCE_GROUP"]=variables.RESOURCE_GROUP


    # Object store (optional)
    if os.path.exists(OBJECTSTORE_CONFIG_PATH) and os.path.isfile(OBJECTSTORE_CONFIG_PATH):
        try:
            with open(OBJECTSTORE_CONFIG_PATH, 'r') as obj_file:
                obj_config = json.load(obj_file)
            # Example: set extra env vars if present
            if "access_key_id" in obj_config:
                os.environ["ACCESS_KEY_ID"] = obj_config["access_key_id"]
            if "uri" in obj_config:
                os.environ["URI"] = obj_config["uri"]
            if "secret_access_key" in obj_config:
                os.environ["SECRET"] = obj_config["secret_access_key"]
            if "bucket" in obj_config:
                os.environ["BUCKET"] = obj_config["bucket"]
            if "username" in obj_config:
                os.environ["USER"] = obj_config["username"]
        except (OSError, json.JSONDecodeError):
            pass

