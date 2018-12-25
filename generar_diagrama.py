#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from odf.opendocument import OpenDocumentChart, OpenDocumentText
from odf import chart, style, table, text, draw

from odf.opendocument import OpenDocumentDrawing
from odf.style import Style, MasterPage, PageLayout, PageLayoutProperties, GraphicProperties, DrawingPageProperties, TextProperties, GraphicProperties, ParagraphProperties, DrawingPageProperties
from odf.draw import Page, G, Polygon, Rect, Frame, TextBox, Image
from odf.text import P


doc = OpenDocumentDrawing()

##### Estilos de pagina

# Create the drawing page
dpstyle = Style(family="drawing-page",name="DP1")
dpstyle.addElement(DrawingPageProperties(backgroundsize="border", fill="none"))
doc.automaticstyles.addElement(dpstyle)

# Create page layout specifying dimensions
plstyle = PageLayout(name="PM1")
plstyle.addElement(PageLayoutProperties(margin="0cm", pageheight="400mm", pagewidth="500mm", printorientation="portrait"))
doc.automaticstyles.addElement(plstyle)

# Create a master page
masterpage = MasterPage(stylename=dpstyle, name="Default", pagelayoutname=plstyle)
doc.masterstyles.addElement(masterpage)

# Create a page to contain the drawing
drawpage = Page(masterpagename=masterpage, name="page1", stylename=dpstyle)
doc.drawing.addElement(drawpage)

#### Estilos de texto
textStyle = Style(name="texto", family="graphic")
textStyle.addElement(ParagraphProperties(textalign="left"))
textStyle.addElement(TextProperties(fontsize="3mm", color="#000000", fontfamily="Roboto"))
textStyle.addElement(GraphicProperties(fillcolor="none", fill="none", stroke="none"))
doc.styles.addElement(textStyle)


titleStyle = Style(name="titulo", family="graphic")
titleStyle.addElement(ParagraphProperties(textalign="center"))
titleStyle.addElement(TextProperties(fontsize="9mm", color="#000000", fontfamily="Roboto"))
titleStyle.addElement(GraphicProperties(fillcolor="none", fill="none", stroke="none"))
doc.styles.addElement(titleStyle)



lukaStyle = Style(family="graphic", name="luka")
lukaStyle.addElement(GraphicProperties(fill="solid", fillcolor="#bbffbb", strokecolor="#000000", strokewidth="0.1mm"))
doc.automaticstyles.addElement(lukaStyle)

paloStyle = Style(family="graphic", name="palo")
paloStyle.addElement(GraphicProperties(fill="solid", fillcolor="#ffaaaa", strokecolor="#000000", strokewidth="0.1mm"))
doc.automaticstyles.addElement(paloStyle)


paloverdeStyle = Style(family="graphic", name="paloverde")
paloverdeStyle.addElement(GraphicProperties(fill="solid", fillcolor="#6666ff", strokecolor="#000000", strokewidth="0.1mm"))
doc.automaticstyles.addElement(paloverdeStyle)

billonverdeStyle = Style(family="graphic", name="billon")
billonverdeStyle.addElement(GraphicProperties(fill="solid", fillcolor="#33ff33", strokecolor="#000000", strokewidth="0.1mm"))
doc.automaticstyles.addElement(billonverdeStyle)


maximas_cajitas_por_linea = 25
distancia_entre_cajitas = 0.5
margen = 10
margen_superior = 40
start_y = margen_superior


def cajas(cantidad, texto, style, offset_x=0, offset_y=0):
	global start_y, margen, margen_superior
	group=G()
	drawpage.addElement(group)
	for i in range(cantidad):
		x = margen +offset_x +  (i % maximas_cajitas_por_linea)*(1+distancia_entre_cajitas)
		y = start_y + offset_y + (math.floor(i/maximas_cajitas_por_linea)) * (1+distancia_entre_cajitas)
		group.addElement(Rect(height="1mm", width="1mm", x="{}mm".format(x), y="{}mm".format(y), stylename=style))
	x = margen + maximas_cajitas_por_linea * (1+distancia_entre_cajitas)
	titleframe = Frame(stylename=textStyle, width="60mm", height="10mm", x="{}mm".format(x + 8 + offset_x), y="{}mm".format(start_y + 0 - 2))
	group.addElement(titleframe)
	textbox = TextBox()
	titleframe.addElement(textbox)
	textbox.addElement(P(text=texto))
	start_y += (math.floor(cantidad/maximas_cajitas_por_linea)) * (1+distancia_entre_cajitas) + 4
	height = (math.ceil(cantidad/maximas_cajitas_por_linea)) * (1+distancia_entre_cajitas) + 4
	return height


