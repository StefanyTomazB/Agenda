from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Agendamento(BaseModel):
    id: int
    nome: str
    data: str

agendamentos: List[Agendamento] = []

@app.post("/agendamentos", response_model=Agendamento)
def criar_agendamento(agendamento: Agendamento):
    agendamentos.append(agendamento)
    return agendamento

@app.get("/agendamentos", response_model=List[Agendamento])
def listar_agendamentos():
    return agendamentos

@app.delete("/agendamentos/{agendamento_id}")
def deletar_agendamento(agendamento_id: int):
    for agendamento in agendamentos:
        if agendamento.id == agendamento_id:
            agendamentos.remove(agendamento)
            return {"mensagem": "Agendamento removido"}
    raise HTTPException(status_code=404, detail="Agendamento não encontrado")
