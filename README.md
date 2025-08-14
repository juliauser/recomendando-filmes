
# 🎬 Recomendador de Filmes (Flask + TMDB)

Aplicação web simples em **Flask** que recomenda filmes com base em um filme informado pelo usuário, usando a API do **The Movie Database (TMDB)**.

## ✨ Funcionalidades
- Busca do filme pelo nome (usa o primeiro resultado encontrado).
- Recomendação de filmes similares via endpoint de recomendações da TMDB.
- Cards com pôster, título, ano e descrição resumida.
- Paginação simples das recomendações.
- Página **/sobre** com detalhes do projeto.
- Uso de **variáveis de ambiente** para proteger a API Key.

## 🚀 Como executar localmente
1. **Clone** o repositório e entre na pasta:
   ```bash
   git clone https://github.com/seu-usuario/movie_recommender.git
   cd movie_recommender
   ```

2. (Opcional) **Crie e ative** um ambiente virtual:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Crie um arquivo `.env`** na raiz do projeto com sua chave da TMDB:
   ```env
   TMDB_API_KEY=sua_chave_aqui
   ```

5. **Execute** a aplicação:
   ```bash
   python app.py
   ```

6. Abra no navegador:
   - <http://127.0.0.1:5000/>

## 🧩 Endpoints da TMDB utilizados
- Busca de filmes: `/search/movie`
- Recomendações: `/movie/{id}/recommendations`
- Imagens: base `https://image.tmdb.org/t/p/w500`

> Observação: a API TMDB permite escolher o idioma via parâmetro `language=pt-BR` para textos localizados.

## 📦 Estrutura do projeto
```
movie_recommender/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
└── templates/
    ├── index.html
    ├── results.html
    └── sobre.html
```

## 🔒 Segurança (API Key)
- **Não** suba sua chave da TMDB no GitHub.
- O projeto usa `python-dotenv` para ler a variável `TMDB_API_KEY` de um arquivo `.env` (ignorado pelo Git).
- O app mostra um alerta amigável se a chave não estiver configurada.

## ✅ Critérios do teste atendidos
- Uso de **Flask** (funções integradas, rotas e templates).  
- Arquivo **requirements.txt** com as dependências.  
- **README.md** com descrição e instruções de uso.  

---

Feito com ❤️ por Julia
