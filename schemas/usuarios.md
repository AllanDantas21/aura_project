``` sh
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,      -- ID único e autoincrementável para cada usuário
    nome VARCHAR(10) NOT NULL,  -- Nome do usuário, tamanho máximo de 100caracteres
    senha VARCHAR(12) NOT NULL, -- Senha do usuário
);
``` 