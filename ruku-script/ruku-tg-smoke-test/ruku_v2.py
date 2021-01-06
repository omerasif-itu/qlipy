imgs = []
auds = []

# read images
with open('images.txt') as ims:
    images = ims.readlines()
    imgs = [img.strip('\n') for img in images]
    print(imgs)

# read audios
with open('audios.txt') as ads:
    audios = ads.readlines()
    auds = [ad.strip('\n') for ad in audios]
    print(auds)

# extract all audio files for each image file
dnc = [[a for a in auds if i in a] for i in imgs]
[print(i) for i in dnc]
