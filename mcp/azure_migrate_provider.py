import requests

class AzureMigrateProvider:
    """
    Talks to Azure Migrate REST APIs and converts output
    into model-consumable context.
    """

    def __init__(self, subscription_id, resource_group, project_name, token):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.project_name = project_name
        self.token = token

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def discover_servers(self):
        # Simplified discovery call (conceptual)
        url = f"https://management.azure.com/subscriptions/{self.subscription_id}" \
              f"/resourceGroups/{self.resource_group}" \
              f"/providers/Microsoft.Migrate/migrateProjects/{self.project_name}" \
              f"/machines?api-version=2018-09-01-preview"

        resp = requests.get(url, headers=self._headers())
        resp.raise_for_status()

        return resp.json().get("value", [])

    def assess_readiness(self):
        # Placeholder for assessment API
        return {
            "ready": 12,
            "needs_changes": 4,
            "not_supported": 1
        }

    def provide_context(self):
        servers = self.discover_servers()
        readiness = self.assess_readiness()

        return {
            "on_prem_servers": servers,
            "readiness_summary": readiness
        }
