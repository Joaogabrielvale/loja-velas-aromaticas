# 🕯️ Sistema de Gestão - Velas Aromáticas

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-amber)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## 📌 Sobre o Projeto
Sistema de gerenciamento de estoque e cadastro de produtos desenvolvido para loja de velas aromáticas artesanais. O objetivo do sistema é controlar o fluxo de insumos (como potes de vidro, ceras, aromas e essências) e os produtos finais, garantindo a organização do negócio e do catálogo.

## 🚀 Funcionalidades Entregues (AC2) - *Fase Atual*
A segunda fase do projeto foca em inteligência de dados, cálculos automáticos e finalização das operações de banco:
- [x] **Dashboard Dinâmico (Visão Geral):** Criação de uma tela inicial inteligente com painéis estatísticos (Cards) estilizados com Bootstrap.
- [x] **Cálculos em SQL:** Implementação de queries lógicas no Python utilizando `COUNT` (para contagem de catálogo) e `SUM(preco * quantidade)` atrelado à função `COALESCE` para projeção financeira do estoque em tempo real.
- [x] **Finalização do CRUD (Delete):** Implementação e validação da rota de exclusão conectada ao MySQL, permitindo remover registros do estoque de forma segura e imediata.
- [x] **Refatoração de Arquitetura de Software:** Separação do front-end em templates modulares (rotas exclusivas para `/`, `/cadastro` e `/estoque`), garantindo navegação sem bugs e sistema escalável.

## 🚀 Funcionalidades Entregues (AC1)
A primeira fase do projeto contemplou a funcionalidade central do negócio:
- [x] **Arquitetura em 3 Camadas:** Front-end, Back-end e Banco de Dados 100% integrados.
- [x] **Banco de Dados (MySQL):** Criação da tabela `velas` com campos para nome, aroma, descrição sensorial, preço e quantidade.
- [x] **Back-end (Python/Flask):** Rotas estruturadas para recebimento de requisições GET e POST.
- [x] **Front-end (HTML/CSS):** Interface responsiva desenvolvida com Bootstrap (Dark Theme).

## 🛠️ Como rodar o projeto localmente
1. Certifique-se de ter o serviço do MySQL rodando em sua máquina (e o banco `loja_velas` criado).
2. Instalar as dependências executando no terminal:
   `pip install flask mysql-connector-python`
3. Executar a aplicação Python:
   `python app.py`
4. Acessar pelo navegador através do endereço `http://127.0.0.1:5000`

---
*Desenvolvido como projeto acadêmico de análise e desenvolvimento de sistemas (Faculdade Impacta de Tecnologia).*
