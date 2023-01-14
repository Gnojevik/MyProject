from pytube import exceptions, YouTube
from pytube.cli import on_progress

link = input("введи посилання щоб скачати відео: ")

try:
    video = YouTube(link, on_progress_callback=on_progress)

except exceptions.RegexMatchError:
    print("не правильно введене посилання на відео")
except exceptions.MembersOnly:
    print("Відео доступне лише для підписників")
else:    
    print(f"""
        Назва: \t\t\t{video.title}
        Довжина відео: \t\t{video.length/60} min
        Дата публікації: \t{video.publish_date}
        Рейтинг: \t\t{video.rating}
        Перегляди: \t\t{video.views}
        Низька якість важить: \t{video.streams.get_lowest_resolution().filesize_mb} mb
        Висока якість важить: \t{video.streams.get_highest_resolution().filesize_mb} mb
            """.expandtabs(tabsize=8))
    
    quality = input("скачати у високій якості чи в низькій введіть (H / L): ")

if quality.capitalize() == "H":
    output = video.streams.get_highest_resolution()
if quality.capitalize() == "L":
    output = video.streams.get_lowest_resolution()

output.download(output_path="/home/gnojevik/Відео/youtube") 