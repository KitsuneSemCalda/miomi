#!/usr/bin/env python3

import argparse
import queuefile


def setup_args():
    parse = argparse.ArgumentParser(
        prog="miomi",
        description="The little command line tool to download video/audio from youtube",
        epilog="Developed from KitsuneSemCalda",
        usage="%(prog)s [OPTIONS]:",
        )
    subparse = parse.add_subparsers(
            title="subcommands", 
            description="subcommands for miomi", 
            dest="subcommand")
    
    add_queue = subparse.add_parser(
            "add", 
            description="add a new youtube url to the download queue")

    add_queue.add_argument("url", help="The URL of the video or playlist to add the queue")

    subparse.add_parser(
            "clear", 
            description="Clears the download queue")
    
    subparse.add_parser("see", 
                        description="See the current download queue")
    
    subparse.add_parser("persistent", description="save list of url in Documents folder")

    download_queue = subparse.add_parser("downloadqueue", 
                                         description="download all itens in the queue")
    
    download_queue.add_argument("mode", type=str, default="audio", help="The download mode, either 'audio' or 'video'")
    
    download = subparse.add_parser("download", description="Directly download a Youtube video or playlist")
    download.add_argument("url", help="The url of the youtube video or playlist to download")
    download.add_argument("mode", type=str, default="audio", help="The download mode, either 'audio' or 'video'")

    return parse.parse_args()

def main():
    args = setup_args()
    try:
        if args.subcommand == "add":
            queuefile.incrementNewLink(queuefile.filepath, args.url)
        if args.subcommand == "clear":
            queuefile.clearQueue(queuefile.filepath)
        if args.subcommand == "downloadqueue":
            queuefile.downloadQueue(queuefile.filepath, args.mode)
        if args.subcommand == "download":
            queuefile.download(args.url, args.mode)
        if args.subcommand == "see":
            queuefile.readQueue(queuefile.filepath)
        if args.subcommand == "persistent":
            queuefile.persistent()
    except argparse.ArgumentError:
        pass
    

if __name__ == "__main__":
    main()
    pass
