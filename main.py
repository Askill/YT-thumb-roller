from youtube import get_authenticated_service, set_thumbnail
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Change youtube thumbnails automatically')

    parser.add_argument('video_id', metavar='video_id', type=str,
                        help='id of the video you want to change the thumbnail of')
    parser.add_argument('tn_path', metavar='tn_path', type=str,
                        help='path containing thumbnails')
    args = parser.parse_args()

    youtube = get_authenticated_service()
    video_id = args.video_id
    tn_path = args.tn_path
    set_thumbnail(youtube, video_id, tn_path)
