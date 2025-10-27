
import os, json
from ai_core_sdk.ai_core_v2_client import AICoreV2Client
import requests
import variables
import init_env

def extract_deployment_url():
    # instantiate client (do NOT set client-level resource_group to avoid tenant-scope conflicts)
    init_env.set_environment_variables()
    
    client = AICoreV2Client(
        base_url=os.environ["AICORE_BASE_URL"] + "/v2",
        auth_url=os.environ["AICORE_AUTH_URL"],
        client_id=os.environ["AICORE_CLIENT_ID"],
        client_secret=os.environ["AICORE_CLIENT_SECRET"],
    )

    url = f"{client.rest_client.base_url}/lm/deployments"
    headers = {
        "Authorization": client.rest_client.get_token(),
        "AI-Tenant-Scope": "false",
        "AI-Resource-Group": variables.RESOURCE_GROUP
    }

    resp = requests.get(url, headers=headers)
    data = resp.json()
    if isinstance(data, dict):
        # data['resources'] -> list of resources
        for key in ("resources", "items"):
            if key in data and isinstance(data[key], list):
                for r in data[key]:
                    if isinstance(r, dict) and r.get("deploymentUrl"):
                        return r["deploymentUrl"]
        if data.get("deploymentUrl"):
            return data["deploymentUrl"]
    if isinstance(data, list):
        for it in data:
            if isinstance(it, dict) and it.get("deploymentUrl"):
                return it["deploymentUrl"]
    raise KeyError("deploymentUrl not found")
