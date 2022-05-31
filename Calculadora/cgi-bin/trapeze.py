import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

#=--------- Calculo Area ---------+
base_maior = float(form.getvalue('base maior'))
base_menor = float(form.getvalue('base menor'))
altura = float(form.getvalue('altura'))
trapezio_area = (base_maior + base_menor) * altura / 2


title = "Trapézio"
funções.print_header(title)
print("<h1>Trapézio</h1><hr>")
print("<p>Base Maior: {:.1f}".format(base_maior))
print("<p>Base Menor: {:.1f}".format(base_menor))
print("<p>Altura: {:.1f}".format(altura))
print("<p>Área do trapezio: {:.1f}".format(trapezio_area))
print("<a href=\'../trapezio.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()

#=--------- Calculo Perimetro ---------+
base_maior = float(form.getvalue('base maior'))
base_menor = float(form.getvalue('base menor'))
lado1 = float(form.getvalue('lado1'))
lado2 = float(form.getvalue('lado2'))
trapezio_peri = base_maior + base_maior + lado1 + lado2


title = "Trapézio"
funções.print_header(title)
print("<h1>Trapézio</h1><hr>")
print("<p>Base Maior: {:.1f}".format(base_maior))
print("<p>Base Menor: {:.1f}".format(base_menor))
print("<p>Lado 1: {:.1f}".format(lado1))
print("<p>Lado 2: {:.1f}".format(lado2))
print("<p>Área do trapezio: {:.1f}".format(trapezio_peri))
print("<a href=\'../trapezio.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()