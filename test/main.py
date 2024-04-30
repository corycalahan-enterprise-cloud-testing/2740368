#!/usr/bin/python3
from flask import  request

def main():
    if True:
        print("Hello, World!"+request.args.get('name', ''))

if __name__ == '__main__':
    main()
