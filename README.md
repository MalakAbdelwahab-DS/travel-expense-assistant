## Running

Runs out of the box with no setup, no API keys, no accounts.
Answers are generated via keyword matching against `travel_expense_policy.csv`.

To use the real model (Anthropic) agent instead, copy `.env.example` to
`.env` and add your own `ANTHROPIC_API_KEY`.

### How to run and stop

Run: python main.py

Stop: Ctrl+C in the terminal (don't just close the terminal window)