import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

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
        subscription_id = "6a6034ce-5623-4822-8c31-de299765adbe"
        storage_account_name = nomeSito

        storage_client = StorageManagementClient(credential, subscription_id)

        result = storage_client.storage_accounts.check_name_availability(
            {
                "name": storage_account_name,
                "type": "Microsoft.Storage/storageAccounts"
            }
        )

        if result.name_available:
            return func.HttpResponse(body="DISPONIBILE", status_code=200)
        else:
            return func.HttpResponse(body="USATO", status_code=200)
    else:
        return func.HttpResponse(body="ERRORE -> Manca il parametro nomeSito", status_code=400) 