from moviepy.editor import *

basedir = "videos/"
rFILENAME = "sunhorns.mp4"
oFILENAME = "looped.mp4"
LOOP = 2
audios_loop = []
v = VideoFileClip(os.path.join(basedir, rFILENAME), audio=False)
vl = v.fx(vfx.loop, duration=v.duration + 5.0)
# for x in range(0, LOOP):
#     audios_loop.append(v.audio)
# fina = concatenate_audioclips(audios_loop)
# vl.audio.write_audiofile(str(os.path.join(basedir, "loop.mp3")))
# vl.audio.duration = vl.duration
# vl.audio.end = vl.end
# vl.audio.reader.duration = vl.audio.duration
# vl.audio.reader.end = vl.audio.end
# vl.audio = fina
vl.write_videofile(os.path.join(basedir, oFILENAME))
