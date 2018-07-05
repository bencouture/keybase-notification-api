#!flask/bin/python

from flask import Flask, request, jsonify, abort
from subprocess import call
import os

app = Flask(__name__)

@app.route("/send", methods=["POST"])
@app.route("/1/<something>", methods=["POST"])
def send_message(something):
	username = os.environ["KEYBASE_USERNAME"]
	if request.json is not None:
		if request.json["user"]:
			username = request.json["user"]
		message = request.json['message']
	elif request.form is not None:
		if request.form["user"]:
			username = request.form["user"]
		message = request.form['message']
	else:
		raise AssertionError
	call(["keybase", "chat", "send", username, message])
	return 'OK'

@app.route("/sonarr", methods=["POST"])
def send_sonarr():
	username = os.environ["KEYBASE_USERNAME"]
	series = request.json['Series']['Title']
	seasonNumber = str(request.json['Episodes'][0]['SeasonNumber']) 
	episodeNumber = str(request.json['Episodes'][0]['EpisodeNumber']) 
	episodeTitle = request.json['Episodes'][0]['Title']
	message = series + " s" + seasonNumber + "e" + episodeNumber + " - " + episodeTitle
	
	call(["keybase", "chat", "send", username, message])
	return 'OK'

if __name__ == '__main__':
	app.run(port=int("4433"),host='0.0.0.0',debug=True)
