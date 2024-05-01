# Overview

Collection of Data & AI examples. More information here: [https://www.notion.so/Data-AI-examples-bce8a29e0e4b4c838acdf53e31e54c4c?pvs=4](https://www.notion.so/Data-AI-examples-bce8a29e0e4b4c838acdf53e31e54c4c?pvs=4)

- `simpleRegression.ipynb`: Simple regression example.
- `streamlitExampleRegression.py`: Streamlit exampel with upload Excel and use network from `simpleRegression.ipynb`.

# Technical stuff

## Streamlit

- run it:
```powershell
python -m streamlit run .\streamlitExampleRegression.py
```

## Docker

- Create docker build:
```bash
docker build -t streamlitexample .
```

- Enter image in terminal:
```bash
docker run -it streamlitexample /bin/bash
```

- Run it:
```bash
docker run -p 5000:5000 streamlitexample
```

- access:
```bash
http://localhost:5000
```


## Jupyter
- Add paths to import from anywhere in jupyter:

```python
sys.path.append(r"FULLPATH")
```

- autoreload:

```python
%load_ext autoreload

%autoreload 2
```

## Postgres
Some problems with login, therefor changed 'method' to 'trust' here: ```"C:\Program Files\PostgreSQL\15\data\pg_hba.conf"```
