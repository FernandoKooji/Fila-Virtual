# Sistema de Fila Virtual

Sistema de gerenciamento de atendimento com fila virtual, desenvolvido como projeto acadêmico e primeira versão funcional.

O sistema permite que clientes entrem em uma fila de atendimento, acompanhem sua posição e recebam atualizações sobre o andamento do atendimento. O atendente possui um painel para gerenciar a fila, chamar senhas, finalizar atendimentos e marcar senhas como ausentes.

---

## Sobre o projeto

O projeto foi desenvolvido com o objetivo de criar uma solução simples e funcional para gerenciamento de filas de atendimento, reduzindo a necessidade de espera física e permitindo que o cliente acompanhe sua senha por meio de um portal.

A arquitetura foi organizada em camadas, separando:

* API
* Regras de negócio
* Banco de dados
* Schemas de entrada e saída
* Interface do cliente
* Interface do atendente

A comunicação entre frontend e backend é realizada através de uma API REST desenvolvida com FastAPI.

---

## Objetivos

### Objetivo principal

Desenvolver um sistema de fila virtual capaz de organizar o atendimento e permitir o acompanhamento da fila pelo cliente e pelo atendente.

### Objetivos específicos

* Criar senhas normais e preferenciais.
* Controlar a ordem de atendimento.
* Permitir que o atendente chame a próxima senha.
* Permitir finalizar um atendimento.
* Permitir marcar uma senha como ausente.
* Permitir cancelar uma senha.
* Consultar a posição de uma senha.
* Exibir a fila atualizada no painel do atendente.
* Atualizar automaticamente o portal do cliente.
* Registrar tempos de espera e atendimento.
* Persistir os dados utilizando SQLite.

---

## Funcionalidades

### Portal do Cliente

O cliente pode:

* Entrar na fila.
* Escolher entre atendimento normal e preferencial.
* Receber uma senha.
* Consultar sua posição.
* Visualizar pessoas à frente.
* Acompanhar o status da senha.
* Cancelar a senha.
* Receber uma notificação quando sua senha for chamada.
* Receber uma notificação quando a senha for marcada como ausente.
* Receber uma notificação quando o atendimento for finalizado.

A sessão da senha é armazenada no `localStorage`, permitindo recuperar o acompanhamento após recarregar a página.

<!-- INSERIR SCREENSHOT AQUI: Portal do cliente na tela inicial -->

<img width="500" height="400" alt="Untitled-1" src="https://github.com/user-attachments/assets/2b48df2a-c9c4-4d53-9e3e-d89f366cec90" />

<!-- INSERIR SCREENSHOT AQUI: Portal do cliente mostrando uma senha aguardando -->
<img width="500" height="400" alt="2" src="https://github.com/user-attachments/assets/c2e84ed7-f0ad-4150-88ca-d6a87ab454fa" />

<!-- INSERIR SCREENSHOT AQUI: Portal do cliente mostrando a notificação de senha chamada -->
<img width="500" height="400" alt="3" src="https://github.com/user-attachments/assets/363c2d1f-235b-4bf0-9a39-7c1bdceb7ec1" />

<!-- INSERIR SCREENSHOT AQUI: Portal do cliente mostrando a notificação de senha ausente -->
<img width="500" height="400" alt="4" src="https://github.com/user-attachments/assets/a3229468-05d0-4493-a329-f6f461acb65b" />

---

### Painel do Atendente

O atendente pode:

* Visualizar a senha atualmente em atendimento.
* Visualizar a fila de espera.
* Chamar a próxima senha.
* Rechamar a senha atual.
* Finalizar o atendimento.
* Marcar a senha como ausente.
* Atualizar automaticamente a fila.

A ordenação da fila é realizada pelo backend através do `Queue Engine`, evitando que as regras de prioridade sejam duplicadas no frontend.

<!-- INSERIR SCREENSHOT AQUI: Painel do atendente com a fila -->
<img width="500" height="400" alt="5" src="https://github.com/user-attachments/assets/27eabb2e-d3b2-4e31-afcd-9678decde713" />

<!-- INSERIR SCREENSHOT AQUI: Painel do atendente com uma senha em atendimento -->

<!-- INSERIR SCREENSHOT AQUI: Painel do atendente após chamar a próxima senha -->

---

## Tipos de senha

O sistema possui dois tipos:

| Tipo         | Prefixo | Exemplo |
| ------------ | ------- | ------- |
| Normal       | `N`     | `N001`  |
| Preferencial | `P`     | `P001`  |

As senhas são numeradas separadamente.

Exemplo:

