from flask import request, json
from msg_sender import format_message
def func(input):
    return input

def interactive_endpoint(client):
    payload = request.form.get('payload')
    payload = json.loads(payload)
   


    if payload["type"] == "view_submission":
        values = payload["view"]["state"]["values"]
        
        #Set variables
        restaurant_unique = values["rest_uniq"]["plain_text_input-action"]["value"]
        pos = values["pos"]["plain_text_input-action"]["value"]
        table_id = values["table_id"]["plain_text_input-action"]["value"]
        qr_link = values["qr_link"]["plain_text_input-action"]["value"]
        issue_def = values["issue_def"]["plain_text_input-action"]["value"]
        country_code = values["country_code"]["static_select-action"]["selected_option"]["text"]["text"]
        issue_date = values["issue_date"]["datepicker-action"]["selected_date"]
        issue_time = values["issue_time"]["timepicker-action"]["selected_time"]

        format_message(client, payload, restaurant_unique, pos, table_id, qr_link, issue_def, country_code, issue_date, issue_time)

    if payload["type"] == 'block_actions':
        print(payload)
        button=payload["actions"][0]["value"]
        
        selection = payload["actions"][0]["action_id"]
        match button:
            case "Detail":
                message_text=func(selection)
            case "Table":
                message_text=func(selection)
            case "Payment":
                message_text=func(selection)
        # Check to see what the rest was and update the message
        
        client.chat_postMessage(channel=payload["channel"]["id"],thread_ts=payload["container"]["message_ts"],text=message_text)
        #client.chat_update(channel=payload["channel"]["id"],ts=payload["container"]["message_ts"],blocks=[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}])
    return ""