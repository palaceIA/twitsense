# 🌟 [TwitSense]

## Gerenciador de Comentários com Análise de Sentimento em Tempo Real

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Licença](https://img.shields.io/badge/License-[TIPO_DE_LICENÇA]-brightgreen.svg?style=for-the-badge)](LICENSE)

---

## 💡 Sobre o Projeto

Este é um sistema robusto de **gerenciamento de comentários** construído com **Streamlit**, **Python** e **Supabase**. Ele não é apenas um CRUD (Create, Read, Update, Delete), mas um sistema inteligente focado em insights imediatos.

O grande diferencial é a integração de um modelo de **Análise de Sentimento** em tempo real. Toda vez que um comentário é publicado ou editado, ele é classificado automaticamente, fornecendo feedback visual instantâneo ao usuário.

### Funcionalidades em Destaque:

* **Análise de Sentimento em Tempo Real:** Classificação instantânea (`positivo`, `negativo`, `neutro`, `irrelevante`) usando um *callable model* (`model_predict_fn`).
* **Resumo de Sentimentos (Dashboard):** Exibição de métricas visuais que totalizam os comentários por cada categoria de sentimento.
* **Visualização Clara:** Cada comentário na lista é marcado com uma bolinha colorida:
    * **🟢 Positivo**
    * **🔴 Negativo**
    * **🟡 Neutro**
    * **⚪ Irrelevante**
* **Gerenciamento Completo:** Publicação, listagem, edição e exclusão de comentários.

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Interface (UI)** | **Streamlit** | Criação rápida e interativa do front-end. |
| **Backend/Lógica** | **Python** | Regras de negócio e chamada ao modelo de IA. |
| **Banco de Dados** | **Supabase (PostgreSQL)** | Persistência de dados e execução de funções RPC. |
| **Análise de Sentimento** | `model_predict_fn` | Função de classificação de texto (simulada ou real). |

---

## ⚙️ Configuração e Instalação

Siga estes passos para configurar e rodar o projeto localmente.

### Pré-requisitos

* Python (3.8+)
* Conta no Supabase

### 1. Clonar o Repositório

```bash
git clone [https://www.youtube.com/shorts/apr341idq8U](https://www.youtube.com/shorts/apr341idq8U)
cd [NOME DO SEU PROJETO]