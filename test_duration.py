from pytest import approx
import subprocess
import json
from pathlib import Path



def ffprobe(file: Path) -> dict:
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                   file],universal_newlines=True)
    return json.loads(meta)

def test_duration():
    #fnin = "C:/Users/96171/PycharmProjects/exercise2_ec500/test_video.mp4"
    #fnout = "C:/Users/96171/PycharmProjects/exercise2_ec500/test_video.mp4_480.mp4"
    fnin = "test_video.mp4"
    fnout = "test_video.mp4_480.mp4"

    original_meta = ffprobe(fnin)
    orig_duration = float(original_meta['streams'][0]['duration'])

    meta_480 = ffprobe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])

    assert round(orig_duration) == approx(round(duration_480))

