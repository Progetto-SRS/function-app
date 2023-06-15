import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:

    nomeContainer = req.params.get('nomeContainer')
    accountStorage = req.params.get('accountStorage')
    if not nomeContainer and not accountStorage:
        try:
            req_body = req.get_json()
        except (ValueError, KeyError):
            return func.HttpResponse(body="ERRORE -> Specificare i parametri nomeContainer e accountStorage", status_code=400) 
        else:
            nomeContainer = req_body.get('nomeContainer')
            accountStorage = req_body.get('accountStorage')

    if nomeContainer and accountStorage:
        credential = DefaultAzureCredential()
        account_url = f"https://{accountStorage}.blob.core.windows.net"

        blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

        blob_service_client.delete_container(nomeContainer)

        return func.HttpResponse(body="SUCCESSO", status_code=200)
    else:
        return func.HttpResponse(body="ERRORE -> Specificare i parametri nomeContainer e accountStorage", status_code=400)