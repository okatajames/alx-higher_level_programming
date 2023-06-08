#!/usr/bin/python3
if __name__ == "__main__":
    """ This prints all the hidden dirs"""
    import hidden_4

    for j in dir(hidden_4):
        if j[:2] != "__":
            print(j)
