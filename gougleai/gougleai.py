# Path to python.exe: "U:\prive\Applications\Python\python.exe"
# Exuecute cmd line: `"U:\prive\Applications\Python\python.exe" ./gougleai.py`
# Install <requests> with pip: `"U:\prive\Applications\Python\Scripts\pip.exe" install requests`

import urllib.request
import json
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

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
				url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
				headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {apiKey}'}
				
				params = {'prompt': prompt, 'max_tokens': maxTokenNumber}
				params = json.dumps(params).encode('utf-8')
				req = urllib.request.Request(url, data=params, headers=headers)
				response = urllib.request.urlopen(req)
				data = response.read()
				
				result = json.loads(data.decode('utf-8'))
				
				complete.choices = [result]
				return complete
			else:
				raise Exception("Cannot complete empty string.")
		else:
			raise Exception("Model '" + str(model) + "' not found in gougleai API.")