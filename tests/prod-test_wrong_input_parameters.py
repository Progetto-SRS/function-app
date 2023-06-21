import requests

massimoTentativi = 4

tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.get("https://prod-functions-srs.azurewebsites.net/api/check-name")
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 400
assert response.content == b"ERRORE -> Manca il parametro nomeSito"
print("Funzione check-name testata con successo...")

tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.get("https://prod-functions-srs.azurewebsites.net/api/create-account-storage")
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 400
assert response.content == b"ERRORE -> Mancano i parametri nomeSito e gruppoRisorse"
print("Funzione create-account-storage testata con successo...")

tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.get("https://prod-functions-srs.azurewebsites.net/api/delete-account-storage")
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 400
assert response.content == b"ERRORE -> Mancano i parametri nomeSito e gruppoRisorse"
print("Funzione delete-account-storage testata con successo...")

tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.get("https://prod-functions-srs.azurewebsites.net/api/enable-static-website")
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 400
assert response.content == b"ERRORE -> Manca il parametro nomeSito"
print("Funzione enable-static-website testata con successo...")

tentativoAttuale = 1
risultatoRichiesta = 500
while tentativoAttuale <= massimoTentativi and risultatoRichiesta != 200:
    response = requests.get("https://prod-functions-srs.azurewebsites.net/api/disable-static-website")
    risultatoRichiesta = response.status_code
    tentativoAttuale += 1
assert response.status_code == 400
assert response.content == b"ERRORE -> Manca il parametro nomeSito"
print("Funzione disable-static-website testata con successo...")