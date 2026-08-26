WIP (WORK IN PROGRESS)

Estrutura do projeto (Avançado)
1.Portal do cliente(QR Code)
Número de pessoas na fila com tempo estimado*
Entrada na fila (Nome e Sobrenome)
Fila preferencial
Escolha do serviço*
Upload Antecipado (clica no numero do whats e inicia conversa já com uma mensagem tipo “Olá”)
Acompanhamento da posição
Botão de sair da fila , e confirmação
Confirmar quando faltar 2 posições:*
Se não confirmar em x minutos a senha é pulada.
As senhas não dão shift um número para frente. O número ausente é deletado da fila e todos permanecem com a mesma senha para evitar confusão
2.Painel do Atendente
Chamar o próximo, chamar anterior, chamar novamente, pular atual, inserir número para chamar 
Visualizar a senha chamada com nome da pessoa
Visualizar a fila e colorir dependendo do serviço, criar uma classificação para filtrar por chegada, por tempo de atendimento, etc*
Visualizar detalhes do serviço*
Histórico das ultimas chamadas, em vermelho a senha pulada
No começo do dia resetar filas

3.Dashboard Gerencial*
Estatísticas
Relatórios
Configuração de serviços e tempos estimados


Estrutura do projeto Simples
1.Portal do cliente(QR Code)
Número de pessoas na fila, botão para entrar na fila 
Fila preferencial ou normal
Upload Antecipado (clica no numero do whats e inicia conversa já com uma mensagem tipo “Olá”)
Acompanhamento da posição
Tempo estimado
Botão de sair da fila , e confirmação

2.Painel do Atendente
Cadastro de atendentes
Visualizar uma lista das pessoas na fila, todas preferenciais vão para o início
Visualizar uma lista das pessoas em atendimento com um botão ao lado do nome de finalizar.
Chamar o próximo, chamar anterior, chamar novamente, Ausente, chamada manual, 
Visualizar a senha chamada com nome da pessoa
Históricos das últimas chamadas, em uma cor neutra as atendidas, em vermelho a senha cancelada, ausente, etc
Botão de encerrar expediente com confirmação e gera logs dia, número de atendimentos. E zera a fila

3.Display de chamada
Na web com a senha atual e últimas chamadas

Softwares

Backend
Frontend
Tempo Real
Hospedagem
Python
HTML
WebSocket
Docker
FastAPI
CSS




SQLite
JavaScript





Lógica da fila
Cliente escaneia QR Code:
1.1 Escolhe a fila Preferencial ou Normal:

As senhas são geradas:
Preferencial: P001, P002 … P999
Normal: N001, N002 … N999

Sistema salva:
ID: 245
Senha: N001
Status: Aguardando

Organização da fila é prioridade balanceada (ex.: 3 preferenciais → 1 normal). 
exemplo: P001, P002, P003, N001, P004, N002 …

Quando o atendente clicar em qualquer botão que chame uma senha: 
5.1. Próximo:
O sistema escolhe a primeira senha da fila e exibe no painel
No programa aparece a senha atual N001 em atendimento

	5.2. Reexibir: 
Ao chamar N001 e depois N002, ao apertar Anterior apenas reapresenta a senha no painel

5.3. Chamar novamente:
A senha no painel é chamada novamente. O buzzer é tocado novamente e Text to Speech “Senha N001”.



5.4. Chamada Manual:
O atendente digita a senha e aparece uma de cinco mensagens:
-senha não encontrada, senha já atendida, senha cancelada, senha ausente e senha em atendimento. Com mensagem para atendente: 
N001
status: Ausente
Data 22/06/2026 14:10

5.5. Delay para evitar chamada dupla:
Desabilita o botão ao clicar, com um contador regressivo de 3 segundos para chamar o próximo e reabilita após uma resposta do servidor

Fila Vazia:
Se a fila estiver vazia e o atendente apertar Próximo aparece uma mensagem no sistema, “Nenhum cliente aguardando”. Evitando erros.

