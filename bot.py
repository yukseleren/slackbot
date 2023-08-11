import slack
import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from slackeventsapi import SlackEventAdapter
from dynamic_form import create_incident as ci
from input_handler import interactive_endpoint as ie

#env_path = Path('.') / '.env'
#os.getenv ile path'i al

env_path = os.getenv(".env")
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])


@app.route('/slack/create_incident', methods=['POST'])
def run_dynamic_form():
    ci(client)
    return ""

@app.route('/slack/interactive', methods=['POST'])
def send_message():
    ie(client)
    return jsonify(), 204

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
