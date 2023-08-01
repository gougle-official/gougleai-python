import requests
import json

apiKey = ""
orgId = ""

class models:
	list = """GLT-1: gougleai.models.glt.glt1 (gougleai.models.glt.versions[0])
GLT-1.0.5: gougleai.models.glt.glt105 (gougleai.models.glt.versions[1])"""
	
	class glt:
		glt1 = "gougleai.models.glt.glt1"
		glt105 = "gougleai.model.glt.glt105"
		versions = [glt1, glt105]

def complete(model, prompt:str, maxTokenNumber:int = 100):
	if apiKey == "":
		raise Exception("API Key cannot be empty string.")
	else:
		complete.choices = []
		if str(model) in models.list:
			if prompt != "":
				url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
				headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {apiKey}'}
				
				params = {'prompt': prompt, 'max_tokens': maxTokenNumber}
				req = requests.post(url, data=params, headers=headers)
				print(url + " " + str(params) + " " + str(headers))
				data = req.text
				
				result = data
				
				complete.choices = [result]
				return complete
			else:
				raise Exception("Cannot complete empty string.")
		elif model != "":
			raise Exception("Model '" + str(model) + "' not found in gougleai API.")
		else:
			raise Exception("Model cannot be empty.")

class chat:
	def complete(model, chatHistory:object, maxTokenNumber:int = 100):
		chatHistory = {}
		chatHistory.role = ""
		chatHistory.message = ""
		if chatHistory.role != "ai" or chatHistory.role != "system" or chatHistory.role != "user":
			raise Exception("Role must be 'ai', 'system' or 'user', cannot be '" + chatHistory.role + "'.")
		if apiKey == "":
			raise Exception("API Key cannot be empty string.")
		else:
			complete.choices = []
			if str(model) in models.list:
				if chatHistory != "":
					url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
					headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {apiKey}'}

					params = {'prompt': chatHistory, 'max_tokens': maxTokenNumber}
					params = json.dumps(params).encode('utf-8')
					req = urllib.request.Request(url, data=params, headers=headers)
					response = urllib.request.urlopen(req)
					data = response.read()

					result = json.loads(data.decode('utf-8'))

					complete.choices = [result]
					return complete
				else:
					raise Exception("Cannot complete empty string.")
			elif model != "":
				raise Exception("Model '" + str(model) + "' not found in gougleai API.")
			else:
				raise Exception("Model cannot be empty.")