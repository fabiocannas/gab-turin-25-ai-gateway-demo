## Credits
+ [AI Gateway](https://github.com/Azure-Samples/AI-Gateway)
+ [Remote-MCP-Apim-Functions-Python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
+ [Sample-App-AOAI-ChatGPT](https://github.com/microsoft/sample-app-aoai-chatGPT)

## Prerequisites

+ [Python](https://www.python.org/downloads/) version 3.12.6
+ [Azure Developer CLI](https://aka.ms/azd)
+ Use [Visual Studio Code](https://code.visualstudio.com/) to run and debug locally
+ Install Jupiter extension for Visual Studio Code
+ Create Python virtual environment (https://code.visualstudio.com/docs/python/environments#_creating-environments) -> use requirements.txt
+ Before using Jupiter notebooks run:
   ```shell
   az login --tenant <tenant-id>
   az account set --subscription <subscription-id>
   ```
+ demos\remote-mcp-apim-functions - create azd environment:
  ```shell
   azd auth login
   azd env new "demo" --location "<az-region>" --subscription "<subscription-id>"
   ```
+ demos\remote-mcp-apim-functions - deploy infrastructure and code:
  ```shell
   azd up
   ```
   
