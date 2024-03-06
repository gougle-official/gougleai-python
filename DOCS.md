# Gougle AI API Docs − Python
## Usages
For `python` using `pip` in `cmd` :
```sh
pip install gougleai
```

## Models
| Model Name     | Model ID                     | Model Type                          |
| -------------- | ---------------------------- | ----------------------------------- |
| GLT-1          | `gougleai.models.glt.glt1`   | Chat Completion and Text Completion |
| GLT-1.0.5 Beta | `gougleai.models.glt.glt105` | Chat Completion and Text Completion |
| GIC-1          | `gougleai.models.gic.gic1`   | Image Generation                    |
| GIC-1.0.5 Beta | `gougleai.models.gic.gic105` | Image Generation                    |

## Example
`python`: 
```py
import gougleai

gougleai.apiKey = "YOUR_API_KEY_HERE"

while True:
	userInput = input("User: ")
	
	response = gougleai.complete(model = gougleai.models.glt.glt1, prompt = userInput, maxTokenNumber = 100)
	
	print("GLT-1: " + response.choices[0])
```
## More docs
To see more docs about Gougle AI API, you can read [`gougle-official/gougleai/DOCS.md`](https://www.github.com/gougle-official/gougleai/blob/main/DOCS.md) for `all` or [`gougle-official/gougleai-javascript/DOCS.md`](https://www.github.com/gougle-official/gougleai-javascript/blob/main/DOCS.md) for `javascript`. 
