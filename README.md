# To Run the FastApi Backend Server Locally

- Pre-requisite
    - Ollama
    - conda
    - Python 3.10+

## Steps

1. Create the python environment
2. Download Ollama (https://ollama.com)
3. Run ```Ollama pull llama2```
4. Change directory to ```src```
5. Run the below command
```bash
uvicorn main:app --reload
```
