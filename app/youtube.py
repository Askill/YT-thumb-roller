import os
import pickle

import google_auth_oauthlib.flow
import googleapiclient.discovery
from google.auth.transport.requests import Request

from helper import get_next_tn


def get_authenticated_service():
    scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.upload"]
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "app/secrets.json"
    if os.path.exists("CREDENTIALS_PICKLE_FILE"):
        with open("CREDENTIALS_PICKLE_FILE", 'rb') as f:
            credentials = pickle.load(f)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_local_server()
        if credentials.expired:
            credentials.refresh(Request())
        with open("CREDENTIALS_PICKLE_FILE", 'wb') as f:
            pickle.dump(credentials, f)
    return googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

def set_thumbnail(youtube, video_id, thumbnail_dir):
    tn_path = get_next_tn(thumbnail_dir)
    if tn_path is None:
        return None
    thumbnail_response = youtube.thumbnails().set(
        videoId=video_id,
        media_body=tn_path,
    ).execute()
    return thumbnail_response

