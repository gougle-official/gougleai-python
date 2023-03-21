# Gougle AI API Docs
## Usages
### For `python` with `pip` in `cmd` :
```shell
pip install gougleai
```

### For `javascript` with `cdn` in `html` page :
```html
<script src="https://api.withgougle.cf/ai/gougleai-js" type="text/javascript"></script>
```

## Models
<table>
    <tr>
        <th>Model Name</th>
        <th>Model ID</th>
    </tr>
    <tr>
        <td>GLT-1</td>
        <td>gougleai.models.glt.glt1</td>
    </tr>
</table>

## Example
```python
# Path to python.exe: "C:\Program Files (x86)\Python\python.exe"
# Exuecute cmd line: '"C:\Program Files (x86)\Python\python.exe" ./example.py'

import gougleai

gougleai.apiKey = "gougle"

while True:
	userInput = input("User: ")
	
	response = gougleai.complete(model = gougleai.models.glt.glt1, prompt = userInput, maxTokenNumber = 100)
	
	print("GLT-1: " + response.choices[0])
```
