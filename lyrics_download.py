import argparse
import urllib3
import mutagen

FLAGS = None

def main():
    tag=mutagen.File(FLAGS.file)['COMM::XXX'][0].strip("163 key(Don't modify):")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        type=str,
        default='',
        help='Music file.'
    )
    FLAGS, unparsed = parser.parse_known_args()
    main()