Se o cliente não respondeu:
Cliente foi chamado
↓
Não compareceu
↓
Atendente aperta "Ausente"
↓
Status = Ausente
↓
Sai da fila ativa
↓
Vai para o histórico 

Cliente sai da fila:
9.1. botão sair da fila com confirmação “Deseja realmente sair?”  S / N
No sistema a senha é removida sem alterar a senha das outras pessoas
Exemplo: N001, N002, N003. 
Se N002 sair fica: N001, N003.
No programa a senha vai para o histórico como “cancelado” e só pode ser chamado via chamada manual

9.2. Cliente só pode sair quando status “Aguardando” e bloquear quando em atendimento, atendido, ausente e cancelado. Aparecendo uma mensagem “Esta senha já foi chamada”.

Status na fila para atendente:
Aguardando, Em atendimento, Atendido, Ausente, Cancelado.
Exemplo:
N001 status aguardando
aperta próximo
N001 status em atendimento
aperta finalizar
N001 Atendido
Evitando erro que uma senha seja considerada atendida por apenas ter sido chamada

Tempo de espera:
Salva o tempo de espera com o horário de entrada na fila e quando a senha é chamada. 
Salva o tempo estimado com o cálculo do tempo médio que fica mais preciso quanto mais atendimentos tiver.

Enquanto houver menos de 10 atendimentos o tempo estimado está indisponível.
Depois de 20 atendimentos calcula o tempo médio.

Atualização da posição:
No portal web o cliente vê:
Sua senha: N006
Posição atual: 3
Quando alguém é atendido, sai da fila ou é pulado:
Posição atual: 2
tempo estimado: 15 minutos
Atualiza automaticamente

Encerrar expediente:
Botão pequeno para evitar clicar sem querer com confirmação
13.1. Clientes na fila:
Caso existem clientes na fila aparece a mensagem:
“Existem 12 clientes aguardando.
Deseja encerrar mesmo assim?”
As senhas são reiniciadas diariamente


Guarda o histórico do dia:
ID: 245
Senha: N001
Tipo: N ou P
Entrada: 09:00
Chamada: 09:12
Finalização: 09:18
Espera: 12 min
Status: Atendido 

Recuperação falhas, quedas, etc:
Caso o sistema principal cair, deve salvar:
Última senha normal: 47
Última senha preferencial: 12
Fila atual
Status dos atendimentos
Senha atualmente em atendimento

Ao reiniciar:
N048
continua corretamente.

Estrutura final dos estados
Aguardando
     │
     ▼
Em atendimento
     │
     ├──► Finalizado
     │
     └──► Ausente
Aguardando
     │
     └──► Cancelado
















Estrutura da API
fila_virtual/
│
├── app/
│   ├── main.py	# Inicializa a API
│   │
│   ├── routers/	#Camada de rotas
│   │   ├── __init__.py
│   │   ├── queue_router.py
│   │   └── ticket_router.py
│   │
│   ├── database/
│   │   ├── database.db
│   │   ├── database.py	# Conexão SQLite
│   │   ├── schema.sql	# Criação das tabelas
│   │   └── queries.py	# SQL reutilizáveis
│   │
│   ├── schemas/	# Modelos Pydantic
│   │   └── ticket.py	
│   │
│   ├── services/
│   │   ├── ticket_service.py	# Regras de negócio
│   │   ├── queue_service.py	#Gerenciamento da fila 
│   │   └── report_service.py
│   │
│   ├── websocket/
│   │   └── manager.py	# Atualizações em tempo real
│   │
│   └── utils/
│       ├── formatter.py
│       └── validator.py
│
├── requirements.txt
└── README.md



Camada de rotas
Tickets
POST /tickets/

Queue
POST /queue/next
POST /queue/finish
POST /queue/skip
POST /queue/cancel
GET /queue/status
GET /queue/position/{ticket_code}

Reports
GET /reports/daily
GET /reports/history
GET /reports/statistics 


