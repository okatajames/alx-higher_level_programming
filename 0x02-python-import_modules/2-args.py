#!/usr/bin/python3
if __name__ == "__main__":
    """Print the num and list of args"""
    import sys

    track = len(sys.argv) - 1
    if track == 0:
        print("0 arguments.")
    elif track == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(track))
    for k in range(track):
        print("{}: {}".format(k + 1, sys.argv[k + 1]))
