## Aura querys
- This project is a web application that allows users to execute queries on a cloud database directly from their browser.

## Install
```bash
git clone https://github.com/AllanDantas21/aura_project.git && cd aura_project && chmod 777 ./run.sh
```
## Download dependencies
```sh
# dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd frontend && yarn install && cd ..
```

## Create a .env file with these variables
```bash
DB_HOST=host
DB_NAME=name
DB_USER=user
DB_PASSWORD=password 
```

## Start the project
```bash
./run.sh
```

### After starting the project, go to: http://localhost:3000

## Project structure

```bash
my_own_libc/
├── backend/         # Backend files
│   ├── main.py      # API endpoints(/query, /auth)
│   └── database.py  # Database connection
│
├── frontend/             
│   └── srcs/
│       ├── pages/   # Application pages (e.g., loginPage, queryPage)
│       └── app.js   # "main"
├── run.sh           # Script to start the backend and frontend
├── .env             # Create a .env file and add the database connection variables
└── README.md        # Docs  

```