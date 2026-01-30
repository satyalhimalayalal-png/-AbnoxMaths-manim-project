from fpdf import FPDF

# Words/phrases list
phrases = [
    ("Playful",),
    ("Grumpy",),
    ("Toxic",),
    ("Argumentative", "Confrontations"),
    ("Uncooperative",),
    ("Cooperative",),
    ("Happiness",)
]

# Constants
font_size = 100
page_width = 297  # A4 landscape width in mm
page_height = 210  # A4 landscape height in mm

# Custom PDF class
class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

# Create the PDF
pdf = PDF(orientation="L", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)

# Add each phrase to its own page
for phrase in phrases:
    pdf.add_page()
    pdf.set_font("Arial", "B", font_size)
    pdf.set_text_color(0, 0, 0)

    total_lines = len(phrase)
    line_spacing = 20
    total_text_height = font_size * total_lines + (total_lines - 1) * line_spacing
    y_start = (page_height - total_text_height) / 2

    for idx, line in enumerate(phrase):
        pdf.set_xy(0, y_start + idx * (font_size + line_spacing))
        pdf.cell(page_width, font_size + 5, line, ln=True, align="C")

# Output file
pdf.output("final_with_happiness.pdf")