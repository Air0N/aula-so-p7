import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

#=--------- Calculo Area ---------+
base = float(form.getvalue('base'))
altura = float(form.getvalue('altura'))
triangulo_area = (base * altura) / 2

title = "Triangulo"
funções.print_header(title)
print("<h1>Triangulo</h1><hr>")
print("<p>Base: {:.1f}".format(base))
print("<p>Altura: {:.1f}".format(altura))
print("<p>Área do Triangulo: {:.1f}".format(triangulo_area))
print("<a href=\'../triangulo.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()

#=--------- Calculo Perimetro ---------+
base = float(form.getvalue('base'))
lado1 = float(form.getvalue('lado1'))
lado2 = float(form.getvalue('lado2'))
triangulo_peri = base + lado1 + lado2

title = "Triangulo"
funções.print_header(title)
print("<h1>Triangulo</h1><hr>")
print("<p>Base: {:.1f}".format(base))
print("<p>Lado 1: {:.1f}".format(lado1))
print("<p>Lado 2: {:.1f}".format(lado2))
print("<p>Perimetro do Triangulo: {:.1f}".format(triangulo_peri))
print("<a href=\'../triangulo.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()
