# Dockerfile Generator

Hi, thanks for visiting my repo, this project is a simple dockerfile generator based on OpenAI API, so make sure u already have an OpenAI API key. This Dockerfile Generator is accessed through in console, but this project will always be developed to bring more features.

## 🔧 How to use with Virtual Environment

Clone this repo to ur computer

```bash
  git clone https://github.com/ISMAILABDURRAHIMNF/Dockerfile-Generator.git
```

Use your virtual environtmend and install all required modules using `pip install` on the console

```bash
  pip install reqirements.txt -r
```

Create the `.env` file in the same directory as `main.py` using this variable.

```bash
  OPENAI_API_KEY=
  SECRET_KEY=
  DEPLOY_PATH=
```

Use the program by running `src/main.py`

```bash
  python src/main.py
```

## 🔧 How to use with Docker

Clone this repo to ur computer

```bash
  git clone https://github.com/ISMAILABDURRAHIMNF/Dockerfile-Generator.git
```

Build docker image

```bash
  docker build -t dockerfile-generator .
```

Run docker container with environment variabel (OPENAI_API_KEY, SECRET_KEY, DEPLOY_PATH). Replace the 8080 with your custom port u want.

```bash
  docker container run -d -p 8080:5000 \
    -e OPENAI_API_KEY= \
    -e SECRET_KEY= \
    -e DEPLOY_PATH= \
    dockerfile-generator
```

## ❗Warning !

Make sure u already have an OpenAI API key and save it in the `.env` file.
