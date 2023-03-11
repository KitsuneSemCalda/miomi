#!/usr/bin/env python3

import argparse
import logging

from video.downloader import download_video

def setup_args():
    parse = argparse.ArgumentParser(
            prog="miomi",
            description="A youtube vídeo downloader and converter",
            usage="%(prog)s [OPTIONS]:",
            epilog="developed from KitsuneSemCalda"
    )
    
    video_group = parse.add_argument_group("Vídeo options")
    video_group.add_argument(
        "--video",
        "-v",
        help="Download the vídeo from the specified Youtube URL",
        metavar="URL"
    )

    video_group.add_argument(
        "--resolution",
        "-r",
        choices=["240p", "360p", "480p", "720p", "1080p"],
        default="720p",
        help="Set the resolution of the vídeo",
        metavar="RESOLUTION"
    )

    audio_group = parse.add_argument_group("Audio options")
    audio_group.add_argument(
        "--audio",
        "-a",
        help="Download the audio from the specified Youtube URL",
        metavar="URL"
    )

    audio_group.add_argument(
        "--format",
        "-f",
        choices=["mp3","wav", "m4a"],
        default="wav",
        help="Set the audio format (default: wav)",
        metavar="FORMAT"
    )

    return parse


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('download.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    args = setup_args().parse_args()
    if args.video:
        download_video(args.video, args.resolution)
    pass
