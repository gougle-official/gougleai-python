import requests
import json

apiKey = ""
orgId = ""

class models:
	@property
	def list(self):
		lst = ""

		for e in self.__dict__:
			if isinstance(e, dict):
				for i, n in enumerate(e.items()):
					lst += f"{n[1]}: gougleai.models.{e.__name__}[\"{n[0]}\"] (gougleai.models.{e.__name__}.versions[{i}])\n"

		return lst
	
	glt = {
		"glt-1": "GLT-1",
		"glt-1.0.5": "GLT-1.0.5"
	}
	glt["versions"] = [e for e in glt.values()]
	
	gic = {
		"gic-1": "GLT-1",
		"gic-1.0.5": "GLT-1.0.5"
	}
	gic["versions"] = [e for e in glt.values()]

def complete(model, prompt: str, maxTokenNumber: int = 100):
	if apiKey == "":
		raise Exception("API Key cannot be empty string.")
	else:
		complete.choices = []
		if str(model) in models.list:
			if str(model) in models.glt.__dict__.values():
				if prompt != "":
					url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
					headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {apiKey}'}
					
					params = {'prompt': prompt, 'max_tokens': maxTokenNumber}
					req = requests.post(url, data=params, headers=headers)
					data = req.text
					
					result = data
					
					complete.choices = [result]
					return complete
				else:
					raise Exception("Cannot complete empty string.")
			else:
				raise Exception("Model '" + str(model) + "' is not a Text Completion model.\nSee https://github.com/gougle-official/gougleai-python/blob/main/README.md#models for the models list with model types.")
		elif model != "":
			raise Exception("Model '" + str(model) + "' not found in gougleai API.")
		else:
			raise Exception("Model cannot be empty.")

class chat:
	def complete(model, chatHistory:object, maxTokenNumber:int = 100):
		if chatHistory["role"] != "ai" and chatHistory["role"] != "system" and chatHistory["role"] != "user":
			raise Exception("Role must be 'ai', 'system' or 'user', cannot be '" + chatHistory["role"] + "'.")
		if apiKey == "":
			raise Exception("API Key cannot be empty string.")
		else:
			complete.choices = []
			if str(model) in models.list:
				if str(model) in models.glt.__dict__.values():
					if chatHistory != {} and chatHistory["message"] != "":
						url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
						headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {apiKey}'}

						params = {'prompt': chatHistory, 'max_tokens': maxTokenNumber}
						params = json.dumps(params).encode('utf-8')

						req = requests.post(url, data=params, headers=headers)
						data = req.text
						
						result = data

						complete.choices = [result]
						return complete
					else:
						raise Exception("Cannot complete empty conversation.")
				else:
					raise Exception("Model '" + str(model) + "' is not a Text Completion model.\nSee https://github.com/gougle-official/gougleai-python/blob/main/README.md#models for the models list with model types.")

			elif model != "":
				raise Exception("Model '" + str(model) + "' not found in gougleai API.")
			else:
				raise Exception("Model cannot be empty.")
