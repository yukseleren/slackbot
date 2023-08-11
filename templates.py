def MessageTemplate(client, payload, restaurant_unique, pos, table_id, qr_link, issue_def, country_code, issue_date, issue_time):

    msg_template = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":rotating_light: New Issue Has Arrived",
                    } 
                },
                {
                "type": "divider"
                },
                
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Restaurant Unique ID:*\n" + restaurant_unique
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*POS:*\n" + pos
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Table ID:*\n" + table_id
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Country Code:*\n" + country_code
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Issue Date:*\n" + issue_date
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Issue Time:*\n" + issue_time
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                    "type": "mrkdwn",
                    "text": "*Issue:* " + issue_def
                    }
                },
                {
                    "type": "section",
                    "text": {
                    "type": "mrkdwn",
                    "text": "*QR Link:* " + qr_link
                    }
                },
                {
                    "type": "actions",
                
                    "elements": [
                    {  
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Get Restaurant Details"
                        },
                        "value" : "Detail",
                        "action_id": restaurant_unique
                    }
                    ]
                },
                {
                    "type": "actions",
                
                    "elements": [
                    {  
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Get Payment"
                        },
                        "value" : "Payment",
                        "action_id": pos
                    }
                    ]
                },
                {
                    "type": "actions",
                
                    "elements": [
                    {  
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Get Table"
                        },
                        "value" : "Table",
                        "action_id": table_id
                    }
                    ]
                }

            ]
    }
    return msg_template