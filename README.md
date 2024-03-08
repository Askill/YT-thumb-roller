# YT-thumb-roller

Automatically rotate youtube thumbnails, if you're not VIP enough for youtube to grant you the ability.

## Prerequisite

Follow this guide to obtain youtube API access: https://developers.google.com/youtube/registering_an_application  
You need a GCP Account -> create a new project -> create a OAuth 2.0-Client for a Desktop Application (follow the guide above).   
This will give you the `client_id`, `project_id` and `client_secret` which you need to insert into `app/secrets.json` opr download as a json file, just overwrite the existing one.

## Setup and Usage

Start with running the script once manually, to setup your login information and install dependencies:

    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r app/requirements.txt
    python app/main.py anythinghere anythinghereaswell

In this step we only setup the login information, no need to provide a video_id or thumbnails, the script will fail with an error, but that is fine, as long as a new .pickle file was created. Otherwise repeat the steps above.

At this point you can test yoursetup on an unlisted video by running the following command, an absolute path to the directory containing the thumbnails is recommended:

    source venv/bin/activate && \
    python app/main.py <video_id> <path_to_thumbnails>

## Automate

Create a Cronjob to periodically update your thumbnail

        crontab -e
        # change the paths and variables and insert this line:
        1 * * * * * * source </path/to/project>/venv/bin/activate && python </path/to/project>/app/main.py <video_id> <path_to_video_thumbnails>

This example updates the thumbnail once an hour for the provided video for ever.
