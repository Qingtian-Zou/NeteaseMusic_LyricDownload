import argparse
import urllib.request
import os
from ast import literal_eval

FLAGS = None

def main():
    file=os.path.split(FLAGS.file_path)
    file=file[1].strip(".mp3")+".lrc"
    raw=urllib.request.urlopen("http://music.163.com/api/song/media?id="+FLAGS.id)
    lyrics=raw.read().decode('utf-8')
    lyrics=literal_eval(lyrics)
    try:
        f=open(os.path.join(os.path.split(FLAGS.file_path)[0],file),'w',encoding="utf-8")
        lyrics=lyrics["lyric"]
        lyrics=lyrics.split('\n')
        f.write("[00:00.000]"+os.path.basename(FLAGS.file_path.split(".mp3")[0])+"\n")
        for line in lyrics:
            f.write(line+'\n')
        f.close()
        print("Dumped successfully!")
    except KeyError as identifier:
        print("No lyrics found!")
    # TODO: write lyrics into the music file as an entry of the id3v2 tag

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--id',
        type=str,
        default='',
        help='Music id from Netease Music.'
    )
    parser.add_argument(
        '--file_path',
        type=str,
        default='',
        help='Abosolute path to the music file.'
    )
    FLAGS, unparsed = parser.parse_known_args()
    main()
