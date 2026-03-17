# layout_generator.py
# ────────────────────────────────────────
# v.2.0 soporta alineación
"""
Motor espacial del GeckoLayoutMaker.

Convierte una lista de widgets en un layout
según distintos modos:

    - matrix
    - diamond
    - vertical
    - horizontal

Genera código PyQt5 listo para integrarse
con los widgets generados por WidgetGenerator.
"""
import sys

print("LayoutGenerator module loaded")

class LayoutGenerator:

    def __init__(self, layout_mode="matrix", alignment=None):
        self.layout_mode = layout_mode
        self.alignment = alignment

    # -------------------------------------------------
    # Helper interno para addWidget
    # -------------------------------------------------
    def _add(self, name, row=None, col=None):

        if self.alignment is not None:

            if row is not None:
                return f"layout.addWidget(self.{name}, {row}, {col}, alignment={self.alignment})"
            else:
                return f"layout.addWidget(self.{name}, alignment={self.alignment})"

        else:

            if row is not None:
                return f"layout.addWidget(self.{name}, {row}, {col})"
            else:
                return f"layout.addWidget(self.{name})"

    # -------------------------------------------------
    # Genera y retorna el Layout
    # -------------------------------------------------
    def generate_layout_code(self, widget_names):

        if self.layout_mode == "matrix":
            return self._matrix(widget_names)

        if self.layout_mode == "diamond":
            return self._diamond(widget_names)

        if self.layout_mode == "vertical":
            return self._vertical(widget_names)

        if self.layout_mode == "horizontal":
            return self._horizontal(widget_names)

        raise ValueError("Unknown layout mode")

    # -------------------------------------------------
    # MATRIX
    # -------------------------------------------------
    def _matrix(self, widgets):

        code = []

        code.append("layout = QGridLayout()")
        code.append("")

        cols = int(len(widgets) ** 0.5) or 1

        row = 0
        col = 0

        for name in widgets:

            #code.append(f"layout.addWidget(self.{name}, {row}, {col})")
            code.append(self._add(name, row, col))

            col += 1

            if col >= cols:
                col = 0
                row += 1

        return "\n".join(code)

    # -------------------------------------------------
    # VERTICAL
    # -------------------------------------------------
    def _vertical(self, widgets):

        code = []

        code.append("layout = QVBoxLayout()")
        code.append("")

        for name in widgets:
            #code.append(f"layout.addWidget(self.{name})")
            code.append(self._add(name))

        return "\n".join(code)

    # -------------------------------------------------
    # HORIZONTAL
    # -------------------------------------------------
    def _horizontal(self, widgets):

        code = []

        code.append("layout = QHBoxLayout()")
        code.append("")

        for name in widgets:
            #code.append(f"layout.addWidget(self.{name})")
            code.append(self._add(name))

        return "\n".join(code)

    # -------------------------------------------------
    # DIAMOND
    # -------------------------------------------------
    def _diamond(self, widgets):

        code = []

        code.append("layout = QGridLayout()")
        code.append("")

        n = len(widgets)

        if n == 4:

            positions = [
                (0, 1),
                (1, 0),
                (1, 2),
                (2, 1),
            ]

        elif n == 5:

            positions = [
                (0, 1),
                (1, 0),
                (1, 2),
                (2, 1),
                (1, 1),
            ]

        else:
            # fallback a matrix
            return self._matrix(widgets)

        for name, pos in zip(widgets, positions):

            r, c = pos
            #code.append(f"layout.addWidget(self.{name}, {r}, {c})")
            code.append(self._add(name, r, c))

        return "\n".join(code)