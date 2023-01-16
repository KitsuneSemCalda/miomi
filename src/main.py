#!/usr/bin/env python3

import argparse
import queue_controller


def setup_args():
    parse = argparse.ArgumentParser(
        prog="miomi",
        description="The little command line tool to download video/audio from youtube",
        epilog="Developed from KitsuneSemCalda",
        usage="%(prog)s [OPTIONS]:",
        )
    subparse = parse.add_subparsers(title="subcommands", description="subcommands for miomi", dest="subcommand")
    
    add_queue = subparse.add_parser("addqueue", description="subcommand to add a new url to queue")
    add_queue.add_argument("url")

    subparse.add_parser("clearqueue", description="subcommand to clean a queue file")
    download_queue = subparse.add_parser("downloadqueue", description="subcommand to download links in queue")
    download_queue.add_argument("mode", type=str, default="audio")
    return parse.parse_args()

def main():
    args = setup_args()
    if args.subcommand == "addqueue":
        queue_controller.incrementNewLink(queue_controller.filepath, args.url)
    if args.subcommand == "clearqueue":
        queue_controller.clearQueue(queue_controller.filepath)
    if args.subcommand == "downloadqueue":
        queue_controller.downloadQueue(queue_controller.filepath, args.mode)
    if args.subcommand == "seequeue":
        queue_controller.readQueue(queue_controller.filepath)

if __name__ == "__main__":
    main()
    pass
