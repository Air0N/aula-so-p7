import cgitb, cgi
import funções

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

#=--------- Calculo Area ---------+
base = float(form.getvalue('base'))
altura = float(form.getvalue('altura'))
retangulo_area = base * altura


title = "Retângulo"
funções.print_header(title)
print("<h1>Retângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base))
print("<p>Altura: {:.1f}".format(altura))
print("<p>Área do retângulo: {:.1f}".format(retangulo_area))
print("<a href=\'../retangulo.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()

#=--------- Calculo Perimetro ---------+
base = float(form.getvalue('base'))
altura = float(form.getvalue('altura'))
retangulo_peri = (base * 2) + (altura * 2)


title = "Retângulo"
funções.print_header(title)
print("<h1>Retângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base))
print("<p>Altura: {:.1f}".format(altura))
print("<p>Perimetro do retângulo: {:.1f}".format(retangulo_peri))
print("<a href=\'../retangulo.html\'><button class='buttom'>Novo Calculo</button></a>")
funções.print_footer()
