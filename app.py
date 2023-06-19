import argparse
import os
from main import Features

app_name = 'Youtube MP3 Downloader'

def exec_build(create_spec):
    if create_spec or not os.path.exists('app.spec'):
        print('Creating new .spec file and build app.')
        os.system(f'pyinstaller --noconfirm --onefile --console --icon icon.ico --name "Youtube MP3" main.py')
        if os.path.exists('app.spec'):
            os.remove('app.spec')
        os.rename(f'{app_name}.spec', 'app.spec')
    else:
        print('Using existing .spec file to build app.')
        os.system(f'pyinstaller app.spec')

def exec_run():
    while True:
        Features.download_mp3()

def main():
    parser = argparse.ArgumentParser(description='Youtube MP3')
    parser.add_argument('action', choices=['run', 'build'], help='Command')
    parser.add_argument('-c', '--create-spec', action='store_true', help='Create new .spec file')
    args = parser.parse_args()

    if args.action == 'run':
        exec_run()
    elif args.action == 'build':
        exec_build(args.create_spec)

if __name__ == '__main__':
    main()