```text
N001
N002
N003

P001
P002
P003
```

A fila prioriza as senhas preferenciais antes das senhas normais, de acordo com as regras implementadas no `Queue Engine`.

---

## Fluxo principal

O fluxo básico do sistema é:

```text
Cliente
   │
   ▼
Escolhe tipo de atendimento
   │
   ▼
POST /tickets/
   │
   ▼
Senha criada
   │
   ▼
Cliente acompanha posição
   │
   ▼
GET /queue/position/{ticket_code}
   │
   ▼
Atendente chama próxima
   │
   ▼
Senha → em_atendimento
   │
   ├───────────────┐
   │               │
   ▼               ▼
Finalizado      Ausente
   │               │
   └───────┬───────┘
           ▼
     Cliente recebe
       notificação
```

---
<!--
## Arquitetura

A aplicação utiliza uma arquitetura dividida em camadas:

```text
Frontend
   │
   ▼
Router
   │
   ▼
Service
   │
   ▼
Queue Engine / Regras de negócio
   │
   ▼
Queries SQL
   │
   ▼
SQLite
```

### Responsabilidade das camadas

**Routers**

Responsáveis pelos endpoints HTTP da API.

**Services**

Contêm as operações do sistema e fazem a comunicação entre API, banco e regras de negócio.

**Queue Engine**

Centraliza as regras relacionadas à ordenação e gerenciamento da fila.

**Database**

Responsável pela conexão com SQLite e pelas consultas SQL.

**Schemas**

Definem os modelos de entrada e saída utilizados pela API.

**Frontend**

Responsável pela interface do cliente e do atendente e pelo consumo da API.

---

## Estrutura do projeto

```text
fila_virtual/
│
├── app/
│   │
│   ├── core/
│   │   ├── constants.py
│   │   ├── date_formatter.py
│   │   ├── dependencies.py
│   │   ├── settings.py
│   │   ├── exceptions.py
│   │   └── response_mapper.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── queries.py
│   │   └── schema.sql
│   │
│   ├── routers/
│   │   ├── queue_router.py
│   │   ├── page_router.py
│   │   ├── report_router.py
│   │   └── ticket_router.py
│   │
│   ├── schemas/
│   │   ├── queue.py
│   │   ├── ticket.py
│   │   └── report.py
│   │
│   ├── services/
│   │   ├── queue_service.py
│   │   ├── report_service.py
│   │   └── ticket_service.py
│   │
│   ├── utils/
│   │   └── queue_engine.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── attendant.css
│   │   │   ├── portal.css
│   │   │   └── shared.css
│   │   │
│   │   └── js/
│   │       ├── api/
│   │       ├── mappers/
│   │       ├── portal/
│   │       ├── ui/
│   │       ├── utils/
│   │       └── attendant.js
│   │
│   ├── templates/
│   │   ├── attendant.html
│   │   └── index.html
│   │
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

> O banco SQLite local (`database.db`) e o ambiente virtual Python (`venv/`) não fazem parte do repositório.
--> 
--- 

## Tecnologias utilizadas

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* SQLite

### Frontend

* HTML
* CSS
* JavaScript
* JavaScript ES Modules
* LocalStorage
* Fetch API

### Desenvolvimento

* Visual Studio Code
* Swagger / OpenAPI
* SQLite

---

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

Entre na pasta:

```bash
cd fila_virtual
```

---

### 2. Criar o ambiente virtual

Linux/macOS:

```bash
python3 -m venv venv
```

Windows:

```bash
python -m venv venv
```

---

### 3. Ativar o ambiente virtual

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000
```

---

## Documentação da API

A aplicação utiliza a documentação automática do FastAPI.

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

<!-- INSERIR SCREENSHOT AQUI: Swagger mostrando os endpoints da aplicação -->

---

## Principais endpoints

### Tickets

| Método   | Endpoint                 | Descrição          |
| -------- | ------------------------ | ------------------ |
| `POST`   | `/tickets/`              | Criar uma senha    |
| `DELETE` | `/tickets/{ticket_code}` | Cancelar uma senha |

### Fila

| Método | Endpoint                        | Descrição                      |
| ------ | ------------------------------- | ------------------------------ |
| `GET`  | `/queue/current`                | Consultar atendimento atual    |
| `GET`  | `/queue/status`                 | Consultar resumo da fila       |
| `GET`  | `/queue/list`                   | Consultar fila ordenada        |
| `GET`  | `/queue/position/{ticket_code}` | Consultar posição de uma senha |
| `POST` | `/queue/next`                   | Chamar próxima senha           |
| `POST` | `/queue/finish`                 | Finalizar atendimento          |
| `POST` | `/queue/skip`                   | Marcar senha como ausente      |
| `POST` | `/queue/cancel`                 | Cancelar senha                 |
| `POST` | `/queue/recall`                 | Rechamar senha atual           |

