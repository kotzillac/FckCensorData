import yt_dlp
import json

while True:
    id = input("Yandex Music track ID or URL: ").split('/')[-1].split('?')[0]

    print("Fetching track info...")

    from yandex_music import Client
    client = Client().init()
    track_info = client.tracks([id])[0]
    track_name = f'{track_info.title} - {(", ".join(track_info.artistsName()))}'
    print(f'Track name: {track_name}')

    should_download = input("Download track? (y/n): ").lower() == 'y'
    if should_download:
        def download_sound():
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'tracks/{id}',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"ytsearch1:{track_name}"])

        download_sound()

    with open('list.json', 'r') as f:
        data = json.loads(f.read())
        data['tracks'][id] = f'https://cdn.statically.io/gh/kotzillac/FckCensorData@main/tracks/{id}'

    with open('list.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    with open('README.md', 'a', encoding='utf-8') as f:
        f.write(f'\n- [{track_name}](https://music.yandex.ru/track/{id})')

    with open('git_message.txt', 'a', encoding='utf-8') as f:
        f.write(f'Added [{track_name}]; ')
    
    print(f'Successfully added track {track_name}')