def lukas(cantidad, texto, offset_x=0, offset_y=0):
	return cajas(cantidad, texto, lukaStyle, offset_x, offset_y)

def palos(cantidad, texto, offset_x=80, offset_y=0):
	return cajas(cantidad, texto, paloStyle, offset_x, offset_y)

def palos_verdes(cantidad, texto, offset_x=200, offset_y=0):
	return cajas(cantidad, texto, paloverdeStyle, offset_x, offset_y)

def billones_verdes(cantidad, texto, offset_x=310, offset_y=0):
	return cajas(cantidad, texto, billonverdeStyle, offset_x, offset_y)


# Acá empezamos a dibujar los cuadraditos
lukas(2, "Comerse un completo")
lukas(70, "Una bicicleta")
lukas(188, u"Sueldo Mínimo")
lukas(250, u"Playstation")
lukas(600, u"Sueldo Promedio")
offset = lukas(1000, u"1 Palo = ")

start_y -= offset
palos(1, u"", 65)

start_y = margen_superior
palos(1, u"1 Palo")
palos(1, u"Sueldo Secretaria")
palos(4, u"Sueldo Ejecutivo")
palos(9, u"Sueldo Gerente")
palos(14, u"Asignación mensual de un parlamentario")
palos(30, u"Sueldo Gerente Corporación")
#palos(24, u"Costo mensual de un diputado")
#palos(31, u"Costo mensual de un senador")

palos(60, u"Departamente 1 ambiente en Santiago")

palos(296, u"Costo anual de un diputado")
palos(374, u"Costo anual de un senador")

offset = palos(670, u"1 Palo Verde = ")
start_y -= offset
palos_verdes(1, u"", 150 )

start_y = margen_superior
palos_verdes(1, u"1 Palo Verde")
palos_verdes(4, u"La media casa en La Dehesa")
palos_verdes(53, u"Presupuesto anual del Hogar de Cristo")
palos_verdes(182, u"Costo anual del Congreso")
palos_verdes(211, u"Presupuesto anual Junji")
palos_verdes(448, u"Presupuesto anual del Sename")
palos_verdes(650, u"Ley reservada del cobre")
palos_verdes(780, u"Aporte anual por déficit Transantiago")
offset = palos_verdes(1000, u"1000 millones de USD = ")


start_y -= offset
billones_verdes(1, u"",283 )


start_y = margen_superior
billones_verdes(1, u"1000 millones de USD")
billones_verdes(1, u"Aporte anual de Codelco")
billones_verdes(1, u"Costo anual licitación Junaeb")
billones_verdes(3, u"Patrimonio de Ponce Lerou")
billones_verdes(3, u"Costo anual Gratuidad educación superior")
billones_verdes(4, u"Costo anual reforma de pensiones Piñera")
billones_verdes(4, u"Patrimonio de Horst Paulmann")
billones_verdes(14, u"Patrimonio de Andronico Luksic")
billones_verdes(60, u"Gasto público anual del estado")
billones_verdes(150, u"Patrimonio de Jeff Bezos")
billones_verdes(170, u"Inversiones del sistema de AFPs")
billones_verdes(223, u"PIB anual de Chile")


group=G()
drawpage.addElement(group)
titleframe = Frame(stylename=titleStyle, width="240mm", height="30mm", x="80mm", y="10mm")
group.addElement(titleframe)
textbox = TextBox()
titleframe.addElement(textbox)
textbox.addElement(P(text="Riqueza en Chile"))



doc.save("diagrama-de-riquezas-en-Chile", True)
