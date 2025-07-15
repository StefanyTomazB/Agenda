# API de Agendamento

Esta é uma API simples de agendamento feita com FastAPI.

## Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```
3. Acesse a documentação automática em [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints
- `POST /agendamentos`: Cria um novo agendamento
- `GET /agendamentos`: Lista todos os agendamentos
- `DELETE /agendamentos/{id}`: Remove um agendamento
