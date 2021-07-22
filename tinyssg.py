#!/usr/bin/env python3
import argparse


def cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src_dir', default='src/',
                        help='Markdown Source Directory (default: src/)')
    parser.add_argument('-t', '--template_dir', default='template/',
                        help='Template Directory (default: template/)')
    parser.add_argument('-e', '--extra_dir', default='extra/',
                        help='Extra Files Directory (default: extra/)')
    parser.add_argument('-o', '--output_dir', default='output/',
                        help='Output Directory (default: output/)')
    return parser.parse_args()


def main():
    print(cmd())


if __name__ == '__main__':
    main()
