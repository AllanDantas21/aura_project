## Aura querys
 - Fiz o deploy de um banco de dados da aurora na nuvem (Render)
   e essa aplicação é para facilitar a conexão com ele.

## instalação
```bash
git clone https://github.com/AllanDantas21/aura_project.git && cd aura_project && chmod 777 ./run.sh
```
## baixar as dependencias
```sh
# dependencias backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# dependencias frontend
cd frontend && yarn install && cd ..
```
## iniciar o projeto
```bash
./run.sh
```

### Após iniciar o projeto entre em: http://localhost:3000