# Overview

Train and save a network, deploy an application using streamlit and create an image from the dockerfile.

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