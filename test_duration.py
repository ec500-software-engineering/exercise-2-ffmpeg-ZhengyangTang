import subprocess
import json
from pathlib import Path
from pytest import approx

def ffprobe_tang(file: Path) -> dict:
    meta1 = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format',
                                         'json', '-show_streams', '-show_format', file],
                                        universal_newlines = True)
    return json.loads(meta1)

def test_duration():

    original_meta = ffprobe_tang('test_video.mp4')
    t480_meta = ffprobe_tang('test_video.mp4_480.mp4')

    duration = float(original_meta['streams'][0]['duration'])
    t480_duration = float(t480_meta['streams'][0]['duration'])
   
    assert duration == approx(t480_duration)

