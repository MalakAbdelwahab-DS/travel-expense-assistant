### Project Description

Simple AI assistant that answers user questions based on travel expense policy data. 
The application uses an LLM when an API_KEY is provided. Otherwise, it falls back to regular CSV retrieval relying on pandas.


### Project structure

```
app/
├── config.py           # App configuration
├── llm.py              # LLM setup/integration
├── main.py             # Entry point
├── policy_retrieval.py # CSV-based policy lookup
├── prompt.py           # Prompt templates
├── router.py           # API routes
├── schema.py           # Request/response models
├── utils.py            # Helper functions
├── data/
│   └── travel_expense_policy.csv
└── static/
    └── index.html       # Simple web UI

.env.example             # Copy to .env and add model configurations
pyproject.toml           # Poetry dependencies
```


### How to run 

1. Install Poetry (if you don't have it): see https://python-poetry.org/docs/#installation

2. Install dependencies: `poetry install`

3. Run the app: `poetry run run_app`

4. Go to the link of the application, the default is http://127.0.0.1:8000 

5. See /docs for Swagger

6. To run the application with the AI model, copy `.env.example` to `.env` and add your own `API_KEY` and model configuration.


