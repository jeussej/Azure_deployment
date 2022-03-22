from bottle import route, run

@route("/cosas/<cosa>")
def cosas(cosa):
    saludo = "Hola,"
    return saludo + str(cosa)

run(host='localhost', port=8080, debug=True)