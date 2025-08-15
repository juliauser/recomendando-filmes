
# 🎬 Recomendando filmes (Flask + TMDB)

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
   git clone https://github.com/juliauser/recomendando-filmes
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
   API_KEY=sua_chave_aqui
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
MOVIE_RECOMMENDER/
├── static/              # Arquivos CSS, JS, imagens estáticas
│   └── style.css
├── templates/           # Templates HTML do Flask
│   ├── index.html       # Página inicial
│   ├── results.html     # Resultados e paginação
│   └── sobre.html       # Página "Sobre"
├── .env                 # Variáveis de ambiente (API Key)
├── .gitignore           # Arquivos ignorados pelo Git
├── app.py               # Código principal da aplicação Flask
├── README.md            # Documentação do projeto
└── requirements.txt     # Dependências do Python
```

## 🔒 Segurança (API Key)
- **Não** suba sua chave da TMDB no GitHub.
- O projeto usa `python-dotenv` para ler a variável `API_KEY` de um arquivo `.env` (ignorado pelo Git).
- O app mostra um alerta amigável se a chave não estiver configurada.

Feito com 🖤 por Julia.