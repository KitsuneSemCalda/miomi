import argparse

def setup_args():
    parse = argparse.ArgumentParser(
        prog="miomi",
        description="The little command line tool to download video/audio from youtube",
        epilog="Developed from KitsuneSemCalda",
        usage="%(prog)s [OPTIONS]:",
        )
    return parse.parse_args()

def main():
    setup_args()

if __name__ == "__main__":
    main()
    pass
