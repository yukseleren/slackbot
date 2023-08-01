import slack_sdk
import os
import ssl
import certifi
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response, make_response
from slackeventsapi import SlackEventAdapter
import json

ssl_context = ssl.create_default_context(cafile=certifi.where())
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events',app)



client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'],ssl=ssl_context)

BOT_ID = client.api_call("auth.test")['user_id']
restaurants = ["rest1", "rest2", "rest3"]
threads_to_reply = []
@app.route("/slack/messages", methods =["POST"])
def messages():
        # Parse the request payload
    form_json = json.loads(request.form["payload"])

    # Check to see what the rest was and update the message
    selection = form_json["actions"][0]["action_id"]
    print(selection)
    if selection == "rest1":
        print("a")
        message_text = "1"
    elif selection == "rest2":
        print("b")
        message_text = "2"
    else:
        print("c")
        message_text = "3"

    client.chat_postMessage(channel=form_json["channel"]["id"],thread_ts=form_json["container"]["thread_ts"],text=message_text)
    # response = client.api_call(
    # "chat.update",
    # channel=form_json["channel"]["id"],
    # ts='1690399233.101759',
    # text=message_text,
    # attachments=[]
    # )
    return make_response("",200)
@slack_event_adapter.on('message')
def message(payload):

    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id= event.get('user')
    thread = event.get('ts')
    text = event.get('text')
    if user_id != BOT_ID and user_id != None:
        if text in restaurants:
            threads_to_reply.append(thread)
            client.chat_postMessage(channel=channel_id, thread_ts=thread, text=text[0], blocks=[
            {
                "type": "actions",
                
                "elements": [
                    {  
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Details"
                        },
                        "value" : "burda",
                        "action_id": text
                    }
                ]
            }
        ])
    
        
                        # blocks =  [ 
                        #             {
                        #             "type": "section",
                        #             "text" :{   
                        #                 "type" : "mrkdwn",
                        #                 "text":'yavuz naber ya'
                                        
                        #                 }
                        #             }
                        #         ]
                        
                        #         )
if __name__ == "__main__":
    app.run(debug=True)
    # ,
    #                                 {
    #                                     "type" : "divider"
    #                                 },
    #                                 {
    #                                     "type" : "actions",
    #                                     "elements" : [
    #                                         {
    #                                             "type" : "button",
    #                                             "text" : "Detailed information for the rest",
    #                                             "value" : "details",
    #                                             "confirm" : print("selam")
    #                                         }
    #                                     ]
    #                                 }

