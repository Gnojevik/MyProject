from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
import re
from pytube import exceptions, YouTube
from SaveDirectory import Ui_MainWindow


class testWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionsave_Directory.triggered.connect(self.click)
        self.pushButton.clicked.connect(self.click)
        self.lineEdit.textEdited.connect(self.text_edited)
        self.comboBox.currentIndexChanged.connect(self.current_index)
        self.progressBar.setVisible(False)
        self.comboBox.setVisible(False)
        self.label_2.setVisible(False)
        
    link = ''
    index = 0
    
    def text_edited(self, s):

        self.pushButton.setEnabled(True)
        self.actionsave_Directory.setEnabled(True)
        self.comboBox.setVisible(True)
        self.label_2.setVisible(True)
        self.link = s
        
    
    def save_dir(self):
        path = QFileDialog.getExistingDirectory()
        return path

    def click(self, link):
        self.info_video(self.link, self.index)
        
                

    def current_index(self):
        self.index = self.comboBox.currentIndex()
        print(self.index)
        

    def info_video(self, link, quality ):
        e = ''
        try:
            video = YouTube(link, on_progress_callback=self.progress_func)

        except exceptions.RegexMatchError:
            #print("не правильно введене посилання на відео")
            QMessageBox.warning(self, 'Warning', "не правильно введене посилання на відео" )
            e = "не правильно введене посилання на відео"
            return e
        except exceptions.MembersOnly:
            QMessageBox.warning(self, 'Warning', "Відео доступне лише для підписників")
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

            if quality == 0:
                output = video.streams.get_highest_resolution()   
                output.download(output_path = self.save_dir())
            if quality == 1:
                output = video.streams.get_lowest_resolution()
                output.download(output_path = self.save_dir())
            if quality == 2:
                audio_streams = video.streams.filter(only_audio=True)
            
                # знайдіть найвищу якість за бітрейтом
                highest_bitrate = 0
                highest_bitrate_stream = None
                for stream in audio_streams:
                    if stream.abr is not None:
                        # використовуємо регулярний вираз, щоб виділити значення бітрейту
                        abr_match = re.search(r'(\d+)kbps', stream.abr)
                        if abr_match:
                            abr = int(abr_match.group(1))
                            if abr > highest_bitrate:
                                highest_bitrate = abr
                                highest_bitrate_stream = stream

                # виведіть інформацію про найвищий бітрейт
                QMessageBox.information(self, 'information', f""" Найвищий бітрейт: {highest_bitrate} kbps  """ )
                
                # завантажте аудіо стрім з найвищим бітрейтом
                if highest_bitrate_stream is not None:
                    file_name = f"{video.title}.mp3"
                    highest_bitrate_stream.download(filename = file_name, output_path = self.save_dir())
                else:
                    QMessageBox.warning(self, 'Warning', "Не вдалося знайти аудіо стрім з найвищим бітрейтом.")
                   
                   

            
                 
                  
    def progress_func(self, stream, chunk, bytes_remaining):
            size = stream.filesize 
            progress = round(((float(abs(bytes_remaining-size)/size))*float(100)))
            self.progressBar.setVisible(True)
            self.progressBar.setValue(progress)
            if progress == 100:
                QMessageBox.information(self, 'information', f""" {stream.title} \n \n Успішно скачано  """ )
            
    

app = QApplication(sys.argv)
test = testWindow()
sys.exit(app.exec())