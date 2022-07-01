import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://ammar.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', '7UpbSpZFSiGSvdvPoeofCtOIM33PkzcGMwxWL9jwmwhmyqB6FM9jwQFQDvIeQ3zwGTthvhMBy8jidv1OqgAkpg=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'resume-data'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'data'),
}