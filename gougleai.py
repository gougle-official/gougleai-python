# Path to python.exe: "C:\Program Files (x86)\Python\python.exe"
# Exuecute cmd line: '"C:\Program Files (x86)\Python\python.exe" ./gougleai.py'
# Install <requests> with pip: '"C:\Program Files (x86)\Python\Scripts\pip.exe" install requests'

import requests

apiKey = ""
orgId = ""

class models:
	list = """GLT-1: gougleai.models.glt.glt1 (gougleai.models.glt.versions[0])
GLT-1.0.5: gougleai.models.glt.glt105 (gougleai.models.glt.versions[1])"""
	
	class glt:
		glt1 = "gougleai.models.glt.glt1"
		glt105 = "gougleai.model.glt.glt105"
		versions = [glt1, glt105];

def complete(model, prompt:str, maxTokenNumber:int = 100):
	if apiKey == "":
		raise Exception("API Key cannot be empty string.")
	else:
		complete.choices = []
		if str(model) in models.list:
			if prompt != "":
				complete.choices = [requests.get('https://api.openai.com/v1/engines/davinci-codex/completions', headers = {'Content-Type': 'application/json','Authorization': f'Bearer {apiKey}'}, params = {'prompt': prompt,'max_tokens': maxTokenNumber}).json()]
				return complete
			else:
				raise Exception("Cannot complete empty string.")
		else:
			raise Exception("Model '" + str(model) + "' not found in gougleai API.")
			
