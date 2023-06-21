import requests

nomeSito = "testwebappsrs"
gruppoRisorse = "users-env"
massimoTentativi = 4

# Controllo che il servizio check-name restituisca 'USATO'
tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.post("https://prod-functions-srs.azurewebsites.net/api/check-name", json={"nomeSito": "prodstoragesrs"})
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 200
assert response.content == b"USATO"
print("Controllo disponibilità account di storage già usato eseguito con successo...")

# Controllo che il servizio check-name restituisca 'SUCCESSO'
# Il nome del sito cambia in maniera tale da arrivare al successo del controllo
tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.post("https://prod-functions-srs.azurewebsites.net/api/check-name", json={"nomeSito": nomeSito})
    if(response.content == b"USATO"):
        response = requests.post("https://prod-functions-srs.azurewebsites.net/api/delete-account-storage", json={"nomeSito": nomeSito, "gruppoRisorse": gruppoRisorse})
        response = requests.post("https://prod-functions-srs.azurewebsites.net/api/check-name", json={"nomeSito": nomeSito})
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 200
assert response.content == b"DISPONIBILE"
print("Controllo disponibilità account di storage non ancora usato eseguito con successo...")

# Controllo che il servizio create-account-storage restituisca 'SUCCESSO'
tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.post("https://prod-functions-srs.azurewebsites.net/api/create-account-storage", json={"nomeSito": nomeSito, "gruppoRisorse": gruppoRisorse})
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 200
assert response.content == b"SUCCESSO"
print("Creazione dell'account di storage eseguita con successo...")

# Controllo che il servizio enable-static-website restituisca 'SUCCESSO'
tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.post("https://prod-functions-srs.azurewebsites.net/api/enable-static-website", json={"nomeSito": nomeSito})
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 200
assert response.content == b"SUCCESSO"
print("Attivazione sito web statico eseguita con successo...")

# Controllo che il servizio disable-static-website restituisca 'SUCCESSO'
tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.post("https://prod-functions-srs.azurewebsites.net/api/disable-static-website", json={"nomeSito": nomeSito})
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 200
assert response.content == b"SUCCESSO"
print("Disattivazione sito web statico eseguita con successo...")

# Controllo che il servizio delete-account-storage restituisca 'SUCCESSO'
tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.post("https://prod-functions-srs.azurewebsites.net/api/delete-account-storage", json={"nomeSito": nomeSito, "gruppoRisorse": gruppoRisorse})
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 200
assert response.content == b"SUCCESSO"
print("Eliminazione dell'account di storage eseguita con successo...")