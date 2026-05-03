from pytubefix import YouTube

url = "YourYTVideoUrl"

video = YouTube(url)

eng_subtitle = None
try:
    for available_subtitle in video.captions:
        if "en" in available_subtitle.code:
            eng_subtitle = available_subtitle.code
            break

except Exception as e:
    print("Не удалось достучаться до видео")
    exit(1)

captions = None
if eng_subtitle is not None:
    captions = video.captions[eng_subtitle].generate_txt_captions()
    if captions is not None:
        with open("subtitles.txt", "w", encoding="utf-8") as file:
            file.write(captions)
else:
    print("Английские субтитры не были найдены :( ")
