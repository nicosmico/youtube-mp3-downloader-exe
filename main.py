from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import sys

# TODO: Use .env to define this
app_path = os.getcwd() # Use this when run with python (dev)
# app_path = os.path.dirname(sys.executable) # Use this when build .exe (prod)

# TODO: Create new files for each class. Remember edit build command too.

class Features:
    @staticmethod
    def download_mp3():
        link = ''
        while len(link) == 0 or ('youtube.com' not in link and 'youtu.be' not in link):
            Utils.clear_screen()
            print('♪♪♪♪♪ Youtube MP3 v0.1 ♪♪♪♪♪ \n')

            print('Instrucciones: ')
            print('\t 1) Ingrese el link del video a descargar (Ctrl + V).')
            print('\t 2) Luego presione Enter.')
            link = input("Link de Youtube >> ")

        # Download video
        temp_dir = os.path.join(app_path, '.temp')
        file_path = Downloader.download_by_link(link, temp_dir)
        if not file_path:
            print('✕ Error: Error al descargar el archivo.')
            return

        # Convert to mp3
        converted_file_path = Converter.convert_to_mp3(file_path)
        os.remove(file_path)
        if not converted_file_path:
            print('✕ Error: Error al convertir el archivo.')
            return
        
        file_name = os.path.basename(converted_file_path)
        print(f'✓ Archivo descargado: ‣ {file_name} \n')
        print('Presione Enter para continuar → \n')
        input()

class Downloader:
    @staticmethod
    def download_by_link(link: str, output_path: str | None = None) -> str | None:
        """
        Download youtube video by link
        """
        try:
            output_path = output_path or app_path
            yt = YouTube(link)
            # print('[Downloader] Video name: ', yt.title)
            # print('[Downloader] Video channel: ', yt.author)

            # Get best stream by abr
            # streams = yt.streams.order_by('abr').desc()
            streams = yt.streams.filter(only_audio=True).order_by('abr').desc()
            if not streams or len(streams) == 0:
                print('[Downloader] Streams not found.')
                return None

            # Download
            stream = streams[0]
            print(f'Descargando: "{yt.title}" \n')
            # print(f'[Downloader] Downloading {yt.title}...')
            # print('[Downloader] Stream: ', stream)
            file_path = stream.download(output_path=output_path)
            # print('[Downloader] Download completed.')
            return file_path

        except Exception as e:
            print(f'[Downloader] Error downloading file: {link}')
            print(f'[Downloader] Error: {str(e)}')
            return None

class Converter:
    @staticmethod
    def convert_to_mp3(file_path: str, output_path: str | None = None) -> str | None:
        """
        Convert file in file_path to .mp3
        """
        try:
            file_name = os.path.basename(file_path)
            # print(f'[Converter] Converting {file_name} to mp3...')

            file = AudioFileClip(file_path)

            new_file_name = file_name.split('.')[0] + '.mp3'
            output_path = output_path or app_path
            output_path = os.path.join(output_path, new_file_name)

            file.write_audiofile(output_path)
            file.close()
            # print('[Converter] Conversion completed.')
            return output_path

        except Exception as e:
            print(f'[Converter] Error converting to mp3: {file_path}')
            print(f'[Converter] Error: {str(e)}')
            return None

class Utils:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    while True:
        Features.download_mp3()
