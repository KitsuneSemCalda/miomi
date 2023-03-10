#!/usr/bin/env python3

import argparse

def setup_args():
    parse = argparse.ArgumentParser(
            prog="miomi",
            description="A youtube vídeo downloader and converter",
            usage="%(prog)s [OPTIONS]:",
            epilog="developed from KitsuneSemCalda"
    )

    return parse


if __name__ == "__main__":
    args = setup_args().parse_args()
    pass
