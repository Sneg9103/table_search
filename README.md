<div align="center">
  <h1>DB Schema Handler</h1>
  <img alt="release 0.0.1" src="https://img.shields.io/badge/release-0.0.1-blue">
</div>
<hr />

This Docker Compose configuration allows <b>locally</b> launch a project version 
for <b>development</b>. The configuration contains the following services (containers):

* searcher_py_host (python 3.12, pip, Django, DRF, psycopg2, requests, gunicorn etc.)
* searcher_ng_host (Nginx 1.24 for the proxy requests between containers)
* searcher_db_host (PostgreSQL 15.1 for the database storage)

## 📟 <a name="cheat_sheet"></a>Cheat sheet
* `docker exec -it searcher_py_host bash` enter to the container
* `docker-compose down` stop all containers
* `docker system prune -a --volumes` remove all containers, images, networks, and volumes
* `docker-compose up -d --build` build and run all containers

### Test users:
- email: `your email in .env`, password: `your password in .env` is staff and superuser permissions
- email: `tkyivborscht@example.com`, password: `borscht123` is test user
- email: `lvivgalushka@example.com`, password: `galushka123` is test user
- email: `odessaseafood@example.com`, password: `seafood123` is test user
- email: `dniprodelight@example.com`, password: `delight123` is test user
- email: `zaporizhzhiazest@example.com`, password: `zest123` is test user

## 📜 Contents

### ⚙ <a href="#pre_installations">1. Pre-installations</a>
### 🚀 <a href="#first_lounch">2. First launch</a>
#### <a href="#cloning">2.1. Cloning a project to a local machine</a>
#### <a href="#building_image">2.2. Building a project</a>

## ⚙ <a name="pre_installations"></a>1. Pre-installations
At the moment, the project has been tested for Mac OS Apple Silicon (M1).

> For different operating systems, install (or already installed):
* [Git](https://git-scm.com/downloads) (version control system)
* [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/) (Windows)
* [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/) (Mac OS)
* [Python v.3.12](https://www.python.org/downloads/)
* [DBeaver Community](https://dbeaver.io/download/) (UI for database management, just advice)

> Get from colleagues: 
* file `.env`, and put it in the root of the project, or use `.env.example` as a template and create your own `.env` file

## 🚀 <a name="first_lounch"></a>2. First launch
### <a name="cloning"></a>2.1. Cloning a project to a local machine

In the folder where you plan to store the project run terminal and enter the command:

`git clone https://github.com/Sneg9103/table_search.git`

For simplicity of description, the abbreviation `ROOT` will be use as the address 
to the folder (including this folder name) where the project is located. It will have this kind of the tree structure:

```
.ROOT
├── README.md
├── search_service
├── nginx
├── postgres
├── docker-compose.yml
├── .gitignore
├── .env.example
└── .env
```

The received or created `.env` file must be placed in the root of the project at `ROOT/.env`.

### <a name="building_image"></a>2.2. Building a project
Using the IDE, the Git Bash or any other terminal, run the command:

`docker-compose up -d --build`

Assembly of the project will start and it will take about 5 minutes. 
After the build is completed, you will have access to a command line 
in which you can run necessary commands.

Application available at the <a href="localhost">localhost</a>, or admin panel at <a href="localhost/admin">localhost/admin</a> where you can check a successfuly pre-created user.