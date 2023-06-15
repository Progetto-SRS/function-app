import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, StaticWebsite

def main(req: func.HttpRequest) -> func.HttpResponse:

    nomeSito = req.params.get('nomeSito')
    if not nomeSito:
        try:
            req_body = req.get_json()
        except (ValueError, KeyError):
            return func.HttpResponse(body="ERRORE -> Manca il parametro nomeSito", status_code=400) 
        else:
            nomeSito = req_body.get('nomeSito')

    if nomeSito:
        credential = DefaultAzureCredential()

        blob_service_client = BlobServiceClient(account_url=f"https://{nomeSito}.blob.core.windows.net", credential=credential)

        sito_statico = StaticWebsite()

        sito_statico.enabled = True
        sito_statico.index_document = "index.html"
        sito_statico.error_document404_path = "404.html"

        blob_service_client.set_service_properties(None, None, None, None, None, None, sito_statico)

        return func.HttpResponse(body="SUCCESSO", status_code=200)
    else:
        return func.HttpResponse(body="ERRORE -> Manca il parametro nomeSito", status_code=400)