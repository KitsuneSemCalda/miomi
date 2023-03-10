#!/usr/bin/env python3

import pytest
from main import setup_args


def test_setup_args():
    args = setup_args()
    assert args.prog == "miomi"
    assert args.description == "A youtube vídeo downloader and converter"
    assert args.usage == "%(prog)s [OPTIONS]:"
    assert args.epilog == "developed from KitsuneSemCalda"
