import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

def main(req: func.HttpRequest) -> func.HttpResponse:

    nomeSito = req.params.get('nomeSito')
    gruppoRisorse = req.params.get('gruppoRisorse')

    if not nomeSito and not gruppoRisorse:
        try:
            req_body = req.get_json()
        except (ValueError, KeyError):
            return func.HttpResponse(body="ERRORE -> Mancano i parametri nomeSito e gruppoRisorse", status_code=400) 
        else:
            nomeSito = req_body.get('nomeSito')
            gruppoRisorse = req_body.get('gruppoRisorse')
        
    if nomeSito and gruppoRisorse:
        credential = DefaultAzureCredential()
        subscription_id = "8002e241-270d-41b2-9c60-f5e2d8d15f67"
        resource_group_name = gruppoRisorse
        storage_account_name = nomeSito
                                                     
        storage_client = StorageManagementClient(credential, subscription_id)

        storage_client.storage_accounts.delete(resource_group_name, storage_account_name)

        return func.HttpResponse(body="SUCCESSO", status_code=200)
    else:
        return func.HttpResponse(body="ERRORE -> Mancano i parametri nomeSito e gruppoRisorse", status_code=400) 