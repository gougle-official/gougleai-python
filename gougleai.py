# Path to python.exe: "U:\prive\Applications\Python\python.exe"
# Exuecute cmd line: '"U:\prive\Applications\Python\python.exe" ./gougleai.py'
# Install <requests> with pip: '"U:\prive\Applications\Python\Scripts\pip.exe" install requests'

# import requests

apiKey = ""
orgId = ""

class models:
	list = """GLT-1: gougleai.models.glt.glt1 (gougleai.models.glt.versions[0])"""
	
	class glt:
		versions = [1];
		glt1 = "gougleai.models.glt.glt1"

def complete(model, prompt:str, tokenNumber):
	if apiKey == "":
		raise Exception("API Key cannot be empty string.")
	else:
		complete.choices = []
		if str(model) in models.list:
			if prompt != "":
				# complete.choices = [requests.get('https://api.openai.com/v1/engines/davinci-codex/completions', headers = {'Content-Type': 'application/json','Authorization': f'Bearer {apiKey}'}, params = {'prompt': prompt,'max_tokens': tokenNumber}).json()]
				complete.choices = [prompt]
				return complete
			else:
				raise Exception("Cannot complete empty string.")
		else:
			raise Exception("Model '" + str(model) + "' not found in gougleai API.")