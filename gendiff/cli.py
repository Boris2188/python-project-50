import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Compres two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second parser')
    return parser.parse_args()
