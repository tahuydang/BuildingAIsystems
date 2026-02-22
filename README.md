# Building AI systems & Agents tutorial
This repository contains source code and step by steps to build AI system and agent

## Setup
1. Create and activate a virtual environment

2. Install dependencies

3. Run scripts in scripts folder 
```bash
python scripts/hello_api.py

## initialize git locally
```bash
git init
git add . 
git commit -m"Add project structure"

## Add dependencies file
python -m pip freeze > requirements.txt

```bash
git add requirements.txt
git commit -m "Add requirements.txt"
git push 

## Golden rules
Never commit environments or secrets & Keys to version control

## Day03
create a `.env` file in the project level
OPENAI_API_KEY=your_key_here

install dependencies
pip install -r requirements.txt

run:
python scripts/cli_assistant.py