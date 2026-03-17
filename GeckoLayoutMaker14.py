# GeckoLAyoutMaker.py
# --- Gecko Layout Maker Asistido por NOvaDulceKali ---
import sys, os
from generators.widget_generator import WidgetGenerator 
from generators.layout_generator20 import LayoutGenerator
from GeckoPreviewPanel import GeckoPreviewPanel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDial, QSlider, QApplication
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QSpinBox,
    QComboBox,
    QCheckBox,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout
)

import importlib.util

geckoappversion = "1.4"

class GeckoLayoutMaker(QMainWindow):
    """
    GeckoLayoutMaker v1
    -------------------
    Generador geckónico de layouts para PyQt5.

    Permite definir:
        - Cantidad de botones (y sus tamaños [en global])
        - Cantidad de diales (y sus tamaños [en global])
        - Cantidad de sliders (y sus tamaños [en global])
        - Tamaño del Panel a crear [Nueva y Apasionante funcion que abre la puerta al Cálculo Vulkano!!!]
        - Modo de disposición espacial
        - Exclusividad de botones

    Genera widgets y layouts listos para usar.

    Función Preview ---> Proximamente Live Preview!!! no te lo pierdas!!!
    
    Roadmap: 
    * Live Preview.
    * Implementacion de creación de layout en archivo.
    """
    MAX_WIDGETS = 100
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"GeckoLayoutMaker v{geckoappversion}")
        self.setFixedSize(640, 800)
        self._build_ui()
    
    # -----------------------------------------------------------------
    # Interfaz de Usuario Geckonista Geckoista Geckonizado
    # -----------------------------------------------------------------
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        # Geckeado by NOva DulceKali 16/03/26 12:50
        # -------------------------------------------------
        # WIDGET COUNTS (Geckónico Edition)
        # -------------------------------------------------
        group_counts = QGroupBox("The True Widget Souls (Counts and Geometry)")

        counts_layout = QGridLayout()

        self_geometrys_all_spins = []

        # -----------------------------
        # 🟢 Luis Buttons
        # -----------------------------
        self.combo_buttons = QComboBox()
        self.combo_buttons.addItems([str(i) for i in range(self.MAX_WIDGETS + 1)])

        self.spin_btn_w = QSpinBox()
        self.spin_btn_w.setRange(10, 500)
        self.spin_btn_w.setValue(95)
        self_geometrys_all_spins.append(self.spin_btn_w)

        self.spin_btn_h = QSpinBox()
        self.spin_btn_h.setRange(10, 500)
        self.spin_btn_h.setValue(30)
        self_geometrys_all_spins.append(self.spin_btn_h)

        counts_layout.addWidget(QLabel("Luis Button's"), 0, 0)
        counts_layout.addWidget(self.combo_buttons, 0, 1)

        counts_layout.addWidget(QLabel("Luis's Width"), 1, 0)
        counts_layout.addWidget(self.spin_btn_w, 1, 1)

        counts_layout.addWidget(QLabel("Luis's Height"), 2, 0)
        counts_layout.addWidget(self.spin_btn_h, 2, 1)


        # -----------------------------
        # 🔵 Jenifer Dials
        # -----------------------------
        self.combo_dials = QComboBox()
        self.combo_dials.addItems([str(i) for i in range(self.MAX_WIDGETS + 1)])

        self.spin_dial_w = QSpinBox()
        self.spin_dial_w.setRange(10, 500)
        self.spin_dial_w.setValue(50)
        self_geometrys_all_spins.append(self.spin_dial_w)

        self.spin_dial_h = QSpinBox()
        self.spin_dial_h.setRange(10, 500)
        self.spin_dial_h.setValue(50)
        self_geometrys_all_spins.append(self.spin_dial_h)
        
        counts_layout.addWidget(QLabel("Jenifer Dial's"), 3, 0)
        counts_layout.addWidget(self.combo_dials, 3, 1)

        counts_layout.addWidget(QLabel("Jenifer's Width"), 4, 0)
        counts_layout.addWidget(self.spin_dial_w, 4, 1)

        counts_layout.addWidget(QLabel("Jenifer's Height"), 5, 0)
        counts_layout.addWidget(self.spin_dial_h, 5, 1)

        # -----------------------------
        # 🔴 Vader Sliders
        # -----------------------------
        self.combo_sliders = QComboBox()
        self.combo_sliders.addItems([str(i) for i in range(self.MAX_WIDGETS + 1)])

        self.spin_slider_w = QSpinBox()
        self.spin_slider_w.setRange(10, 500)
        self.spin_slider_w.setValue(27)
        self_geometrys_all_spins.append(self.spin_slider_w)

        self.spin_slider_h = QSpinBox()
        self.spin_slider_h.setRange(10, 500)
        self.spin_slider_h.setValue(137)
        self_geometrys_all_spins.append(self.spin_slider_h)

        counts_layout.addWidget(QLabel("Vader Slider's"), 6, 0)
        counts_layout.addWidget(self.combo_sliders, 6, 1)

        counts_layout.addWidget(QLabel("Vader's Width"), 7, 0)
        counts_layout.addWidget(self.spin_slider_w, 7, 1)

        counts_layout.addWidget(QLabel("Vader's Height"), 8, 0)
        counts_layout.addWidget(self.spin_slider_h, 8, 1)

        group_counts.setLayout(counts_layout)

        # -------------------------------------------------
        # PANEL SIZE
        # -------------------------------------------------
        group_size = QGroupBox("Total Panel Size")

        size_layout = QGridLayout()

        self.spin_width = QSpinBox()
        self.spin_width.setRange(100, 2000)
        self.spin_width.setValue(400)

        self.spin_height = QSpinBox()
        self.spin_height.setRange(100, 2000)
        self.spin_height.setValue(768)

        size_layout.addWidget(QLabel("Width"), 0, 0)
        size_layout.addWidget(self.spin_width, 0, 1)

        size_layout.addWidget(QLabel("Height"), 1, 0)
        size_layout.addWidget(self.spin_height, 1, 1)

        group_size.setLayout(size_layout)

        # -------------------------------------------------
        # LAYOUT MODE
        # -------------------------------------------------

        group_layout_mode = QGroupBox("Layout Mode Distribution")

        layout_mode = QVBoxLayout()

        self.radio_matrix = QRadioButton("Matrix")
        self.radio_diamond = QRadioButton("Diamond")
        self.radio_vertical = QRadioButton("Vertical line")
        self.radio_horizontal = QRadioButton("Horizontal line")

        self.radio_vertical.setChecked(True)  # default seguro

        self.layout_mode_group = QButtonGroup()
        self.layout_mode_group.setExclusive(True)

        self.layout_mode_group.addButton(self.radio_matrix)
        self.layout_mode_group.addButton(self.radio_diamond)
        self.layout_mode_group.addButton(self.radio_vertical)
        self.layout_mode_group.addButton(self.radio_horizontal)

        layout_mode.addWidget(self.radio_matrix)
        layout_mode.addWidget(self.radio_diamond)
        layout_mode.addWidget(self.radio_vertical)
        layout_mode.addWidget(self.radio_horizontal)

        group_layout_mode.setLayout(layout_mode)

        # -------------------------------------------------
        # ALIGNMENT MODE
        # -------------------------------------------------

        group_alignment = QGroupBox("Widget Alignment Rules")

        alignment_layout = QVBoxLayout()

        self.radio_align_center = QRadioButton("Center")
        self.radio_align_left = QRadioButton("Left")
        self.radio_align_right = QRadioButton("Right")
        self.radio_align_top = QRadioButton("Top")
        self.radio_align_bottom = QRadioButton("Bottom")

        self.radio_align_center.setChecked(True)  # default seguro

        self.alignment_group = QButtonGroup()
        self.alignment_group.setExclusive(True)

        self.alignment_group.addButton(self.radio_align_center)
        self.alignment_group.addButton(self.radio_align_left)
        self.alignment_group.addButton(self.radio_align_right)
        self.alignment_group.addButton(self.radio_align_top)
        self.alignment_group.addButton(self.radio_align_bottom)

        alignment_layout.addWidget(self.radio_align_center)
        alignment_layout.addWidget(self.radio_align_left)
        alignment_layout.addWidget(self.radio_align_right)
        alignment_layout.addWidget(self.radio_align_top)
        alignment_layout.addWidget(self.radio_align_bottom)

        group_alignment.setLayout(alignment_layout)


        # -------------------------------------------------
        # BUTTON LOGIC
        # -------------------------------------------------

        group_logic = QGroupBox("Button Logic Mode")
        logic_layout = QVBoxLayout()
        self.chk_exclusive = QCheckBox("Exclusive buttons")
        logic_layout.addWidget(self.chk_exclusive)
        group_logic.setLayout(logic_layout)

        # -------------------------------------------------
        # Gecko Feedback For Intrepid User's
        # -------------------------------------------------
        self.feedback=QTextEdit("Bienvenido a GeckoLayoutMaker!!!")
        #self.feedback.setFixedHeight(371)

        # -------------------------------------------------
        # GENERATE BUTTON
        # -------------------------------------------------
        self.btn_generate = QPushButton("Generate Layout File")
        self.btn_preview = QPushButton("Preview Panel In Memory")
        
        # -------------------------------------------------
        # LAYOUT GECKOLAYOUTMAKER GECKONIZADO
        # -------------------------------------------------
        milayout = QHBoxLayout()
        input_data_zone = QVBoxLayout()
        input_data_zone.addWidget(group_counts)
        input_data_zone.addWidget(group_size)
        input_data_zone.addWidget(group_layout_mode)
        input_data_zone.addWidget(group_alignment)
        input_data_zone.addWidget(group_logic)
        milayout.addLayout(input_data_zone)

        output_zone = QVBoxLayout()
        output_zone.addWidget(self.feedback)
        #output_zone.addStretch()
        output_zone.addWidget(self.btn_generate)
        output_zone.addWidget(self.btn_preview)
        milayout.addLayout(output_zone)
        
        main_layout.addLayout(milayout)

        # ------------------------------------------------
        # CONNECTORS
        # ------------------------------------------------
        self.btn_generate.clicked.connect(self.generate_layout)
        self.btn_preview.clicked.connect(self.preview_panel)

        # Conectar actualizaciones para recálculo smart
        for spin in self_geometrys_all_spins:
            spin.valueChanged.connect(self._validate_config)

        self.spin_width.valueChanged.connect(self._validate_config)
        self.spin_height.valueChanged.connect(self._validate_config)

        self.combo_buttons.currentIndexChanged.connect(self._validate_config)
        self.combo_dials.currentIndexChanged.connect(self._validate_config)
        self.combo_sliders.currentIndexChanged.connect(self._validate_config)

        self.layout_mode_group.buttonClicked.connect(self._validate_config)
        self.alignment_group.buttonClicked.connect(self._validate_config)

        self._validate_config()

    # -----------------------------------------------------------------
    # Metodo Unificado que recolecta los Datos Ingresados
    # -----------------------------------------------------------------    
    def _collect_config(self):

        layout_type = "matrix"
        if self.radio_matrix.isChecked():
            layout_type = "matrix"
        elif self.radio_diamond.isChecked():
            layout_type = "diamond"
        elif self.radio_vertical.isChecked():
            layout_type = "vertical"
        elif self.radio_horizontal.isChecked():
            layout_type = "horizontal"

        # ---------------------------------------
        # Alignment Selection
        # ---------------------------------------

        alignment = "Qt.AlignCenter" #Qt.AlignCenter

        if self.radio_align_left.isChecked():
            alignment = "Qt.AlignLeft"
        elif self.radio_align_right.isChecked():
            alignment = "Qt.AlignRight"
        elif self.radio_align_top.isChecked():
            alignment = "Qt.AlignTop"
        elif self.radio_align_bottom.isChecked():
            alignment = "Qt.AlignBottom"
        elif self.radio_align_center.isChecked():
            alignment = "Qt.AlignCenter"


        config = {
            "buttons": int(self.combo_buttons.currentText()),
            "dials": int(self.combo_dials.currentText()),
            "sliders": int(self.combo_sliders.currentText()),

            "button_size": (self.spin_btn_w.value(), self.spin_btn_h.value()),
            "dial_size": (self.spin_dial_w.value(), self.spin_dial_h.value()),
            "slider_size": (self.spin_slider_w.value(), self.spin_slider_h.value()),

            "width": self.spin_width.value(),
            "height": self.spin_height.value(),
            "layout_type": layout_type,
            "exclusive_buttons": self.chk_exclusive.isChecked(),
            "alignment": alignment,
        }

        return config

    # -----------------------------------------------------------------
    # 💡 Diseño Vulkano de _validate_config()
    # -----------------------------------------------------------------
    def _validate_config(self):

        config = self._collect_config()

        panel_w = config["width"]
        panel_h = config["height"]

        buttons = config["buttons"]
        dials = config["dials"]
        sliders = config["sliders"]

        btn_w, btn_h = config["button_size"]
        dial_w, dial_h = config["dial_size"]
        slider_w, slider_h = config["slider_size"]

        layout_type = config["layout_type"]

        alignment_flag = config["alignment"]

        alignment_map = {
            Qt.AlignLeft: "Qt.AlignLeft",
            Qt.AlignRight: "Qt.AlignRight",
            Qt.AlignTop: "Qt.AlignTop",
            Qt.AlignBottom: "Qt.AlignBottom",
            Qt.AlignCenter: "Qt.AlignCenter",
        }

        alignment_text = alignment_map.get(alignment_flag, "Qt.AlignCenter")

        total_widgets = buttons + dials + sliders

        panel_area = panel_w * panel_h

        area_buttons = buttons * (btn_w * btn_h)
        area_dials = dials * (dial_w * dial_h)
        area_sliders = sliders * (slider_w * slider_h)

        used_area = area_buttons + area_dials + area_sliders

        occupancy = (used_area / panel_area) * 100

        # Todo el mensaje con las Metricas del Panel
        feedback_text = (
            f"\nArea Total: ancho[{panel_w}] alto[{panel_h}] = {panel_area:,} px²\n\n"
            f"{buttons} Botones, ancho[{btn_w}] alto[{btn_h}]\n"
            f"{dials} Diales, ancho[{dial_w}] alto[{dial_h}]\n"
            f"{sliders} Sliders, ancho[{slider_w}] alto[{slider_h}]\n"
            f"Alineación: {alignment_flag}\n"
            f"\nArea Ocupada: {used_area:,} px²\n"
            f"% de Ocupación: {occupancy:.1f}%\n"
        )

        self.feedback.setText(feedback_text)

        if total_widgets == 0:
            self.feedback.setText(feedback_text)
            return self._invalidate("No hay almas que renderizar, se siente el Espacio Vacio!!!\n"+feedback_text)

        # ------------------------------------------
        # VALIDACIÓN POR MODO
        # ------------------------------------------

        if layout_type == "vertical":

            max_height = (
                buttons * btn_h +
                dials * dial_h +
                sliders * slider_h
            )

            max_width = max(btn_w, dial_w, slider_w)

            if max_height > panel_h or max_width > panel_w:
                return self._invalidate(
                    "Gecko advierte: Vertical supera límites del panel.\n"+feedback_text
                )

        elif layout_type == "horizontal":

            max_width = (
                buttons * btn_w +
                dials * dial_w +
                sliders * slider_w
            )

            max_height = max(btn_h, dial_h, slider_h)

            if max_width > panel_w or max_height > panel_h:
                return self._invalidate(
                    "Gecko advierte: Horizontal supera límites del panel.\n"+feedback_text
                )

        elif layout_type == "matrix":

            import math

            #cols = math.ceil(math.sqrt(total_widgets))
            #rows = math.ceil(total_widgets / cols)

            aspect_ratio = panel_w / panel_h
            cols = math.ceil(math.sqrt(total_widgets * aspect_ratio))
            rows = math.ceil(total_widgets / cols)

            #max_cell_w = max(btn_w, dial_w, slider_w)
            #max_cell_h = max(btn_h, dial_h, slider_h)

            widths = []
            heights = []

            if buttons > 0:
                widths.append(btn_w)
                heights.append(btn_h)

            if dials > 0:
                widths.append(dial_w)
                heights.append(dial_h)

            if sliders > 0:
                widths.append(slider_w)
                heights.append(slider_h)

            if not widths:
                return self._invalidate("Gecko advierte: No hay widgets para distribuir.")

            max_cell_w = max(widths)
            max_cell_h = max(heights)

            if cols * max_cell_w > panel_w or rows * max_cell_h > panel_h:
                return self._invalidate(
                    "Gecko advierte: Matrix incompatible con el tamaño actual.\n"+feedback_text
                )

        elif layout_type == "diamond":
            # Simplificado: usa bounding box similar a matrix
            import math

            max_cell_w = max(btn_w, dial_w, slider_w)
            max_cell_h = max(btn_h, dial_h, slider_h)

            diagonal = math.ceil(math.sqrt(total_widgets))

            if diagonal * max_cell_w > panel_w or diagonal * max_cell_h > panel_h:
                return self._invalidate(
                    "Spok recomienda que Jenifer baje de peso.\n"+feedback_text
                )

        # Si pasó todo:
        self._set_valid_state(feedback_text, occupancy)

        if hasattr(self, "preview_window") and self.preview_window is not None:
            config = self._collect_config()
            panel = self._build_panel_from_config(config)
            self.preview_window.update_panel(panel)

        return True

    

    # -----------------------------------------------------------------
    # 🎛 Funciones auxiliares limpias
    # -----------------------------------------------------------------
    def _invalidate(self, message, occupancy=None):

        if occupancy is not None:
            message += f"\n\nOcupación actual: {occupancy:.1f}%"
       
        self.feedback.setText(message)

        self.btn_generate.setEnabled(False)
        self.btn_preview.setEnabled(False)

        self.btn_generate.setStyleSheet("background-color: #662222;")
        self.btn_preview.setStyleSheet("background-color: #662222;")

        return False

    def _set_valid_state(self, message, occupancy=None):

        self.btn_generate.setEnabled(True)
        self.btn_preview.setEnabled(True)

        self.btn_generate.setStyleSheet("")
        self.btn_preview.setStyleSheet("")

        if occupancy is not None:
            self.feedback.setText(
                f"Configuración válida. Gecko sonríe!!!\n"+message
            )



    def _build_panel_from_config(self, config):
        """
        
        """
        # -------------------------------------------------
        # 1️⃣ Crear generador de widgets
        # -------------------------------------------------
        widget_gen = WidgetGenerator(
            buttons=config["buttons"],
            dials=config["dials"],
            sliders=config["sliders"]
        )

        widgets_dict = widget_gen.generate_all()

        all_names = (
            widgets_dict["buttons"] +
            widgets_dict["dials"] +
            widgets_dict["sliders"]
        )

        # -------------------------------------------------
        # 2️⃣ Crear panel real
        # -------------------------------------------------
        panel = QWidget()
        panel.setFixedSize(config["width"], config["height"])

        # Crear instancias reales dinámicamente
        for name in widgets_dict["buttons"]:
            btn = QPushButton(name)
            btn.setFixedSize(*config["button_size"])
            btn.setCheckable(True)
            setattr(panel, name, btn)

        for name in widgets_dict["dials"]:
            dial = QDial()
            dial.setFixedSize(*config["dial_size"])
            setattr(panel, name, dial)

        for name in widgets_dict["sliders"]:
            slider = QSlider()
            slider.setFixedSize(*config["slider_size"])
            setattr(panel, name, slider)

        # -------------------------------------------------
        # 3️⃣ Generar layout usando LayoutGenerator
        # -------------------------------------------------
        #layout_gen = LayoutGenerator(config["layout_type"])
        # Para soporte de alineación
        layout_gen = LayoutGenerator(config["layout_type"], alignment=config["alignment"])
        layout_code = layout_gen.generate_layout_code(all_names)

        # -------------------------------------------------
        # 4️⃣ Ejecutar layout_code en contexto controlado
        # -------------------------------------------------
        local_context = {
            "self": panel,
            "QVBoxLayout": QVBoxLayout,
            "QHBoxLayout": QHBoxLayout,
            "QGridLayout": QGridLayout,
            "Qt": Qt,
        }

        exec(layout_code, {}, local_context)

        layout = local_context.get("layout")

        panel.setLayout(layout)

        # -------------------------------------------------
        # 5️⃣ Exclusividad real si corresponde
        # -------------------------------------------------
        if config["exclusive_buttons"] and widgets_dict["buttons"]:

            group = QButtonGroup(panel)
            group.setExclusive(True)

            for name in widgets_dict["buttons"]:
                group.addButton(getattr(panel, name))

            panel._exclusive_group = group  # evitar GC

        return panel


    # -------------------------------------------------
    # 🔥 Preview usando tus generadores reales
    # -------------------------------------------------
    def preview_panel(self):
        """
            Genera un panel real en memoria utilizando:
                - WidgetGenerator
                - LayoutGenerator

            Muestra el resultado en GeckoPreviewPanel.

            No persiste en archivo.
            Usado para validación visual inmediata.
        """

        if not self._validate_config():
            return

        config = self._collect_config()

        panel = self._build_panel_from_config(config)

        # -------------------------------------------------
        # 6️⃣ Mostrar preview
        # -------------------------------------------------
        #self.preview_window = GeckoPreviewPanel(panel)
        #self.preview_window.show()
        #... "reemplaza por"; dijo NOva... jajajajajja
        # Si ya existe, actualizar
        if hasattr(self, "preview_window") and self.preview_window is not None:
            self.preview_window.update_panel(panel)
            self.preview_window.show()
        else:
            self.preview_window = GeckoPreviewPanel(panel, parent=self)
            self.preview_window.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
            geo = self.geometry()
            screen = QApplication.primaryScreen().availableGeometry()
            
            new_x = geo.x() + geo.width() + 10
            new_y = geo.y()
            
            if new_x + panel.width() > screen.right():
                new_x = geo.x() - panel.width() - 10
            self.preview_window.move(new_x, new_y)
            
            self.preview_window.show()
    
    # -----------------------------------------------------------------
    # --- I WORK ARROUND THIS AT END THE PROYECT... PLEASE WAIT!!!
    # -----------------------------------------------------------------
    def generate_layout(self):

        config = self._collect_config()

        widget_gen = WidgetGenerator(
            buttons=config["buttons"],
            dials=config["dials"],
            sliders=config["sliders"]
        )

        widgets = widget_gen.generate_all()

        all_widgets = (
            widgets["buttons"] +
            widgets["dials"] +
            widgets["sliders"]
        )

        layout_gen = LayoutGenerator(config["layout_type"])

        layout_code = layout_gen.generate_layout_code(all_widgets)

        panel_code = widget_gen.generate_python_panel("MySynthPanel")

        print("\n--- GENERATED PANEL ---\n")
        print(panel_code)
        print("\n--- GENERATED LAYOUT ---\n")
        print(layout_code)

# --- Ejecución Geckonica Clasica Pythonista y Efectiva ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GeckoLayoutMaker()
    ventana.show()
    sys.exit(app.exec_())