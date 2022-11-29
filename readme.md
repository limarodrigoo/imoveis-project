# Imoveis project

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)	![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


Projeto utilizando **Django REST Framework**, **Mysql** onde é possivel cadastrar imóveis,
seus anuncios e reservas.

## Preparando o ambiente

Primeiro você precisa ter o MySQL instalado e rodando no seu ambiente.

Sugiro utilização de um container com a imagem do mysql utilizando o docker-compose escrito. Para isso você deve instalar o docker, docker-compose além do python3 instalado:

* [Como instalar o docker](https://docs.docker.com/engine/install/) 

* [Como instalar o docker-compose](https://docs.docker.com/compose/install/)

* [Como instalar o python](https://wiki.python.org/moin/BeginnersGuide/Download)


## Instalação

Clone o repositório

```bash
  git clone https://github.com/limarodrigoo/imoveis-project.git
  cd imoveis-project
```

>Uma vez na pasta do projeto você deve criar suas várias de ambiente, utilizando o modelo do arquivo *.env.example*

Atente-se ao DB_HOST, se estiver rodando via docker-compose você deve passar o nome do serviço nessa variavel com o valor `database`

* Se optar por rodar o projeto utilizando docker-compose apenas rode o seguinte comando:

 ```bash
> docker-compose up
```

Caso opte por rodar localmente em sua maquina:

* Primeiro crie um ambiente virtual
```bash
python3 -m venv ./venv
```
* Ative o ambiente virtual
```bash
source venv/bin/activate
```
* Instale as dependencias do projeto

```bash
pip install -r requiriments.txt
```

>**Você deverá criar uma database com o mesmo nome passado na variavel de ambiente DB_NAME**

* Faça as migrações 
```bash
python manage.py makemigrations && python manage.py migrate
```

* Rode o serviço
```bash
python manage.py runserver
```

## Populando o banco

Para popular o banco apenas rode o script populate_script.py da seguinte maneira

* Utilizando docker

```bash
docker-compose exec api python populate_script.py
```

* Localmente com o ambiente virtual ativado

```bash
python populate_script.py
```

## Rodando os testes

* Utilizando docker

```bash
docker-compose exec api python manage.py test
```

* Localmente com o ambiente virtual ativado

```bash
python manage.py test
```


>**Acesse o Server por 127.0.0.1:8000**