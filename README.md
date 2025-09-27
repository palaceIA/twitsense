# 🐦 TwitSense

| Plataforma |
| :--- | 
| ![](img/comment.png) |  


## Gerenciador de Comentários com Análise de Sentimento em Tempo Real

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

---

## 💡 Sobre o Projeto

Este é um sistema robusto de **gerenciamento de comentários** construído com **Streamlit**, **Python** e **Supabase**. Ele não é apenas um CRUD (Create, Read, Update, Delete), mas um sistema inteligente focado em insights imediatos.

O grande diferencial é a integração de um modelo de **Análise de Sentimento** em tempo real. Toda vez que um comentário é publicado ou editado, ele é classificado automaticamente, fornecendo feedback visual instantâneo ao usuário.

Experimento ocumentado na plataforma Kaggle com o seguinte link: [https://www.kaggle.com/code/palaciodata/classification-sentiment](https://www.kaggle.com/code/palaciodata/classification-sentiment)  
Dados utilizados open-source da plataforma: [https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)  
Você ira encontrar o modelo na pasta model juntamente com o tokenizador utilizado durante o treinamento

---

### Métricas de Treinamento

| Métrica | Visualização |
| :--- | :--- |
| Perda (Loss) durante o Treinamento | ![Gráfico de Perda durante o treinamento](img/losses.png) |
| Matriz de Confusão | ![Matriz de confusão](img/matrix.png) |
| Precisão por Classe | ![Precisão para cada classe](img/precision.png) |

### Funcionalidades em Destaque:

* **Análise de Sentimento em Tempo Real:** Classificação instantânea (`positivo`, `negativo`, `neutro`, `irrelevante`) usando modelo LSTM(Long shot memory).
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
| **Banco de Dados** | **Supabase (PostgreSQL)** | Persistência de dados e execução de funções. |
| **Análise de Sentimento** | Modelo LSTM | Classificação de texto. |

---


```bash
git clone [https://www.youtube.com/shorts/apr341idq8U](https://www.youtube.com/shorts/apr341idq8U)
cd [NOME DO SEU PROJETO]
