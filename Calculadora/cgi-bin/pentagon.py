import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

#=--------- Calculo Area ---------+
perimetro = float(form.getvalue('perimetro'))
apotema = float(form.getvalue('apotema'))
lado = float(form.getvalue('lado'))

pentagono_area = perimetro * apotema

title = "Pentagono"
funções.print_header(title)
print("<h1>Pentagono</h1><hr>")
print("<p>Perimetro: {:.1f}".format(perimetro))
print("<p>Apótema: {:.1f}".format(apotema))
print("<p>Lado: {:.1f}".format(lado))
print("<p>Área do Pentagono: {:.1f}".format(pentagono_area))
print("<a href=\'../pentagono.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()

#=--------- Calculo Perimetro ---------+
pentagono_peri = lado * 5

title = "Pentagono"
funções.print_header(title)
print("<h1>Pentagono</h1><hr>")
print("<p>Lado: {:.1f}".format(perimetro))
print("<p>Perímetro do Pentagono: {:.1f}".format(pentagono_peri))
print("<a href=\'../pentagono.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()