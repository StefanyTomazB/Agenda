import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_agendamento():
    response = client.post("/agendamentos", json={"id": 1, "nome": "Teste", "data": "2025-07-15"})
    assert response.status_code == 200
    assert response.json()["nome"] == "Teste"

def test_listar_agendamentos():
    client.post("/agendamentos", json={"id": 2, "nome": "Outro", "data": "2025-07-16"})
    response = client.get("/agendamentos")
    assert response.status_code == 200
    assert any(a["nome"] == "Outro" for a in response.json())

def test_deletar_agendamento():
    client.post("/agendamentos", json={"id": 3, "nome": "Remover", "data": "2025-07-17"})
    response = client.delete("/agendamentos/3")
    assert response.status_code == 200
    assert response.json()["mensagem"] == "Agendamento removido"
    response = client.delete("/agendamentos/999")
    assert response.status_code == 404
