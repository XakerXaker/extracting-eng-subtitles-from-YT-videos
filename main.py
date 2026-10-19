import time

from pytubefix import YouTube

url = "YourYTVideoUrl"

ATTEMPTS = 5
PAUSE_SECONDS = 10


def fetch_subtitles(url):
    codes = []
    for attempt in range(ATTEMPTS):
        try:
            video = YouTube(url, client="WEB")
            codes = [caption.code for caption in video.captions]
            if codes:
                eng_code = next((code for code in codes if "en" in code), None)
                if eng_code is None:
                    return None, True
                return video.captions[eng_code].generate_txt_captions(), True
        except Exception:
            pass
        if attempt < ATTEMPTS - 1:
            time.sleep(PAUSE_SECONDS)
    return None, False


captions, youtube_responded = fetch_subtitles(url)

if not youtube_responded:
    print("YouTube не отдал данные о субтитрах. Попробуйте позже")
    exit(1)

if captions is None:
    print("Английские субтитры не были найдены :( ")
    exit(0)

with open("subtitles.txt", "w", encoding="utf-8") as file:
    file.write(captions)
