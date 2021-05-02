from fpdf import FPDF
import os
import re

from scipy.signal.spectral import spectrogram


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297

    def header(self):
        # Custom logo and positioning
        # Create an `assets` folder and put any wide and short image inside
        # Name the image `logo.png`
        # 10 distance from left   8 distance from top   33 size


        self.set_font('helvetica', 'B', 15)
        self.cell(self.WIDTH - 142)
        self.cell(60, 1, 'Multi-Channel Biological Signals Report', 0, 0, 'C')
        self.ln(20)
#

    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def page_body(self, images, PLOT_DIR):
        self.image(PLOT_DIR + '/' + images[0], 15, 30, self.WIDTH - 30)
        self.image(PLOT_DIR + '/' + images[1], 15, self.WIDTH / 2 + 20, self.WIDTH - 30)


    def print_page(self, images, PLOT_DIR):
        # Generates the report
        self.add_page()
        self.page_body(images, PLOT_DIR)

    def construct(self, PLOT_DIR):
        pages_data = []
        # Get all plots
        plots = os.listdir(PLOT_DIR)
        # Sort them by month - a bit tricky because the file names are strings
        plots = sorted(os.listdir(PLOT_DIR),
                       key=lambda x: x.split('.')[0])
        pages_data=[plots[0], plots[1]]
        return [*pages_data]
