from templates import MessageTemplate

def format_message(client, payload, restaurant_unique, pos, table_id, qr_link, issue_def, country_code, issue_date, issue_time):

    msg = MessageTemplate(client, payload, restaurant_unique, pos, table_id, qr_link, issue_def, country_code, issue_date, issue_time)

    client.chat_postMessage(
            channel='#test',
            blocks = msg["blocks"]            
    )