from bottle import route, run

@route("/cosas/<cosa>")
def cosas(cosa):
    return f"<h1>hola {cosa} </h>"

run(host='localhost', port=8080, debug=True)