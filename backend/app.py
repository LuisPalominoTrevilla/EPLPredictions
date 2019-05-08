from flask import Flask
from flask import Response
from flask import request
from flask_cors import CORS
from predict import whoWins
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def api():
    return "API is alive"

@app.route("/predictOne", methods=["POST"])
def predictOne():
    body = request.json
    matchResult = whoWins(body['home'], body['away'])
    matchResult['homeLogo'] = matchResult['homeTeam'].replace(" ", "")+".png"
    matchResult['awayLogo'] = matchResult['awayTeam'].replace(" ", "")+".png"
    return Response(json.dumps(matchResult), content_type='application/json; charset=utf-8')