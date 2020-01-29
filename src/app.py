import fbprophet
import argparse


def getfbprophetversion():
    return fbprophet.__version__


def main(s3path: str):
    # run model against files from s3 location
    # write output to new location in s3
    print('run model against files from {} & write output to new location in s3'.format(s3path))


if __name__ == '__main__':
    print("prophet version = {}".format(getfbprophetversion()))
    # parse s3 file location argument from args

    parser = argparse.ArgumentParser(prog='app')
    parser.add_argument(
        '--data_location',
        help="S3 path that contains data",
        required=False,
        default=None
    )

    args = parser.parse_args()
    args_dict = args.__dict__

    main(args_dict["data_location"])
