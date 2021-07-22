#!/usr/bin/env python3
import argparse


def cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template_dir', default='template/')
    parser.add_argument('-o', '--output_dir', default='output/')
    return parser.parse_args()


def main():
    tmpl, out = cmd().template_dir, cmd().output_dir
    print(tmpl, out)


if __name__ == '__main__':
    main()
