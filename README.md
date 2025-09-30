### SETUP LOCALE
### configurazione del ambiente creazione del environment locale (una sorta di m2)
    - python -m venv venv   ### CREAZIONE VENV
### attivaione della roba di sopra
    - venv\Scripts\activate ### ATTIVAZIONE VENV
### configurazione del gestione del packeging manager pyton
    - pip install pip-tools
 ### preparazione delle dipendenze per generazione txt delle dipendenze del progetto in essere
    - pip-compile requirements.in
 ### descrizione delle dipendenze e derivazione delle singole librerie   
    - pip install -r requirements.txt
 ###   NON disattivare il progetto
    - deactivate ### DISATTIVAZIONE VENV

### RUN LOCALE
    - venv\Scripts\activate ### ATTIVAZIONE VENV
    - python -m fastapi dev  ### LANCIO APP (per usare questo comando da bash serve installare fastapi cli, non l'ho inserita nei requirements)

### UPDATE LIBRARY
    - pip compile --upgrade requirements.in
    - pip install -r requirements.txt

### ADD NEW LIBRARY
    - pip compile requirements.in
    - pip install -r requirements.txt


