# Deploy

## Docker

1. Build image:

       docker build -t tgbonus .

2. Run container:

        docker run -d -e TELEGRAM_TOKEN=... -e SHEET_KEY=... -e ...=... -v /path/to/config/cred.json:/code/config/cred.json tgbonus
       
## Local

1. Setup `.env`.

   Create `.env` file in root dir and fill it with `.env.example`template.

2. Put `cred.json` file with **GoogleService** creds to `config/` folder.

3. Install dependencies:

          pip install -r requirements.txt

4. Run bot:

          make run
   or

          python -m src.main

# Develop

1.
    Install dependencies:

        python -m pip install pre-commit

2. Set up pre-commit hooks and venv:

        make init
