import time
from youtube import *
from test_data.gen_test_data import gen_img


while True:
    gen_img()

    youtube = get_authenticated_service()
    video_id = "x2JOWQu-4Jc"
    tn_path = "C:/projects/yt_thumb_roller/app/test_data/output"
    set_thumbnail(youtube, video_id, tn_path)
    time.sleep(1800)