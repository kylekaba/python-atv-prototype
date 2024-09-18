import sys
import numpy as np
from astropy.io import fits
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

class FitsViewer(QtWidgets.QMainWindow):
    def __init__(self, fits_file=None):
        super().__init__()
        self.setWindowTitle('FITS Viewer')
        self.resize(800, 600)
        self.image_data = None

        # Create the main widget and layout
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)

        # Create ImageView widget
        self.view = pg.ImageView()
        self.layout.addWidget(self.view)

        # Create a menu bar
        self.create_menu()

        # If a FITS file is provided, open it
        if fits_file:
            self.open_fits(fits_file)

    def create_menu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        # Open File action
        openFile = QtWidgets.QAction('Open FITS File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.open_file_dialog)
        fileMenu.addAction(openFile)

        # Exit action
        exitApp = QtWidgets.QAction('Exit', self)
        exitApp.setShortcut('Ctrl+Q')
        exitApp.triggered.connect(QtWidgets.qApp.quit)
        fileMenu.addAction(exitApp)

    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        fits_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open FITS File', '', 'FITS Files (*.fits);;All Files (*)', options=options)
        if fits_file:
            self.open_fits(fits_file)

    def open_fits(self, fits_file):
        try:
            # Read FITS data
            hdu_list = fits.open(fits_file)
            image_data = hdu_list[0].data
            hdu_list.close()

            # Check if data is 2D
            if image_data.ndim != 2:
                raise ValueError("FITS file does not contain 2D image data.")

            self.image_data = image_data

            # Set image data
            self.view.setImage(self.image_data)
            self.setWindowTitle(f'FITS Viewer - {fits_file}')

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error', str(e))

def main():
    fits_file = None
    if len(sys.argv) == 2:
        fits_file = sys.argv[1]

    app = QtWidgets.QApplication(sys.argv)
    viewer = FitsViewer(fits_file)
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
