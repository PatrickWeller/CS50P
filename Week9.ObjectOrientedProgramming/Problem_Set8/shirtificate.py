##### shirtificate.py #####

# Suppose that you’d like to implement a CS50 “shirtificate,”
# a PDF with an image of an I took CS50 t-shirt, shirtificate.png,
# customized with a user’s own name.

# In a file called shirtificate.py,
# implement a program that prompts the user for their name and outputs,
# using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf
# with these specifications:

# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text,
    # centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.
# All other details we leave to you.
# You’re even welcome to add borders, colors, and lines.
# And no need to wrap long names across multiple lines.

# Before writing any code, do read through fpdf2’s tutorial
# to learn how to use it.
# Then skim fpdf2’s API (application programming interface)
# to see all of its functions and parameters therefor.

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def header(self):
        # Setting font: helvetica bold 40
        self.set_font("helvetica", "B", 40)
        # Printing title:
        self.cell(190, 40, "CS50 Shirtificate", align="C")
        # Line break:
        self.ln(20)
        # insert image
        self.image("shirtificate.png", 10, 60, 190)
        # Setting font: helvetica 16
        self.set_font("helvetica", "B", 20)
        # Printing title:
        self.cell(190, 180, f"{self.name} took CS50", align="C")


name = input("Name: ")
pdf = PDF(name)
pdf.add_page()
pdf.output("shirtificate.pdf")
