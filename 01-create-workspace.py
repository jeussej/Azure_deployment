from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id="99e1e721-7184-498e-8aff-b2ad4e53c1c2")
ws = Workspace.create(name='azure-ml',
            subscription_id='b262344d-c5a4-4b5c-882c-eb4acbb44d08',
            resource_group='rg_project_lol_predict',
            create_resource_group=True,
            location='eastus2',
            auth=interactive_auth
            )
            
# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='./.azureml/',file_name='config.json')