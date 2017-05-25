class Prompt:
    # Le constructeur de classe, à compléter plus tard.
    def __init__(self):
        self.done = False

    # Pas besoin d'expliquer je pense...
    # A compléter plus tard. En attendant, écrire "exit" doit faire sortir du programme.
    def run(self):
        self.input = self.read()

        if self.input == "exit":
            self.done = True

    # Trois fonctions qui créent les règles à partir de fichiers .json (JavaScript Object Notation).
    # A compléter plus tard.
    def loadrules(self):
        pass

    def loadruleNotUnderstood(self):
        pass

    def loadruleExit(self):
        pass

    # La fonction qui récupèrera notre input.
    def read(self):
        return input(">")