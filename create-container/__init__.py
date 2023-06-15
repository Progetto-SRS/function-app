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
            return func.HttpResponse("ERRORE -> Specificare i parametri nomeContainer e accountStorage", status_code=200) 
        else:
            nomeContainer = req_body.get('nomeContainer')
            accountStorage = req_body.get('accountStorage')

    if nomeContainer and accountStorage:
        credential = DefaultAzureCredential()
        account_url = f"https://{accountStorage}.blob.core.windows.net"

        blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

        blob_service_client.create_container(nomeContainer, public_access="container")

        return func.HttpResponse("SUCCESSO", status_code=200)
    else:
        return func.HttpResponse("ERRORE -> Specificare i parametri nomeContainer e accountStorage", status_code=200)