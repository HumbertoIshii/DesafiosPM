# Desafios - Programação em Microinformática

Este repositório contém a resolução de 4 desafios práticos desenvolvidos como parte da disciplina **Programação em Microinformática**. Cada desafio tem como objetivo aprimorar habilidades em programação, lógica de desenvolvimento e resolução de problemas utilizando técnicas básicas de programação.

## Desafios

### 1. **Desafio 1:**
   - Montar um site de uma universidade em HTML e CSS.


### 2. **Desafio 2:**
   - Implementar o Flask no desenvolvimento do Desafio 1;
   - Utilizar o CSS Normalize;
   - Utilizar o arquivo base.html.

## Para executar esse projeto

<details>

### Clone esse repositório

```
git clone https://github.com/HumbertoIshii/DesafiosPM.git
cd D2
```

### Crie um ambiente virtual

```
python -m venv venv
```

### Ative o ambiente virtual

```
venv/Scripts/activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Inicie o servidor

```
flask run
```

### Encontre o site em algum navegador

```
https://localhost:5000
```
</details>


## Imagem do Site

![Site](resources/D1%20e%20D2.png)


### 3. **Desafio 3: [Estado da Arte]**
   - Utilizar o framework Bootstrap para criar a estrutura básica da página;
   - Aplicar o recurso @media para criar um layout responsivo;
   - Usar pelo menos 5 componentes do Bootstrap;
   - Implementar um menu de navegação que se adapte a diferentes tamanhos de tela;
   - Usar Flexbox para organizar os elementos em seções da página, como cabeçalho, conteúdo e rodapé;
   - Adicionar estilos personalizados para tornar a página única;
   - Certificar-se de que a página seja totalmente responsiva, funcionando bem em telas de tamanhos variados, desde smartphones até desktops.

## Para executar esse projeto

<details>

### Clone esse repositório

```
git clone https://github.com/HumbertoIshii/DesafiosPM.git
cd D3
```

### Crie um ambiente virtual

```
python -m venv venv
```

### Ative o ambiente virtual

```
venv/Scripts/activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Inicie o servidor

```
flask run
```

### Encontre o site em algum navegador

```
https://localhost:5000
```

</details>

### 4. **Desafio 4: [Estado da Arte +]**
   - Inserir um banco de dados MySQL no Desafio 3.

## Para executar esse projeto

<details>

### Clone esse repositório

```
git clone https://github.com/HumbertoIshii/DesafiosPM.git
cd D4
```

### Crie o Banco de Dados

```
CREATE DATABASE IF NOT EXISTS unlucky;
USE unlucky;

CREATE TABLE IF NOT EXISTS accounts (
	idAccount int(11) NOT NULL AUTO_INCREMENT,
  	username varchar(100) NOT NULL,
  	email varchar(50) NOT NULL,
    PRIMARY KEY (idAccount)
);

create table commentDB (
id int auto_increment,
username varchar(50) NOT NULL,
content varchar(255) not null,
now_date varchar(20),
PRIMARY KEY (id)
);
```

### Configure a senha no Arquivo App.py

```
app.config['MYSQL_PASSWORD'] = 'SENHA' //linha 13
```

### Crie um ambiente virtual

```
python -m venv venv
```

### Ative o ambiente virtual

```
venv/Scripts/activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Inicie o servidor

```
flask run
```

### Encontre o site em algum navegador

```
https://localhost:5000
```

</details>

## Vídeo do Site

https://github.com/user-attachments/assets/1ccea921-c73f-4582-a9d0-def06a715b11

