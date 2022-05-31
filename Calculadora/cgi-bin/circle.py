import cgitb, cgi
import math
import funções

cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
#--- logica do script ---#

raio1 = float(form.getvalue('raio'))
circulo_area = math.pi * math.pow(raio1, 2)

#--- HTML ---#
title = "Círculo"
funções.print_header(title)
print("<h1>Circulo</h1><hr>")
print("<p>Raio: {:.1f}".format(raio1))
print("<p>Area do circulo: {:.1f}".format(circulo_area))
print("<a href=\'../circulo.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()

raio2 = float(form.getvalue('raio'))
circulo_peri = 2 * math.pi * raio2

#--- HTML ---#
title = "Círculo"
funções.print_header(title)
print("<h1>Circulo</h1><hr>")
print("<p>Raio: {:.1f}".format(raio2))
print("<p>Perimetro do circulo: {:.1f}".format(circulo_peri))
print("<a href=\'../circulo.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()