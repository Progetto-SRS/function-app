import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters

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

        params = StorageAccountCreateParameters(
            sku={"name": "Standard_RAGRS"},
            kind="StorageV2",
            location="westeurope",
            minimum_tls_version="TLS1_2",
            allow_blob_public_access=True,
            allow_shared_key_access=True,
            enable_https_traffic_only=True,
            dns_endpoint_type="Standard",
            public_network_access="Enabled",
            access_tier="Hot",
            encryption={
                "services": {
                    "blob": {"enabled": True},
                    "file": {"enabled": True},
                    "table": {"enabled": True},
                    "queue": {"enabled": True},
                },
                "key_source": "Microsoft.Storage",
            },
            supports_https_traffic_only=True
        )

        storage_account = storage_client.storage_accounts.begin_create(
            resource_group_name,
            storage_account_name,
            params
        ).result()

        return func.HttpResponse(body="SUCCESSO", status_code=200)
    else:
        return func.HttpResponse(body="ERRORE -> Mancano i parametri nomeSito e gruppoRisorse", status_code=400) 