import os
import asyncio
import queue



Q = queue.Queue()
path = 'the path where your video to be converted'
files = os.listdir(path)
async def convert_720p():
        while (True):
            if  Q.empty():
                await queue_proc()
            video = Q.get()
            os.system("./ffmpeg -i ./in/{} -b:v 2000k -bufsize 2000k -r 30  -strict -2 -s 1280x720 \
            ./out/{}_720p.mp4".format(video,video))
            os.system('ps - ef | grep python')
            return '720P coverted'





async def convert_480p():
        while(True):
            if  Q.empty():
                await queue_proc()
            video = Q.get
            os.system("./ffmpeg -i ./in/{} -b:v 1000k -bufsize 2000k -r 30  -strict -2 -s 720x480 \
            ./out/{}_480p.mp4".format(video,video))
            os.system('ps - ef | grep python')
            return '480P converted'

async def queue_proc():
    for file in files:
        Q.put(file)
async def main():
    coroutine1 = convert_720p()
    coroutine2 = convert_480p()
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(coroutine1),loop.create_task(coroutine2)]
    loop.run_until_complete(tasks)

    for task in tasks:
        print('Task: ', task.result())

