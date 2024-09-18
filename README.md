# python-atv-prototype
A prototype of ATV that ChatGPT o1 wrote in Python

Prompt: Using the Python programming language, create an equivalent astronomical FITS viewing program to the ATV program written in the Interactive Data Language (IDL). 

Thought for 18 seconds...
Crafting an alternative
The user wants a Python counterpart to IDL’s ATV program for FITS images. Since directly duplicating copyrighted software isn’t allowed, I’ll focus on providing a unique alternative.
Venturing into Python programming
Mapping out a Python program to display FITS images, using astropy, matplotlib, and interactive tools, while adhering to copyright standards.
Visualizing FITS images
I’m working through reading and displaying FITS images in Python, with features like adjusting contrast and zooming, using libraries such as astropy.io.fits and matplotlib.
Crafting the script
I’m piecing together a Python script to read and display a FITS file interactively. It’s fascinating to see how this will visualize data dynamically.
Handling FITS files
I’m opening a FITS file, checking its 2D image data, and setting up sliders for contrast and brightness adjustments using matplotlib widgets.
Evaluating Python tools
I’m mapping out Python libraries for a viewer, like PyQtGraph or matplotlib, and considering existing tools like Ginga or astropy for their interactive features and usability.
Setting up the environment
I’m installing PyQt5, PyQtGraph, and Astropy. These tools will be useful for working on the PyQt5 and PyQtGraph script.
Presenting FITS data
I’m working through a script that opens a FITS file, extracts 2D image data, and uses pyqtgraph’s ImageView widget to display it, ensuring interactive features like zooming and adjusting levels are available.

Certainly! Below is a Python program that serves as an equivalent astronomical FITS viewing tool similar to the ATV (Astronomical Visualization Tool) written in IDL. This program utilizes the `PyQt5` library for the graphical user interface and `pyqtgraph` for advanced image visualization capabilities. It allows you to open FITS files, view the images, zoom, pan, and adjust contrast and brightness interactively.

### Prerequisites

Before running the program, ensure you have the following Python packages installed:

```bash
pip install astropy pyqt5 pyqtgraph numpy
```

### The Code

```python
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
```

### How to Use the Program

1. **Run the Program:**

   Save the code above to a file named `fits_viewer.py`. You can run the program from the command line:

   ```bash
   python fits_viewer.py
   ```

   Optionally, you can provide a FITS file as an argument:

   ```bash
   python fits_viewer.py path_to_your_file.fits
   ```

2. **Opening a FITS File:**

   - If you didn't provide a FITS file as a command-line argument, you can open one using the menu:
     - Click on **File** in the menu bar.
     - Select **Open FITS File**.
     - Browse to your FITS file and open it.

3. **Interacting with the Image:**

   - **Zooming and Panning:**
     - Use the mouse wheel to zoom in and out.
     - Click and drag to pan around the image.
   - **Adjusting Contrast and Brightness:**
     - Right-click and drag horizontally to adjust the contrast.
     - Right-click and drag vertically to adjust the brightness.
   - **Reset View:**
     - Double-click on the image to reset the view to the original scale.

### Features

- **Interactive Visualization:**
  - The viewer uses `pyqtgraph`, which is optimized for fast image rendering and provides smooth interactive capabilities.
- **User-Friendly Interface:**
  - Menu options for opening files and exiting the application.
- **Error Handling:**
  - Displays error messages if the FITS file cannot be read or doesn't contain valid 2D image data.
- **Versatility:**
  - Can be launched without a FITS file and allows you to open files at any time during the session.

### Dependencies Explanation

- **astropy:** Used for reading FITS files.
- **PyQt5:** Provides the GUI elements.
- **pyqtgraph:** Offers advanced image viewing capabilities with interactive features.
- **numpy:** Handles numerical operations on image data.

### Customization

You can extend the program by adding features such as:

- **Region of Interest (ROI) Analysis:**
  - Add tools to select and analyze specific regions within the image.
- **Histogram Equalization:**
  - Implement additional image processing techniques to enhance image contrast.
- **Overlays and Annotations:**
  - Allow users to overlay grids, markers, or annotations on the image.

### Conclusion

This Python program serves as a starting point for an astronomical FITS viewer similar to ATV in IDL. It leverages powerful libraries to provide an interactive and efficient tool for visualizing astronomical data. Feel free to modify and extend the code to suit your specific needs.
