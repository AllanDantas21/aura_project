## Aura querys
 - Fiz o deploy de um banco de dados da aurora na nuvem (Render)
   e essa aplicação é para facilitar a conexão com ele.

## Instalação
```bash
git clone https://github.com/AllanDantas21/aura_project.git && cd aura_project && chmod 777 ./run.sh
```
## Baixar as dependencias
```sh
# dependencias
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd frontend && yarn install && cd ..
```

## Crie um .env com essas variaveis
```bash
DB_HOST=host
DB_NAME=name
DB_USER=user
DB_PASSWORD=password 
```

## iniciar o projeto
```bash
./run.sh
```

### Após iniciar o projeto entre em: http://localhost:3000

## Estrutura do projeto

```bash
my_own_libc/
├── backend/         # Arquivos de backend 
│   ├── main.py      # API endpoints(/query, /auth)
│   └── database.py  # conexão com o banco de dados
│
├── frontend/             
│   └── srcs/
│       ├── pages/   # paginas da aplicação (ex. loginPage, queryPage)
│       └── app.js   # "main"
├── run.sh           # script para iniciar o backend e o frontend
├── .env             # crie um .env e adicione as variaveis de conexão com o BD
└── README.md        # Docs  

```