import sys

class REPL:

    def __init__(self, central_store):
        self.central_store = central_store

    def repl(self):
        cmd_line = raw_input("mm> ")

        if cmd_line == "quit":
            self.quit()

    def quit(self):
        #python auto garbage collection
        sys.exit()