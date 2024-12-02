## 
## Do poprawy - wysokość czcionki na podstawie szerokosci danej linii (teraz sama wysokosc sprawdza)
## Zrobić wersję serwerową albo EXE
## Polskie znaki
## Dodac IF, ze jesli linijka jest nie pusta to dodaje \n na koniec
##
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import red
# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
# Zdefiniuj wymiary ramki
frame_width = 11 * cm
frame_height = 2 * cm

# TEXT:
text1="Do wykonania prototypu. Dotyczy poleceń:   \n"
## Wpis max 2 numery poleceń
text2="PT/24/906/0201\n"
## Wpis max 2 numery poleceń
text3=""
## Wpis max 2 numery poleceń
text4=""                                      
## Wpis max 2 numery poleceń
text5=""
## Wpis max 2 numery poleceń
text6=""
## Ustaw date:
text7="Zgodność z oryginałem  |  2024-11"
text = text1+text2+text3+text4+text5+text6+text7

# Zdefiniuj rozmiar czcionki
font_size = 15
# Zwiekszanie wysokosci
if text5 != "":
    frame_height = frame_height + font_size
if text6 != "":
    frame_height = frame_height + font_size
if text7 != "":
    frame_height = frame_height + font_size

##----------------------------------------------------------------------
# Utwórz obiekt canvas
c = canvas.Canvas("D:/Programming Projects/PIECZATKA1.pdf", pagesize=A4)
# Zarejestruj czcionkę obsługującą polskie znaki
pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

# Zdefiniuj pozycję ramki (wyśrodkowaną na stronie)
x = (A4[0] - frame_width) / 2
y = (A4[1] - frame_height) / 2

# Ustaw kolor ramki na czerwony i narysuj ramkę
c.setStrokeColor(red)
c.rect(x, y, frame_width, frame_height)
c.rect(x+2, y+2, frame_width-4, frame_height-4)



# Ustaw czcionkę, rozmiar i kolor na czerwony
c.setFont("Arial", font_size)
c.setFillColor(red)

# Podziel tekst na linie
lines = text.split('\n')
lines_no = len(lines)

# Oblicz szerokość i wysokość tekstu
text_height = font_size * len(lines)

# Dostosuj rozmiar czcionki, jeśli tekst jest zbyt wysoki dla ramki
while text_height > frame_height - 0.4 * cm:
    font_size -= 1
    c.setFont("Arial", font_size)
    text_height = font_size * len(lines)

# Narysuj tekst wewnątrz ramki (wyśrodkowany)
for i, line in enumerate(lines):
    text_width = c.stringWidth(line, "Arial", font_size)
    text_x = x + (frame_width - text_width) / 2
    text_y = y + frame_height - (i + 1) * font_size - (frame_height - text_height) / 2
    c.drawString(text_x, text_y, line)

# Zapisz plik PDF
c.save()

print("Plik PDF 'output.pdf' został pomyślnie utworzony.")