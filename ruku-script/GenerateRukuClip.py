# imports
import pathlib

from moviepy.editor import *

# ------------------------------
# directory structure should be:
# --- rukus-script/
# ----- GenerateRukuClip.py
# ----- videos/
# ----- audios/
# ----- images/
# ------------------------------
# absolute path of current directory
absolutePath = str(pathlib.Path().absolute())
ruku_vf = []  # ayah_list
FINAL_OUT_VID = "videos/final.mp4"  # out video file path
AYAH_FILE_NAME = ""
MP4 = ".mp4"


# Get Dynamic Buffer size based on number of frames
def get_buffer_size(nframes, ratio):
    return int(nframes * ratio)


#  Generate video file from audios and images
def generate_video(image_file, audio_file, ruku_number):
    global AYAH_FILE_NAME
    global FINAL_OUT_VID
    global ruku_vf
    AYAH_FILE_NAME = (audio_file.split('.'))[0]
    AYAH_FILE_NAME = AYAH_FILE_NAME + MP4
    FINAL_OUT_VID = absolutePath + '/videos/' + ruku_number + MP4
    # out_video_file = absolutePath + "/videos/" + out_file_name + ".mp4"
    # outfile = "final.mp4"
    image_file = absolutePath + "/images/" + image_file
    # image_file = "image.jpeg"
    audio_file = absolutePath + "/audios/" + audio_file
    # audio_file = "audio.mpeg"
    AYAH_FILE_NAME = absolutePath + "/ayah_videos/" + AYAH_FILE_NAME

    # read audio file
    audio = AudioFileClip(audio_file, nbytes=2, fps=44100)
    # Set Duration of audio to image
    image = ImageClip(image_file).set_duration(audio.duration)

    # Optional: Write Mp3
    # audio.write_audiofile("mp3/" + AYAH_FILE_NAME + ".mp3",
    #                       bitrate="192k",
    #                       nbytes=2)

    # set audio to image
    video = image.set_audio(audio)
    # append to list for concatenation
    ruku_vf.append(video)

    # # write single ayah video to file
    # video.write_videofile(AYAH_FILE_NAME,
    #                       fps=1,
    #                       audio_bitrate='192k',
    #                       audio_fps=44100,
    #                       audio_nbytes=2,
    #                       audio_codec="aac")


# main run
images_list = sorted(os.listdir('images'))
audio_list = sorted(os.listdir('audios'))
print("Total Image Files: " + str(len(images_list)))
print("Total Audio Files: " + str(len(audio_list)))
print(images_list)
print(audio_list)

# Reading Ruku Number file
ruku_file = open('ruku-info/2.txt')
ruku_list = list(ruku_file)
# ayah_n = []
for ruku in ruku_list:
    s = ruku.rstrip()
    ayah_n = s.split(" ")[1:]
    ruku_number = s.replace(' ', '')
    ruku_i = images_list[int(ayah_n[0]) - 1: int(ayah_n[1])]
    ruku_a = audio_list[int(ayah_n[0]) - 1: int(ayah_n[1])]
    if ruku_a == [] and ruku_i == []:
        break
    ruku_vf.clear()
    for i in range(len(ruku_a)):
        generate_video(ruku_i[i], ruku_a[i], ruku_number)
    # concat ruku aya list
    com_vid = concatenate_videoclips(ruku_vf)
    # write final ruku video to file
    com_vid.write_videofile(FINAL_OUT_VID,
                            fps=1,
                            audio_bitrate='192k',
                            audio_fps=44100,
                            audio_nbytes=2,
                            audio_codec="aac")
