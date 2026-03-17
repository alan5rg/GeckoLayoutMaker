import sys, os
from PyQt5.QtWidgets import QApplication
from GeckoLayoutMaker14 import GeckoLayoutMaker
import qdarkstyle
from qdarkstyle import DarkPalette

from pathlib import Path

sys.path.append(str(Path(__file__).parent))

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))
    window = GeckoLayoutMaker()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()