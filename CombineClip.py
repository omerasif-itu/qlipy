import glob

from moviepy.editor import *

# Place Videos in this Folder, video names must be sorted!

path = r''  # use your path
video_list = glob.glob("./*.mp4")
clips = []
audios = []
total_nframes = -1
print(video_list)
for i in range(len(video_list)):
    a = AudioFileClip(video_list[i], fps=44100, nbytes=2)
    buffer = int(a.reader.nframes * 0.05)
    total_nframes += a.reader.nframes
    audios.append(a)
    v = VideoFileClip(video_list[i], audio=True, fps_source='fps')
    # a.__setattr__('buffersize', buffer)
    # a.buffersize = buffer
    # a.reader.buffersize = buffer
    # a.duration = a.duration-1
    # a.end =a.duration
    # v.duration = a.duration-1
    # v.end = v.duration
    # v.audio = a
    # v.duration = round(v.duration)
    print(v)
    v.write_videofile("pro/" + video_list[i], fps=1, audio_bitrate='192k', audio_fps=44100, audio_nbytes=2,
                      audio_codec="aac")
    clips.append(v)
print(len(clips))
print(len(audios))
print(total_nframes)
# audio = concatenate_audioclips(audios)
# buffer = int(total_nframes * 0.01)
# buffer2 = 10000
# audio.write_audiofile("audiofinal" + ".mp3", fps=44100, bitrate="192k", nbytes=2, buffersize=buffer)
# final_clip = concatenate_videoclips(clips)
# final_clip.write_videofile("Surah_al_Baqarah_Part-2.mp4", fps=1, audio_bitrate='192k', audio_codec="aac",
#                            audio_bufsize=buffer)

final = concatenate_videoclips(clips)
final.write_videofile("pro/test.mp4",
                      fps=1,
                      audio_codec="aac",
                      audio_nbytes=2,
                      audio_bitrate="192k",
                      audio_fps=44100)
