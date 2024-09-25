# Import pyfiglet and argparse

from pyfiglet import Figlet
import argparse

# shorten Figlet function for better handling

fgl = Figlet()


def main():
    prompt = input("string: ")
    print(printer(prompt))


def printer(prompt):
    fgl.setFont(font="slant")
    return fgl.renderText(prompt)


if __name__ == "__main__":
    main()