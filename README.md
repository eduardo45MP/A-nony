# 🕶 A-nony – CLI para Privacidade e Anonimato

**A-nony** é um aplicativo de linha de comando (CLI) voltado para **privacidade online e anonimato**.
Ele combina a rede **Tor** com uma **VPN de terceiros**, criando uma camada dupla de proteção para o tráfego de internet.

---

## 🚀 Funcionalidades
- 🔒 Conectar à **rede Tor** automaticamente.
- 🌐 Iniciar uma **VPN de terceiros** (beta: RiseupVPN).
- ⚙️ Configuração de opções de privacidade personalizadas.
- ⏹ Sair do aplicativo com segurança.

---

## 📂 Estrutura do Projeto
```

A-nony/
├── docs/                # Documentação de design, arquitetura e ideias
│   ├── arquitecture.md
│   ├── deving.md
│   └── ideia.md
├── src/                 # Código-fonte principal
│   ├── main.py          # CLI principal
│   ├── TNWconn.py       # Conexão com Tor
│   └── VPNconn.py       # Conexão com VPN
├── LICENSE              # Licença MIT
└── README.md            # Este documento

````

---

## ⚙️ Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/a-nony.git
cd a-nony
````

2. Instale dependências necessárias:

```bash
pip install stem
sudo apt install openvpn
```

3. Execute o aplicativo:

```bash
python src/main.py
```

---

## 🖥️ Uso

* Após iniciar, siga as instruções no terminal.
* Menu básico:

```
[1] Conectar à Rede Tor e Iniciar VPN
[2] Configurar Opções de Privacidade
[3] Sair do Aplicativo
```

---

## 🔐 Tecnologias

* **Python 3.10+**
* **Stem** (controle da rede Tor)
* **OpenVPN** (gestão da conexão VPN)
* CLI interativa em Python

---

## 🛡️ Segurança e Limitações

* Este projeto é **educacional/prototipagem**.
* Não substitui soluções profissionais de anonimato.
* Pode exigir **permissões elevadas** (sudo) para configurar VPN.
* Implicações legais: o uso do Tor pode ser restrito em alguns países.

---

## 📜 Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

✨ Criado por **Eduardo45MP.dev** como repositório aberto de estudos em privacidade e anonimato digital.
