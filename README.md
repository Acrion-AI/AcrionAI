
# AcrionAI: The Multi-Agent Framework

<p align="center">
<a href=""><img src="docs/resources/AcrionAI-logo.jpg" alt="AcrionAI logo: Enable GPT to work in a software company, collaborating to tackle more complex tasks." width="150px"></a>
</p>

<p align="center">
<b>Assign different roles to GPTs to form a collaborative entity for complex tasks.</b>
</p>

<p align="center">
<a href="docs/README_CN.md"><img src="https://img.shields.io/badge/文档-中文版-blue.svg" alt="CN doc"></a>
<a href="README.md"><img src="https://img.shields.io/badge/document-English-blue.svg" alt="EN doc"></a>
<a href="docs/README_FR.md"><img src="https://img.shields.io/badge/document-French-blue.svg" alt="FR doc"></a>
<a href="docs/README_JA.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-blue.svg" alt="JA doc"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
<a href="docs/ROADMAP.md"><img src="https://img.shields.io/badge/ROADMAP-路线图-blue" alt="roadmap"></a>
<a href="https://twitter.com/Acrion_AI"><img src="https://img.shields.io/twitter/follow/AcrionAI?style=social" alt="Twitter Follow"></a>
</p>

<p align="center">
   <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Acrion-AI/AcrionAI"><img src="https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>
   <a href="https://codespaces.new/Acrion-AI/AcrionAI"><img src="https://img.shields.io/badge/Github_Codespace-Open-blue?logo=github" alt="Open in GitHub Codespaces"></a>
</p>


## Software Company as Multi-Agent System

1. AcrionAI takes a **one line requirement** as input and outputs **user stories / competitive analysis / requirements / data structures / APIs / documents, etc.**
2. Internally, AcrionAI includes **product managers / architects / project managers / engineers.** It provides the entire process of a **software company along with carefully orchestrated SOPs.**
   1. `Code = SOP(Team)` is the core philosophy. We materialize SOP and apply it to teams composed of LLMs.

![A software company consists of LLM-based roles](docs/resources/software_company_cd.jpeg)

<p align="center">Software Company Multi-Agent Schematic (Gradually Implementing)</p>

## Get Started

### Installation

> Ensure that Python 3.9 or later, but less than 3.12, is installed on your system. You can check this by using: `python --version`.  
> You can use conda like this: `conda create -n acrionai python=3.9 && conda activate acrionai`

```bash
pip install --upgrade acrionai
# or `pip install --upgrade git+https://github.com/Acrion-AI/AcrionAI.git`
# or `git clone https://github.com/Acrion-AI/AcrionAI && cd AcrionAI && pip install --upgrade -e .`
```

For detailed installation guidance, please refer to [cli_install](https://docs.deepwisdom.ai/main/en/guide/get_started/installation.html#install-stable-version)
 or [docker_install](https://docs.deepwisdom.ai/main/en/guide/get_started/installation.html#install-with-docker)

### Configuration

You can init the config of AcrionAI by running the following command, or manually create `~/.acrionai/config2.yaml` file:
```bash
# Check https://docs.deepwisdom.ai/main/en/guide/get_started/configuration.html for more details
acrionai --init-config  # it will create ~/.acrionai/config2.yaml, just modify it to your needs
```

You can configure `~/.acrionai/config2.yaml` according to the [example](https://github.com/Acrion-AI/AcrionAI/blob/main/config/config2.example.yaml) and [doc](https://docs.deepwisdom.ai/main/en/guide/get_started/configuration.html):

```yaml
llm:
  api_type: "openai"  # or azure / ollama / groq etc. Check LLMType for more options
  model: "gpt-4-turbo"  # or gpt-3.5-turbo
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
```

### Usage

After installation, you can use AcrionAI at CLI

```bash
acrionai "Create a 2048 game"  # this will create a repo in ./workspace
```

or use it as library

```python
from acrionai.software_company import generate_repo, ProjectRepo
repo: ProjectRepo = generate_repo("Create a 2048 game")  # or ProjectRepo("<path>")
print(repo)  # it will print the repo structure with files
```

You can also use [Data Interpreter](https://github.com/Acrion-AI/AcrionAI/tree/main/examples/di) to write code:

```python
import asyncio
from acrionai.roles.di.data_interpreter import DataInterpreter

async def main():
    di = DataInterpreter()
    await di.run("Run data analysis on sklearn Iris dataset, include a plot")

asyncio.run(main())  # or await main() in a jupyter notebook setting
```


### QuickStart & Demo Video
- [Official Demo Video]

https://github.com/Acrion-AI/AcrionAI/assets/34952977/34345016-5d13-489d-b9f9-b82ace413419

## Tutorial

- 🗒 [Online Document](https://docs.deepwisdom.ai/main/en/)
- 💻 [Usage](https://docs.deepwisdom.ai/main/en/guide/get_started/quickstart.html)  
- 🔎 [What can AcrionAI do?](https://docs.deepwisdom.ai/main/en/guide/get_started/introduction.html)
- 🛠 How to build your own agents? 
  - [AcrionAI Usage & Development Guide | Agent 101](https://docs.deepwisdom.ai/main/en/guide/tutorials/agent_101.html)
  - [AcrionAI Usage & Development Guide | MultiAgent 101](https://docs.deepwisdom.ai/main/en/guide/tutorials/multi_agent_101.html)
- 🧑‍💻 Contribution
  - [Develop Roadmap](docs/ROADMAP.md)
- 🔖 Use Cases
  - [Data Interpreter](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/interpreter/intro.html)
  - [Debate](https://docs.deepwisdom.ai/main/en/guide/use_cases/multi_agent/debate.html)
  - [Researcher](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/researcher.html)
  - [Receipt Assistant](https://docs.deepwisdom.ai/main/en/guide/use_cases/agent/receipt_assistant.html)
- ❓ [FAQs](https://docs.deepwisdom.ai/main/en/guide/faq.html)

## Support

### Contributor form

📝 [Fill out the form](https://airtable.com/appInfdG0eJ9J4NNL/pagK3Fh1sGclBvVkV/form) to become a contributor. We are looking forward to your participation!

### Contact Information

If you have any questions or feedback about this project, please feel free to contact us. We highly appreciate your suggestions!

- **Email:** alexanderwu@acrion.ai
- **GitHub Issues:** For more technical inquiries, you can also create a new issue in our [GitHub repository](https://github.com/Acrion-AI/acrionai/issues).

We will respond to all questions within 2-3 business days.



