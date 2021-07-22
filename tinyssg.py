#!/usr/bin/env python3
import argparse


def cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src_dir', default='src/')
    parser.add_argument('-t', '--template_dir', default='template/')
    parser.add_argument('-e', '--extra_dir', default='extra/')
    parser.add_argument('-o', '--output_dir', default='output/')
    return parser.parse_args()


def main():
    print(cmd())


if __name__ == '__main__':
    main()
