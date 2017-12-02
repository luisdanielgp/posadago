import requests

class Respuestas():
	def saluda(self,sender_id):
		JSON = {"messaging_type": "RESPONSE",
		"recipient":{
		"id":sender_id
		},
		"message":{
  		"text":"holi!"
			}
		}
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAGUKgfuKVgBAO6al1gRHwzEEH9Hq886Ko4hBHINcQeHiNroxWTPdYkNH1ZCTIUqZAnMu2ZAhINpBTNZCnSc5sXh2RdL7GSnHQStoTvAZBZCM948J38dxZBGHXj2RuZBj604CqMVzHkl0VZCbWnfSZAD9KyM1cAvFtZA0oWIIXZC2cSs7QZDZD'
		respuesta = requests.post(URL,json = JSON)
		print(respuesta)

	def quick(sel,sender_id):
		JSON = {
  "recipient":{
    "id":sender_id
  },
  "message":{
    "text": "Here's a quick reply!",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Search",
        "payload":"POSTBACK_IMAGE",
        "image_url":"https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg"
      },
      {
        "content_type":"location"
      },
      {
        "content_type":"text",
        "title":"Something Else",
        "payload":"POSTBACK_TEXT"
      }
    ]
  }
}
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAGUKgfuKVgBAO6al1gRHwzEEH9Hq886Ko4hBHINcQeHiNroxWTPdYkNH1ZCTIUqZAnMu2ZAhINpBTNZCnSc5sXh2RdL7GSnHQStoTvAZBZCM948J38dxZBGHXj2RuZBj604CqMVzHkl0VZCbWnfSZAD9KyM1cAvFtZA0oWIIXZC2cSs7QZDZD'
		respuesta = requests.post(URL,json = JSON)
		return True

	def generic(sel,sender_id):
		JSON = {
  "recipient":{
    "id":sender_id
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[

        	{'title': 'Cotizar',
						  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
						  'subtitle': 'Cotiza tu envío',
						  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
						  },
						  {'title': 'Cotizar',
						  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
						  'subtitle': 'Cotiza tu envío',
						  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
						  }
        ]
      }
    }
  }
}
		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAGUKgfuKVgBAO6al1gRHwzEEH9Hq886Ko4hBHINcQeHiNroxWTPdYkNH1ZCTIUqZAnMu2ZAhINpBTNZCnSc5sXh2RdL7GSnHQStoTvAZBZCM948J38dxZBGHXj2RuZBj604CqMVzHkl0VZCbWnfSZAD9KyM1cAvFtZA0oWIIXZC2cSs7QZDZD'
		respuesta = requests.post(URL,json = JSON)
		send = requests.post(URL,json = JSON)
		print(send.text)
		return True

	def pln(self,sender_id):
		JSON = {"messaging_type":"RESPONSE",
		"recipient":{
		"id":sender_id
		},
		"message":{
		"text":"Que desea?"
		}	
		}

		URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAGUKgfuKVgBAO6al1gRHwzEEH9Hq886Ko4hBHINcQeHiNroxWTPdYkNH1ZCTIUqZAnMu2ZAhINpBTNZCnSc5sXh2RdL7GSnHQStoTvAZBZCM948J38dxZBGHXj2RuZBj604CqMVzHkl0VZCbWnfSZAD9KyM1cAvFtZA0oWIIXZC2cSs7QZDZD'
		respuesta = requests.post(URL,json = JSON)
		respuesta = requests.post(URL, json = JSON)
		return respuesta, 200

	