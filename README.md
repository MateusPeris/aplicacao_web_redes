# 💻 Monitoramento de Tráfego de Rede

Aplicação web que simula o monitoramento de tráfego de dispositivos em uma rede local, utilizando:

- ⚙️ **Flask** como backend (API REST)
- 🎨 **Streamlit** como frontend (interface interativa)
- 🗃️ **SQLite** para persistência dos dados
- 🐳 **Docker** para empacotamento e execução

---

## 🚀 Funcionalidades

- Registro de dispositivos com IP, nome e taxa de tráfego
- Classificação automática do status (Alta, Normal, Baixa)
- Visualização em tabela com botão de remoção
- Gráfico interativo por taxa de tráfego
- Filtragem por status de tráfego
- Comunicação entre frontend e backend via API REST

---

## 🧱 Estrutura do Projeto

```
monitoriamento_rede/
├── backend/              # Flask (API)
├── frontend/             # Streamlit (UI)
├── database/             # SQLite (volume persistido)
├── Dockerfile            # Docker container principal
├── docker-compose.yml    # Orquestração dos serviços
```

---

## 🐳 Como Executar com Docker

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/monitoriamento_rede.git
cd monitoriamento_rede

# Execute os serviços
docker-compose up --build
```

- Acesse o frontend: http://localhost:8501  
- Acesse a API: http://localhost:5000/dispositivos

---

## ✅ Requisitos (se rodar localmente)

- Python 3.9+
- Pip

```bash
cd backend && pip install -r requirements.txt
cd ../frontend && pip install -r requirements.txt
```

---

## 📦 Endpoints da API

- `GET /dispositivos` → Lista os dispositivos
- `POST /dispositivos` → Adiciona um dispositivo
- `DELETE /dispositivos/<id>` → Remove um dispositivo
