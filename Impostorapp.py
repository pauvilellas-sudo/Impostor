import random
from flask import Flask, request

app = Flask(__name__)

paraules = ["arbre", "casa", "llum", "porta", "finestra", "gat", "gos", "llibre", "escola", "taula", "cadira", "ordinador", "pantalla", "teclat", "ratolí", "programa", "codi", "joc", "impostor", "victòria", "derrota", "amic", "enemic", "somriure", "plor", "música", "cançó", "guitarra", "piano", "bateria", "veu", "ball", "dansa", "festa", "carrer", "plaça", "ciutat", "poble", "muntanya", "riu", "mar", "platja", "sorra", "onada", "barca", "vaixell", "avió", "tren", "cotxe", "bicicleta", "moto", "camí", "carretera", "pont", "túnel", "estació", "aeroport", "hotel", "habitació", "llit", "sofà", "cuina", "menjador", "bany", "dutxa", "lavabo", "sabó", "tovallola", "sabata", "jaqueta", "camisa", "pantaló", "faldilla", "gorra", "barret", "ulleres", "rellotge", "anell", "collaret", "bossa", "motxilla", "llibreta", "bolígraf", "llapis", "goma", "regla", "paper", "full", "quadern", "examen", "nota", "classe", "professor", "alumne", "estudi", "aprendre", "ensenyar", "pregunta", "resposta", "ciència", "matemàtiques", "física", "química", "biologia", "història", "geografia", "filosofia", "art", "pintura", "escultura", "fotografia", "imatge", "color", "forma", "línia", "cercle", "quadrat", "triangle", "rectangle", "estrella", "sol", "lluna", "planeta", "terra", "cel", "núvol", "pluja", "neu", "vent", "tempesta", "fred", "calor", "foc", "aigua", "aire", "pedra", "metall", "fusta", "ferro", "or", "plata", "coure", "vidre", "plàstic", "tela", "roba", "pell", "sang", "cor", "cervell", "mà", "peu", "dit", "cara", "ull", "boca", "nas", "orella", "cabell", "cos", "salut", "malaltia", "metge", "hospital", "farmàcia", "medicina", "pastilla", "vacuna", "sanglot", "crit", "silenci", "soroll", "paraula", "frase", "text", "llengua", "idioma", "català", "castellà", "anglès", "francès", "italià", "alemany", "xinès", "japonès", "coreà", "rus", "grec", "llatí", "escrit", "llegir", "parlar", "escoltar", "sentir", "veure", "mirar", "observar", "pensar", "recordar", "oblidar", "somiar", "imaginar", "crear", "inventar", "descobrir", "explorar", "viatjar", "caminar", "córrer", "saltar", "nedar", "pujar", "baixar", "obrir", "tancar", "encendre", "apagar", "menjar", "beure", "cuinar", "tastar", "pa", "arròs", "pasta", "carn", "peix", "verdura", "fruita", "poma", "pera", "plàtan", "taronja", "llimona", "maduixa", "raïm", "meló", "síndria", "cirera", "préssec", "albercoc", "kiwi", "mango", "pinya", "cafè", "te", "llet", "suc", "cervesa", "vi", "oli", "sal", "sucre", "mel", "xocolata", "galeta", "pastís", "pizza", "hamburguesa", "entrepà", "sopa", "amanida", "formatge", "iogurt", "mantega", "ou", "pollastre", "porc", "vedella", "xai", "bacallà", "tonyina", "salmó", "sardina", "gambes", "cloïsses", "musclos", "calamars", "pop", "aranya", "insecte", "abella", "mosca", "formiga", "papallona", "escarabat", "serp", "llangardaix", "tortuga", "granota", "ocell", "colom", "ànec", "gallina", "gall", "cavall", "vaca", "bou", "ovella", "cabra", "lleó", "tigre", "elefant", "girafa", "zebra", "rinoceront", "hipopòtam", "mico", "goril·la", "panda", "koala", "ós", "llop", "guineu", "ratolí", "conill", "esquirol", "eruga", "estel", "univers", "galàxia", "cometa", "asteroide", "satèl·lit", "telescopi", "astronauta", "coet", "espai", "temps", "segle", "any", "mes", "setmana", "dia", "hora", "minut", "segon", "rellotge", "calendari", "primavera", "estiu", "tardor", "hivern", "gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre", "dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge", "alegria", "tristesa", "ràbia", "por", "sorpresa", "confiança", "amor", "odi", "amistat", "enemistat", "pau", "guerra", "lluita", "esperança", "somni", "desig", "voluntat", "força", "energia", "poder", "màgia", "encant", "misteri", "secret", "veritat", "mentida", "realitat", "ficció", "fantasia", "aventura", "conte", "llegenda", "mite", "heroi", "vilà", "rei", "reina", "príncep", "princesa", "cavaller", "drac", "bruixa", "mag", "gegant", "monstre", "fantasma", "esperit", "àngel", "dimoni", "déu", "temple", "església", "mesquita", "sinagoga", "religió", "fe", "creença", "ritual", "pregària", "símbol", "icona", "bandera", "escut", "himne", "llei", "norma", "regla", "dret", "deure", "justícia", "llibertat", "igualtat", "fraternitat", "democràcia", "dictadura", "govern", "estat", "nació", "capital", "president", "alcalde", "ministre", "policia", "jutge", "advocat", "soldat", "economia", "diners", "banc", "moneda", "bitllet", "targeta", "crèdit", "deute", "inversió", "mercat", "comerç", "botiga", "supermercat", "producte", "preu", "oferta", "demanda", "treball", "feina", "empresa", "oficina", "fàbrica", "taller", "obrer", "enginyer", "arquitecte", "artista", "músic", "escriptor", "pintor", "actor", "cantant", "ballarí", "futbol", "bàsquet", "tennis", "pàdel"]

@app.route("/", methods=["GET"])
def home():
    return '''
        <h1>Joc de l'Impostor 🎭</h1>
        <form action="/jugar" method="post">
            Número de jugadors: <input type="number" name="num_jugadors" min="1">
            <button type="submit">Començar</button>
        </form>
    '''

@app.route("/jugar", methods=["POST"])
def jugar():
    num_jugadors = int(request.form["num_jugadors"])
    paraula_random = random.choice(paraules)
    resultat = "<h2>Resultats del joc:</h2><ul>"

    impostor_dit = False
    for i in range(num_jugadors):
        if random.randint(1, 3) == 1:
            impostor_dit = True
            resultat += f"<li>Jugador {i+1}: <b>IMPOSTOR</b></li>"
        else:
            resultat += f"<li>Jugador {i+1}: {paraula_random}</li>"
        impostor_dit = False

    resultat += "</ul><a href='/'>Tornar a jugar</a>"
    return resultat

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
