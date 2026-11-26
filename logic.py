
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from Ui_calculatrice import Ui_MainWindow
import sys


class Calculatrice(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("nexo_prim")
        self.setWindowIcon(QIcon("calculatrice-removebg-preview.png"))

        # Connexion des boutons numériques
        for i in range(10):
            bouton = getattr(self, f"push_{i}")
            bouton.clicked.connect(self.affichage)

        # Connexion des opérateurs
        self.push_plus.clicked.connect(self.special)
        self.push_moin.clicked.connect(self.special)
        self.push_fois.clicked.connect(self.special)
        self.push_division.clicked.connect(self.special)

        # Connexion des autres boutons
        self.push_clear.clicked.connect(self.all_delete)
        self.push_del.clicked.connect(self.one_delete)
        self.push_egal.clicked.connect(self.resultat)

    # Affichage des chiffres
    def affichage(self):
        bouton = self.sender()
        chiffre = bouton.text()

        if self.label_1.text() == "0":
            self.label_1.setText(chiffre)
        else:
            self.label_1.setText(self.label_1.text() + chiffre)

    # Gestion des opérateurs
    def special(self):
        bouton = self.sender()

        operations = {
            self.push_plus: "+",
            self.push_moin: "-",
            self.push_fois: "x",
            self.push_division: "/"
        }

        symbole = operations[bouton]
        texte = self.label_1.text()

        # Empêcher deux opérateurs successifs
        if texte[-1] in ["+", "-", "x", "/"]:
            return

        self.label_1.setText(texte + symbole)

    # Suppression totale
    def all_delete(self):
        self.label_1.setText("0")

    # Suppression du dernier caractère
    def one_delete(self):
        texte = self.label_1.text()

        if texte != "0":
            texte = texte[:-1]

        self.label_1.setText(texte if texte else "0")

    # Calcul du résultat
    def resultat(self):
        texte = self.label_1.text()

        for operateur in ["+", "-", "x", "/"]:

            if operateur in texte:
                try:
                    a, b = texte.split(operateur)

                    A = float(a)
                    B = float(b)

                    if operateur == "+":
                        resultat = A + B

                    elif operateur == "-":
                        resultat = A - B

                    elif operateur == "x":
                        resultat = A * B

                    elif operateur == "/":
                        if B == 0:
                            self.label_1.setText("Erreur")
                            return

                        resultat = A / B

                    # Éviter les résultats comme 15.0
                    if resultat == int(resultat):
                        resultat = int(resultat)

                    self.label_1.setText(str(resultat))
                    return

                except ValueError:
                    self.label_1.setText("Erreur")
                    return

        self.label_1.setText("Erreur")


def main():
    app = QApplication(sys.argv)

    window = Calculatrice()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

