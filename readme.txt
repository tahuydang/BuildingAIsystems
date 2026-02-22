### AI Dev Environment includes
1. Python: 
   Massive AI ecosystem: TensorFlow, Pytorch, OpenAI, Langchain
   Works across platforms: Windows, Mac, Linux - Write once run anywhere
   Easy API integration: Connect to GPT, Claude, Gemini with just a few lines
2. Dependency isolation
3. Project structure
    A clean AI project has 
        Source code folder
        Dependency file
        Configuration files
        Documentation
    -> Good structure scales from prototype to production

4. Version control

### From code to AI Response
1. Call an LLM API from python

2. Pass input text to the model

3. Receive and print output

4. Control behavior with parameters

Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.

Step01: Active your environment
```bash
source .venv/bin/activate

Step02: Install required libraries
```bash
pip install openai
pip install python-dotenv 
pip freeze > requirements.txt

Step03: Store API key Securely
create .env file 
add OPENAI_API_KEY to .evn file 
add .env to .gitignore to make sure that git never tracks it

Step04: Write python script to call llm api 

## The core prompt structure 
1. Role 
    Who the model is 

2. Task 
    What it must do 

3. Context 
    What it knows

4. Constraints
    What it must avoid 

5. Output format 
    How it must respond

-> This structure works across all LLMs, it's universal

## System vs User Prompt 
System Prompt:
    - Define behaviours and rules
    - Sets the foundation

User Prompt:
    - Supply task input
    - Provide specifics

Instruction Hierarchy
    - System Instruction
        Highest priority 
    - Developer Instruction
        Design time constraints and implement guidance 
    - User Instruction
        Runtime requests that may override weak rules
-> If your rules are weak or unclear, User input overrides them. => Models will ignore you 


## Failure modes 
    Hallucination
    Overconfidence
    Ignoring constraints
    Wrong assumptions
    Responding without knowledge
=> Most failures are prompt design issues, not model limitations

## Guardrails in prompts 
    - Explicit instruction for unknown scenarios 
    - Permission to refuse
        "If unsure, say you don't know"
    - Ground responses in provided context
    - Refusal conditions
        When not to respond
=> Guardrails increase trust, and trust is everything in production systems.

## Engineer the prompt 
    Role: Define how the model is 
    Task: Clarify the objective
    Constraints: Set boundaries
    Format: Specify output structure
    Guardrails: Handle edge cases
=> Structure first, wording second

## Template the prompt 
    Make it reusable
    - Parameterize 
    - Document 
    - Store 

----- Structure output ------------
