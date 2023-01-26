from pytube import exceptions, YouTube
from pytube.cli import on_progress

#link = input("введи посилання щоб скачати відео: ")

def info_video(link):
    e = ''
    try:
        video = YouTube(link, on_progress_callback=on_progress)

    except exceptions.RegexMatchError:
        #print("не правильно введене посилання на відео")
        e = "не правильно введене посилання на відео"
        return e
    except exceptions.MembersOnly:
        #print("Відео доступне лише для підписників")
        e = "Відео доступне лише для підписників"
        return e
    else: 
        print(video.streams.filter(progressive=True, adaptive=True))   
        e = f"""
            Назва: \t\t\t\t\t {video.title}
            Довжина відео: \t\t\t{round(video.length/60, 1)} min
            Дата публікації: \t\t\t{video.publish_date}
            Рейтинг: \t\t\t\t\t{video.rating}
            Перегляди: \t\t\t\t {video.views}
            Низька якість важить: \t{round(video.streams.get_lowest_resolution().filesize_mb, 2)} mb
            Висока якість важить: \t{round(video.streams.get_highest_resolution().filesize_mb, 2)} mb
                """.expandtabs(tabsize=8)
                
        print(f"""
            Назва: \t\t\t{video.title}
            Довжина відео: \t\t{video.length/60} min
            Дата публікації: \t{video.publish_date}
            Рейтинг: \t\t{video.rating}
            Перегляди: \t\t{video.views}
            Низька якість важить: \t{video.streams.get_lowest_resolution().filesize_mb} mb
            Висока якість важить: \t{video.streams.get_highest_resolution().filesize_mb} mb
                """.expandtabs(tabsize=8))
        return e        
        

def quality (q):        
    quality = input("скачати у високій якості чи в низькій введіть (H / L): ")

    if quality.capitalize() == "H":
        output = video.streams.get_highest_resolution()
    if quality.capitalize() == "L":
        output = video.streams.get_lowest_resolution()

    output.download(output_path="/home/gnojevik/Зображення/live_paper") 