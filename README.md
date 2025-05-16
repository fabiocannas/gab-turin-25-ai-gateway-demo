![alt text](https://github.com/fabiocannas/global-azure-turin-25-ai-gateway-demo/blob/main/GlobalAzure%20Turin%20-%20Mattia%20Contessa%26Fabio%20Cannas%20-%20Deploying%20and%20Protecting%20LLMs%20at%20Scale%20with%20Azure%20API%20Management.png)

## Credits
+ [AI Gateway](https://github.com/Azure-Samples/AI-Gateway)
+ [Remote-MCP-Apim-Functions-Python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
+ [Sample-App-AOAI-ChatGPT](https://github.com/microsoft/sample-app-aoai-chatGPT)

## Presentation
[Slides (.pdf)](https://github.com/fabiocannas/global-azure-turin-25-ai-gateway-demo/blob/main/Global%20Azure%20Torino%202025%20-%20AI%20Gateway.pdf)

## Demos - Prerequisites

+ [Python](https://www.python.org/downloads/) version 3.12.6
+ [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
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


   
