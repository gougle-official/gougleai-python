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
| Model Name     | Model ID                   | Model Type                          |
| -------------- | -------------------------- | ----------------------------------- |
| GLT-1          | gougleai.models.glt.glt1   | Chat Completion and Text Completion |
| GLT-1.0.5 Beta | gougleai.models.glt.glt105 | Chat Completion and Text Completion |
| GIC-1          | gougleai.models.gic.gic1   | Image Generation                    |
| GIC-1.0.5 Beta | gougleai.models.gic.gic105 | Image Generation                    |

## Example
### `python`
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

### `javascript`

#### `html`
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>
		<input type="text" id="myInput">
		<p id="myParagraph"></p>
		<script src="https://api.withgougle.cf/ai/gougleai-js" type="text/javascript"></script>
		<script src="./app.js" type="text/javascript"></script>
	</body>
</html>
```

#### `javascript`
```javascript
gougleai.apiKey = "YOU_API_KEY_HERE";
userInput = document.getElementById("myInput");
textOutput = document.getElementById("myParagraph");

userInput.addEventListener("submit", () => {
	prompt = userInput.value;
	
	response = gougleai.complete(gougleai.models.glt.glt1, prompt, 100);
	
	textOutput.textContent = "GLT-1: " + response.choices[0];
});
```
