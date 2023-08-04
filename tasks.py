from robocorp.tasks import task
from robocorp import workitems, vault
import requests

@task
def transcribe_patient_record():

    hf_secret = vault.get_secret("Huggingface")
    headers = {
        "Authorization": f"Bearer {hf_secret['api-token']}",
        "Content-Type": "audio/flac",
    }

    for item in workitems.inputs:
        paths = item.download_files("*.flac")

        for path in paths:
            file = open(path, "rb")
            response = requests.post(hf_secret['whisper-url'], headers=headers, data=file)
            json_resp = response.json()
            print(f"AI SAYS: {json_resp['text']}")
            workitems.outputs.create(payload=json_resp)