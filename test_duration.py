from pytest import approx
import subprocess
import json
import myffmpeg.ffprobe as probe

def ffprobe(file) -> dict:
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    str(file)],universal_newlines=True)
    return json.loads(meta)

def test_duration():
    fnin = "./test_video.mp4"
    fnout = "./test_video.mp4_480.mp4"

    orig_meta = probe.ffprobe(fnin)
    orig_duration = float(orig_meta['streams'][0]['duration'])


    meta_480 = probe.ffprobe(fnout)
    duration_480 = float(meta_480['streams'][0]['duration'])

    assert round(orig_duration) == approx(round(duration_480))
