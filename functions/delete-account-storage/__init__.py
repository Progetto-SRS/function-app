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
        subscription_id = "6a6034ce-5623-4822-8c31-de299765adbe"
        resource_group_name = gruppoRisorse
        storage_account_name = nomeSito
                                                     
        storage_client = StorageManagementClient(credential, subscription_id)

        storage_client.storage_accounts.delete(resource_group_name, storage_account_name)

        return func.HttpResponse(body="SUCCESSO", status_code=200)
    else:
        return func.HttpResponse(body="ERRORE -> Mancano i parametri nomeSito e gruppoRisorse", status_code=400) 