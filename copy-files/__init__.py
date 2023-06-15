import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:

    nomeContainerOrigine = req.params.get('nomeContainerOrigine')
    accountStorageOrigine = req.params.get('accountStorageOrigine')
    nomeContainerDestinazione = req.params.get('nomeContainerDestinazione')
    accountStorageDestinazione = req.params.get('accountStorageDestinazione')
    if not nomeContainerOrigine and not accountStorageOrigine and not nomeContainerDestinazione and not accountStorageDestinazione:
        try:
            req_body = req.get_json()
        except (ValueError, KeyError):
            return func.HttpResponse("ERRORE -> Specificare i parametri nomeContainerOrigine, accountStorageOrigine, nomeContainerDestinazione e accountStorageDestinazione", status_code=200) 
        else:
            nomeContainerOrigine = req_body.get('nomeContainerOrigine')
            accountStorageOrigine = req_body.get('accountStorageOrigine')
            nomeContainerDestinazione = req_body.get('nomeContainerDestinazione')
            accountStorageDestinazione = req_body.get('accountStorageDestinazione')

    if nomeContainerOrigine and accountStorageOrigine and nomeContainerDestinazione and accountStorageDestinazione:
        credential = DefaultAzureCredential()
        account_url_origine = f"https://{accountStorageOrigine}.blob.core.windows.net"
        account_url_destinazione = f"https://{accountStorageDestinazione}.blob.core.windows.net"

        blob_service_client_origine = BlobServiceClient(account_url=account_url_origine, credential=credential)
        blob_service_client_destinazione = BlobServiceClient(account_url=account_url_destinazione, credential=credential)

        container_origine = blob_service_client_origine.get_container_client(nomeContainerOrigine)
        container_destinazione = blob_service_client_destinazione.get_container_client(nomeContainerDestinazione)

        blobs = container_origine.list_blobs()
        for blob in blobs:
            blob_client_origine = container_origine.get_blob_client(blob.name)
            blob_client_destinazione = container_destinazione.get_blob_client(blob.name)
            blob_client_destinazione.start_copy_from_url(blob_client_origine.url)

        return func.HttpResponse("SUCCESSO", status_code=200)
    else:
        return func.HttpResponse("ERRORE -> Specificare i parametri nomeContainer e accountStorage", status_code=200)

    #{ "nomeContainerOrigine": "sitoweb", "accountStorageOrigine": "devstoragesrs", "nomeContainerDestinazione": "$web", "accountStorageDestinazione": "webappprova" }