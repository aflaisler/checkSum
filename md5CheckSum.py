import hashlib
import argparse


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="name of file to check")
    args = parser.parse_args()

    assert args.filename is not None, "Please enter the number of days to retrieve the data from"
    assert isinstance(args.filename, str), "Please enter a str"

    filepath = '/Users/aymericflaisler/Downloads/' + args.filename
    print md5(filepath)
