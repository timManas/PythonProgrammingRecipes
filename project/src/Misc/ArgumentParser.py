#!/usr/bin/env python

import argparse

def main():
    print("Fetching arguments From User")

    parser = argparse.ArgumentParser()
    parser.add_argument("--name", dest="name", required=True, help="Name")
    parser.add_argument("--age", dest="age", required=False, help="Age of User")
    parser.add_argument("--id", dest="id", required=True, default="12345", help="Id")
    argument = parser.parse_args()

    print("Name: " + argument.name + "  |Age: " + argument.age + "    |Id: " + argument.id)

    pass


if __name__ == '__main__':
    main()