<img width="500" height="800" alt="6" src="https://github.com/user-attachments/assets/56677e60-d9e7-4987-837b-f04bc45ae006" />

<img width="500" height="800" alt="7" src="https://github.com/user-attachments/assets/b4a52127-b8ed-4503-9c08-a853c2acde60" />

---

## Banco de dados

O sistema utiliza SQLite.

A tabela principal é:

```text
tickets
```

Ela registra informações como:

* ID;
* código da senha;
* tipo;
* status;
* data de criação;
* horário da chamada;
* horário de finalização;
* tempo de espera;
* tempo de atendimento.

<img width="900" height="400" alt="8" src="https://github.com/user-attachments/assets/6794a543-8b54-45ff-ac7d-1762a1b7b559" />

O controle dos últimos números utilizados é armazenado em:

```text
system_state
```

O arquivo `schema.sql` contém a estrutura necessária para inicialização do banco.

---

## Status das senhas

Durante o fluxo do sistema, uma senha pode assumir estados como:

```text
aguardando
     │
     ▼
em_atendimento
   │       │
   │       ├──► ausente
   │       │
   │       └──► finalizado
   │
   └────────────► cancelado
```

---

## Testes

A API foi testada através do Swagger e do fluxo completo da aplicação.

Os principais cenários validados foram:

* Criação de senha normal.
* Criação de senha preferencial.
* Ordenação da fila.
* Chamada da próxima senha.
* Consulta da senha atual.
* Consulta da posição.
* Finalização do atendimento.
* Marcação de senha como ausente.
* Cancelamento.
* Rechamada.
* Atualização automática do painel do atendente.
* Atualização automática do portal do cliente.
* Notificações de mudança de estado.

<!-- INSERIR SCREENSHOT AQUI: Exemplo de teste de criação de senha no Swagger -->

<!-- INSERIR SCREENSHOT AQUI: Exemplo de consulta de posição no Swagger -->

---
<!--
## Demonstração

<!-- INSERIR SCREENSHOT AQUI: Visão geral do sistema funcionando -->
<!--
### Portal do Cliente

<!-- INSERIR SCREENSHOT AQUI: Portal do cliente -->
<!--
### Painel do Atendente

<!-- INSERIR SCREENSHOT AQUI: Painel do atendente -->
<!--
### Notificações

<!-- INSERIR SCREENSHOT AQUI: Popup verde indicando que a senha foi chamada -->

<!-- INSERIR SCREENSHOT AQUI: Popup vermelho indicando que a senha foi marcada como ausente -->
---

## Segurança e arquivos locais

Arquivos específicos do ambiente de desenvolvimento não fazem parte do repositório.

Entre eles:

```text
venv/
.env
database.db
*.db
```

Esses arquivos são protegidos pelo `.gitignore`.

O banco de dados local pode ser recriado a partir do `schema.sql`.

---

<!--
imitações da V1

Esta versão representa uma **primeira versão funcional do projeto**.

Alguns recursos podem ser aprimorados em versões futuras, como:

* autenticação de atendentes;
* múltiplos guichês;
* controle de permissões;
* WebSocket para comunicação em tempo real;
* painel de chamadas dedicado para TV;
* relatórios gerenciais;
* dashboard;
* estimativa avançada de tempo de espera;
* integração com serviços externos;
* deploy em ambiente de produção.
-->
---

## Próximos passos

A evolução planejada do projeto inclui:

1. Melhorias na experiência visual.
2. Painel de chamadas para TV/monitor.
3. Relatórios e métricas.
4. Comunicação em tempo real utilizando WebSocket.
5. Melhorias de segurança e autenticação.
6. Preparação para implantação em ambiente real.

---
<!--
## Documentação do projeto

A documentação complementar do desenvolvimento pode apresentar:

* decisões de arquitetura;
* modelagem do banco;
* regras da fila;
* desenvolvimento da API;
* desenvolvimento do frontend;
* testes realizados;
* dificuldades encontradas;
* soluções implementadas;
* evolução do projeto.

<!-- INSERIR LINK AQUI: Relatório completo do projeto, caso seja publicado separadamente -->

Projeto desenvolvido por Fernando Kooji Shimomura, para fins acadêmicos e de aprendizado, com foco em desenvolvimento de APIs, banco de dados, arquitetura de software e integração entre backend e frontend.

