#GeckoPreviewPanel
#────────────────────────────────────────
"""
Ventana simple para visualizar panels generados
por GeckoLayoutMaker.

Recibe un QWidget ya construido y lo muestra
dentro de un contenedor con layout limpio.

Modo de uso:

    panel = MySynthPanel()
    preview = GeckoPreviewPanel(panel)
    preview.show()
"""

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt5.QtGui import QColor


class GeckoPreviewPanel(QWidget):

    def __init__(self, panel_widget, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Gecko Preview Panel")
        self.current_panel = panel_widget

        # -----------------------------------------------------
        # Saco el estilo porque me genera problemas de previsualización 16/03/26 08:53
        '''
        self.panel_widget.setStyleSheet("""
            background-color: #202020;
            border: 2px solid #404040;
            padding: 10px;
        """)
        '''
        # -----------------------------------------------------

         # Colores Compatibles tema MIT
        self.color_fondo_oscuro = QColor("#19232d")
        self.color_fondo_claro = QColor("#fafafa")
        self.color_text_claro = QColor("#fafafa")
        self.color_fondoinstrumento_claro = QColor("#a9a9a9")
        self.color_fondoinstrumento_Oscuro = QColor("#19232d")
        # Colores Tema RadarSpok for GeckoMoog
        self.color_on = QColor("#00FF44")   
        self.color_off = QColor("#A30000")  
        self.color_star = QColor("#FFFFFF") 
        self.color_text = QColor("#00CC33") 
        self.color_btn_on = QColor("#00ffaa") 
        self.color_btn_off = QColor("#B30000") 
        self.color_btn_pause = QColor("#DDB800") 
        self.color_btn_play = QColor("#00ffaa")  
        
        '''
        # Aplico el EStilo GeckoMoog
        self.panel_widget.setStyleSheet("""
            QWidget {
            background-color: #19232d;
            /*border: 2px solid #00ffaa;*/
            padding: 10px;
            }
            QTextEdit {
                background-color: black;
                color: #0f8;
                font: 10pt Consolas;
                font-weight: bold;
                font-size: 12px;
            }                           
            QLabel {
                color: #ccc;
                font-weight: normal;
            }
            QPushButton {
                background-color: #19232d;
                color: #0f8;
                border: 2px solid #00ffaa;
                border-radius: 13px;
                font-size: 11px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #454545;
                color: #0f8;
                border: 1px solid #0f8;
            }
            QPushButton:checked {
                background-color: #00ffaa;
                color: #000;
                border: 2px solid #0f8;
            }
            QPushButton:pressed {
                background-color: #00ffaa;
                color: #000;
                border: 2px solid #0f8;
            }
            QDial {
                background-color: #222;
                color: #0f8;
            }
            QDial::groove {
                border: 1px solid #444;
                border-radius: 40px;
            }
            QDial::handle {
                background: qradialgradient(cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5,
                                            stop:0 #0f8, stop:1 #084);
                width: 18px;
                height: 18px;
                border: 2px solid #0f8;
                border-radius: 9px;
            }
            QGroupBox {
                font: 10pt Consolas;
                font-weight: normal;
                border-radius: 13px;
                margin-top: 5px;
            }
            QGroupBox::title {
                font: bold 12pt Consolas;
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding-left: 13px;
                color: #0f8;
            }                           
        """)
        '''
        
        self._build_ui()

    
    # ----------------------------------------------------------------------------
    # Construccion del Preview con el Panel Diseñado Minimalismo Geckonico Vulkano
    # ----------------------------------------------------------------------------
    def _build_ui(self):
        self.container_layout = QVBoxLayout()
        title = QLabel("Gecko Layout Preview")
        title.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
            padding:6px;
        """)
        self.container_layout.addWidget(title)
        # panel generado
        #self.container_layout.addWidget(self.panel_widget)
        self.container_layout.addWidget(self.current_panel)
        # espacio final
        self.container_layout.addStretch()
        
        self.setLayout(self.container_layout)

    # ----------------------------------------------------------------------------
    # 
    # ----------------------------------------------------------------------------
    def update_panel(self, new_panel):
        if self.current_panel is not None:
            self.container_layout.removeWidget(self.current_panel)
            self.current_panel.setParent(None)
            self.current_panel.deleteLater()

        self.current_panel = new_panel
        self.container_layout.insertWidget(1, self.current_panel)

    # Salida Geckonica    
    def closeEvent(self, event):
        # Opcional: podrías simplemente ocultarlo en vez de destruirlo
        self.hide()
        event.ignore()
        #super().closeEvent(event)