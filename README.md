# Deploy

## Docker
1. Build image:

       docker build -t tgbonus .

2. Run container:

        docker run -d -e TELEGRAM_TOKEN=... -e SHEET_KEY=... -e ...=... -v /path/to/config/cred.json:/code/config/cred.json tgbonus
       


# Develop

1.
    Install dependencies:

        python -m pip install pre-commit

2. Set up pre-commit hooks and venv:

        make init
