#!/usr/bin/env python3

import pytest
from main import setup_args


def test_setup_args():
    args = setup_args()
    assert args.prog == "miomi"
    assert args.description == "A youtube vídeo downloader and converter"
    assert args.usage == "%(prog)s [OPTIONS]:"
    assert args.epilog == "developed from KitsuneSemCalda"

def test_all_parameters():
    args = setup_args()
    assert args.parse_args(["--video", "https://www.youtube.com/watch?v=VIDEO_ID"]).video == "https://www.youtube.com/watch?v=VIDEO_ID"
    assert args.parse_args(["--resolution", "720p"]).resolution == "720p"
    assert args.parse_args(["--audio", "https://www.youtube.com/watch?v=VIDEO_ID"]).audio == "https://www.youtube.com/watch?v=VIDEO_ID"
    assert args.parse_args(["--format", "wav"]).format == "wav"

