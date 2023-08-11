from flask import request

def create_incident(client):
    trigger_id = request.form.get('trigger_id')
    client.views_open(
        trigger_id=trigger_id,
        view={
            "type": "modal",
            "callback_id": "dynamic_form_submission",
            "title": {
                "type": "plain_text",
                "text": "SRE Incident Form"
            },
            "blocks": [
		{
			"type": "input",
            "block_id": "rest_uniq",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":knife_fork_plate: Restaurant Unique",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "Enter qlub restaurant unique ID",
					"emoji": True
				}
			]
		},
		{
			"type": "input",
            "block_id": "pos",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":desktop_computer: POS",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "Enter the POS that restaurant uses",
					"emoji": True
				}
			]
		},
		{
			"type": "input",
            "block_id": "table_id",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":chair: Table ID",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "If it's for all table, write 'All'",
					"emoji": True
				}
			]
		},
		{
			"type": "input",
            "block_id": "qr_link",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":qlubframe: QR Link",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "For more than one link, seperate with ','",
					"emoji": True
				}
			]
		},
		{
			"type": "input",
            "block_id": "issue_def",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":red_circle: Issue",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "Explain the issue in details",
					"emoji": True
				}
			]
		},
		{
			"type": "input",
            "block_id": "issue_date",
			"element": {
				"type": "datepicker",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				},
				"action_id": "datepicker-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":date: Date of the Issue",
				"emoji": True
			}
		},
		{
			"type": "input",
            "block_id": "issue_time",
			"element": {
				"type": "timepicker",
				"placeholder": {
					"type": "plain_text",
					"text": "Select time",
					"emoji": True
				},
				"action_id": "timepicker-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":clock1: Time of the Issue",
				"emoji": True
			}
		},
        
		{
			"type": "input",
            "block_id": "country_code",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select Country Code",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": ":flag-ae: AE",
							"emoji": True
						},
						"value": "AE"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": ":flag-au: AU",
							"emoji": True
						},
						"value": "AU"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": ":flag-br: BR",
							"emoji": True
						},
						"value": "BR"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": ":flag-sa: SA",
							"emoji": True
						},
						"value": "SA"
					},
					{
						"text": {
							"type": "plain_text",
							"text": ":flag-sg: SG",
							"emoji": True
						},
						"value": "SG"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":round_pushpin: Country Code",
				"emoji": True
			}
		}
	],
            "submit": {
                "type": "plain_text",
                "text": "Submit"
            }
        }
    )
    return ""