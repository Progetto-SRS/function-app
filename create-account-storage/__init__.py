import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters

def main(req: func.HttpRequest) -> func.HttpResponse:

    nomeSito = req.params.get('nomeSito')                                           # Recupero il parametro nomeSito dalla richiesta GET

    if not nomeSito:                                                                # Se non sono riuscito ad ottenere il parametro dalla richiesta GET
        try:
            req_body = req.get_json()                                               # Leggo il corpo della richiesta POST in formato JSON
        except (ValueError, KeyError):
            return func.HttpResponse("ERRORE -> Specificare il nome del sito tramite il parametro nomeSito", status_code=200) 
        else:
            nomeSito = req_body.get('nomeSito')                                     # Recupero il parametro nomeSito dalla richiesta POST
        
    if nomeSito:                                                                    # Se sono riuscito a leggere il parametro nomeSito
        credential = DefaultAzureCredential()
        subscription_id = "8002e241-270d-41b2-9c60-f5e2d8d15f67"
        resource_group_name = "users-env"
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

        return func.HttpResponse("SUCCESSO", status_code=200)
    else:
        return func.HttpResponse("ERRORE -> Specificare il nome del sito tramite il parametro nomeSito", status_code=200) 