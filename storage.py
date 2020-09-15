import argparse as arg
import tempfile as tmp
import os
import json as js

def pars_args():
    parser = arg.ArgumentParser()
    parser.add_argument('-key')
    parser.add_argument('-value')
    args = parser.parse_args()
    return args

def json_work(storage, args):

    dictionary = {}

    if os.stat(storage).st_size == 0:
        with open(storage, 'w') as f:
            js.dump(dictionary, f)

    elif args.value is None:
        print(None)

    else:
        with open(storage, 'w') as f:
            js.dump(dictionary, f)


def main():
    args = pars_args()
    storage = os.path.join(tmp.gettempdir(), 'storage.data')
    json_work(storage, args)


main()