from fpdf import FPDF


def main():
    pdf = FPDF()
    pdf.add_page()
    pdf = title_text(pdf)
    pdf = paste_image(pdf)
    pdf = paste_name(input("Name: "), pdf)
    pdf.output("shirtificate.pdf")


def title_text(f):
    f.set_font("Arial", style="B", size=40)
    f.cell(80)
    f.cell(30, 40, "CS50 Shirtificate", align="C")
    return f


def paste_image(f):
    f.image("shirtificate.png", x=10, y=60 ,w=190, h=200)
    return f


def paste_name(s, f):
    f.set_font("Arial", size=25)
    f.set_text_color(255, 255, 255)
    f.cell(-30, 235, f"{s} took CS50", align="C")
    return f


main()
