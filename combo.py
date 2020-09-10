# imports
import pathlib

from moviepy.editor import *

# ------------------------------
# directory structure should be:
# --- combine/
# ----- combo.py
# ----- videos/
# ----- audios/
# ----- images/
# ----- mp3/
# ------------------------------
# absolute path of current directory
absolutePath = str(pathlib.Path().absolute())
videos = []  # clips list
out_video_file = ""  # out video file path


# Get Dynamic Buffer size based on number of frames
def get_buffer_size(nframes, ratio):
    return int(nframes * ratio)


#  Generate video file from raw audios and images
def generate_video(image_file, audio_file):
    global out_video_file
    out_video_file_name = (audio_file.split('.'))[0]
    out_video_file = absolutePath + "/videos/" + out_video_file_name + ".mp4"
    # outfile = "final.mp4"
    image_file = absolutePath + "/images/" + image_file
    # image_file = "image.jpeg"
    audio_file = absolutePath + "/audios/" + audio_file
    # audio_file = "audio.mpeg"

    # read raw audio file
    audio = AudioFileClip(audio_file, nbytes=2, fps=44100)
    # Set Duration of audio to raw image
    image = ImageClip(image_file).set_duration(audio.duration)

    # Optional: Write Mp3
    audio.write_audiofile("mp3/" + out_video_file_name + ".mp3",
                          bitrate="192k",
                          nbytes=2,
                          buffersize=1000)  # fix issue for audio glitches.
    # set audio to raw image
    video = image.set_audio(audio)
    # append to list for concatenation
    videos.append(video)


# main run
images_list = sorted(os.listdir('images'))
audio_list = sorted(os.listdir('audios'))
print("Total Image Files: " + str(len(images_list)))
print("Total Audio Files: " + str(len(audio_list)))
print(images_list)
print(audio_list)

# generate video from raw audio and images
for i in range(len(audio_list)):
    generate_video(images_list[i], audio_list[i])

# concat video list
com_vid = concatenate_videoclips(videos)

# write final video to file
# Note: Buffer size is static.
# 1000 is used to fix audio glitches at the end of the clips.
com_vid.write_videofile(out_video_file,
                        fps=1,
                        audio_bitrate='192k',
                        audio_fps=44100,
                        audio_nbytes=2,
                        audio_codec="aac",
                        audio_bufsize=1000)  # fix issue for audio glitches.
