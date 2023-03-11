import os
import pytest, pytube
from unittest.mock import patch
from video.downloader import download_video

@pytest.mark.parametrize("url,resolution", [
    ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "720p"),
    ("https://www.youtube.com/watch?v=EvuL5jyCHOw", "360p")
])
def test_download_video(url, resolution):
    video = pytube.YouTube(url)

    with patch('builtins.input', return_value="s"):
        download_video(url, resolution)

    expected_path = os.path.join(os.path.expanduser("~"), "Vídeos", f"{video.title}.mp4")
    assert os.path.exists(expected_path)
