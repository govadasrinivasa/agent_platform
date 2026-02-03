from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

TARGET_API_URL = "https://management.azure.com/subscriptions/89cf22e2-fdb7-4274-b120-c36e0851da00/resourceGroups/migrationactivity/providers/Microsoft.Migrate/migrateProjects/project-migration/machines?api-version=2018-09-01-preview"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlBjWDk4R1g0MjBUMVg2c0JEa3poUW1xZ3dNVSIsImtpZCI6IlBjWDk4R1g0MjBUMVg2c0JEa3poUW1xZ3dNVSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NjQzOTkxNC02M2I3LTQ2NGUtODMyNy05YjEzNzM3YWU4Y2YvIiwiaWF0IjoxNzcwMDI1OTMzLCJuYmYiOjE3NzAwMjU5MzMsImV4cCI6MTc3MDAzMDE4MCwiYWNyIjoiMSIsImFjcnMiOlsicDEiXSwiYWlvIjoiQWNRQU8vOGJBQUFBZ0JxZ2d4SDhNRFc4YnBGN0tpem5xZ0x4aWE3aGZMSjcvVU5BeXc1TjVUTUtsTGlEVjNsenlYYkN3SU5PclZXcHgxMmVHRDhWTkJBYmpYTGNodC9BQzloWkkxN2dXeG1JYktoYjdxYS85Q0dRZVVTejJlUDh2TEgwWjRkRXFNU25NLzZ2QzJpeXhyY2xKMUlzajhQODBMaWU3RkhnUUFBMHhDMmZZcmpHQlhHUW51V292MFBHcXBhdVRpanlHS0twdmRzQmNVZWs5NlRFbG11NXhyWjlYWXhaaFNuY3pIYWlCRDFZR1hIM1FFSmMvRE5GYnJjR1dMbm1JWGU1TjkrdyIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwaWQiOiJiNjc3YzI5MC1jZjRiLTRhOGUtYTYwZS05MWJhNjUwYTRhYmUiLCJhcHBpZGFjciI6IjAiLCJkZXZpY2VpZCI6IjA4NTA5MWVkLTM4MjgtNDBiYS1hZjdiLTM1ZDQ1MmJmNGE2YyIsImZhbWlseV9uYW1lIjoiR292YWRhIiwiZ2l2ZW5fbmFtZSI6IlNyaW5pdmFzYSBSYW8iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMjIuMTY3LjExMi45OCIsIm5hbWUiOiJTcmluaXZhc2EgUmFvIEdvdmFkYSIsIm9pZCI6ImYxNTY0ZTM1LTc3ZGYtNGRmMy1hNmYzLWUwNjIyYzcwNWNkZiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xOTI4NjY4MjU2LTI4NTk1MTE1MjEtMTQ2NTg5MDM2LTU0MjMxIiwicHVpZCI6IjEwMDMyMDA0MkM3NUQ2NjQiLCJyaCI6IjEuQVVvQUZKbERScmRqVGthREo1c1RjM3JvejBaSWYza0F1dGRQdWtQYXdmajJNQk1qQVhWS0FBLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInNpZCI6IjAwYWJkODQ5LTdjZTYtYjA0NC05NmU1LTA5MzM0N2VmNWVlNiIsInN1YiI6IjBLOERSdk9QN1FwQzBnVlc2alNlN004VkpiX0VvNllnSEFvcWNLRzd6SDQiLCJ0aWQiOiI0NjQzOTkxNC02M2I3LTQ2NGUtODMyNy05YjEzNzM3YWU4Y2YiLCJ1bmlxdWVfbmFtZSI6InNnb3ZhZGFAaW5ub21pbmRzLmNvbSIsInVwbiI6InNnb3ZhZGFAaW5ub21pbmRzLmNvbSIsInV0aSI6ImREbC1vdDRQQ0VDaWYwYS03aVdSQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfYWN0X2ZjdCI6IjMgNSIsInhtc19mdGQiOiJhcUo1X0RIYmxOMS1qdncwcXlOTUxKbWZFRVlCRGVwNU85aUsxNWtJUlJRQmFtRndZVzVsWVhOMExXUnpiWE0iLCJ4bXNfaWRyZWwiOiIxIDMyIiwieG1zX3N1Yl9mY3QiOiIzIDQiLCJ4bXNfdGNkdCI6MTQxNTEwMDAwOH0.BiGnCHHnxWI_jTXHR9okAuLejDRniD6VUGoGlt4LOSt77AG9Z0EMj1CnQd5XZIP7VHHkGGf_bkLYgVJYhJkO-K_2mN43HARb-n0ORxhHar_utukbamgz5EBTUzHM0m_QFuzgBDZ__PHNmjsSs3ADfFoJ43kbcpJF0mZ2u8r4APLjb7F4LpvrS9o-6nfH5_gNnwJThv9KIF6TuxnBV_vom7AzORkh5PVb4p0JUBuAJ-MI0eBuIgWrWN5XRfKXodI4LNm-9fQ-HZZpJieLUrrxLgbCYMZKluwP0HQccb-RxxcnZIsIXBPlcLpwIa4CElgNv7dDYVFOLexsIZ4E_dFXDA"


@app.post("/call-external-api")
async def call_external_api(payload: dict):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                TARGET_API_URL,
                json=payload,
                headers=headers
            )

            response.raise_for_status()

            return {
                "status": "success",
                "response": response.json()
            }

    except httpx.HTTPStatusError as e:
        # Remote server returned 4xx / 5xx
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.text
        )

    except httpx.RequestError as e:
        # Network / DNS / connection issues
        raise HTTPException(
            status_code=500,
            detail=f"Request failed: {str(e)}"
        )
