from tools.calculator import CalculatorTool
from tools.registry import ToolRegistry
from model.llm import LLMClient
from vectorstore.store import VectorStore
from rag.ingestor import DocumentIngestor
from rag.retriever import Retriever
from rag.embedder import Embedder
from memory.memory_manager import MemoryManager
#from agent.context import AgentContext
from agent.runtime import AgentRuntime
from orchestration.executor import AgentExecutor
from orchestration.workflow_engine import WorkflowEngine
from api.controller import AgentController
from mcp.server import MCPServer
from mcp.context_provider import ContextProvider
from mcp.azure_migrate_provider import AzureMigrateProvider

#setup
tool_registry = ToolRegistry()
tool_registry.register(CalculatorTool())

llm = LLMClient()
runtime = AgentRuntime(llm, tool_registry)
executor = AgentExecutor(runtime)
workflow = WorkflowEngine(executor)
controller = AgentController(workflow)

#RAG
embedder = Embedder()
store = VectorStore()
ingestor = DocumentIngestor(store, embedder)
retriever = Retriever(store, embedder)

ingestor.ingest([
    "RAG improves LLM accuracy by grounding responses in external data.",
    "Vector embeddings capture semantic meaning of text.",
    "AI agents combine reasoning, memory, and tools."
])

#Memory
memory = MemoryManager()

#Run Agent
# query = "How does RAG improves AI Agents?"
# knowledge = retriever.retrieve(query)
# print("knowledge", knowledge)
# context = AgentContext(
#     query=query,
#     knowledge=knowledge, 
#     memory=memory.recall())

azure_provider = AzureMigrateProvider(
    subscription_id = "89cf22e2-fdb7-4274-b120-c36e0851da00",
    resource_group = "migrationactivity",
    project_name = "project-migration",
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlBjWDk4R1g0MjBUMVg2c0JEa3poUW1xZ3dNVSIsImtpZCI6IlBjWDk4R1g0MjBUMVg2c0JEa3poUW1xZ3dNVSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NjQzOTkxNC02M2I3LTQ2NGUtODMyNy05YjEzNzM3YWU4Y2YvIiwiaWF0IjoxNzcwMTE0NjU3LCJuYmYiOjE3NzAxMTQ2NTcsImV4cCI6MTc3MDEyMDI4NywiYWNyIjoiMSIsImFjcnMiOlsicDEiXSwiYWlvIjoiQWNRQU8vOGJBQUFBdnZadWVkMDBwVXhhclRnYjV1YlV2SmdITXVFUmEzbmgxbTgrRVgzdkE1Ti9EcUhlcXlHSkg1TTV2czV2VmRGNk9qVmIwS1V5a0ZGMTZUbDEvMzNMU1NIcjRLMFk3dzNXSXpsTzZuTWY4UUUvZklrUWJvbnNUbGFpYnZGTkg4WjNNaEg1T1ZDMmlIQWQ1UkZoMlJVZjhVYTM1d3YraDdUdVRUc1JoeGhVTWJrbGlwajFZM05ZVzg1NFBUUGV4bXpRRnFKL1FJQmhDaWYxdXVzTTBDZEh4NnJpd1d2OU8wNHM4THBCUlpNSWVWZ0MrQjI0UzlIV2ZUejVRc0tHYXQ4MSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwaWQiOiJiNjc3YzI5MC1jZjRiLTRhOGUtYTYwZS05MWJhNjUwYTRhYmUiLCJhcHBpZGFjciI6IjAiLCJkZXZpY2VpZCI6IjA4NTA5MWVkLTM4MjgtNDBiYS1hZjdiLTM1ZDQ1MmJmNGE2YyIsImZhbWlseV9uYW1lIjoiR292YWRhIiwiZ2l2ZW5fbmFtZSI6IlNyaW5pdmFzYSBSYW8iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyNy4xMDcuMjguOTgiLCJuYW1lIjoiU3Jpbml2YXNhIFJhbyBHb3ZhZGEiLCJvaWQiOiJmMTU2NGUzNS03N2RmLTRkZjMtYTZmMy1lMDYyMmM3MDVjZGYiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTkyODY2ODI1Ni0yODU5NTExNTIxLTE0NjU4OTAzNi01NDIzMSIsInB1aWQiOiIxMDAzMjAwNDJDNzVENjY0IiwicmgiOiIxLkFVb0FGSmxEUnJkalRrYURKNXNUYzNyb3owWklmM2tBdXRkUHVrUGF3ZmoyTUJNakFYVktBQS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzaWQiOiIwMGFiZDg0OS03Y2U2LWIwNDQtOTZlNS0wOTMzNDdlZjVlZTYiLCJzdWIiOiIwSzhEUnZPUDdRcEMwZ1ZXNmpTZTdNOFZKYl9FbzZZZ0hBb3FjS0c3ekg0IiwidGlkIjoiNDY0Mzk5MTQtNjNiNy00NjRlLTgzMjctOWIxMzczN2FlOGNmIiwidW5pcXVlX25hbWUiOiJzZ292YWRhQGlubm9taW5kcy5jb20iLCJ1cG4iOiJzZ292YWRhQGlubm9taW5kcy5jb20iLCJ1dGkiOiJZbEJuV0lvWXZFNlF5NGZVWXhJTkFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2FjdF9mY3QiOiIzIDUiLCJ4bXNfZnRkIjoiSWtZdlVSVzhIWEFQQ09fOHdkZzJkcnZyZkRQRTBIYVBaVk93ZjlDVDNLMEJZWE5wWVhOdmRYUm9aV0Z6ZEMxa2MyMXoiLCJ4bXNfaWRyZWwiOiIyMiAxIiwieG1zX3N1Yl9mY3QiOiIzIDEyIiwieG1zX3RjZHQiOjE0MTUxMDAwMDh9.K_2hxLyeCE0ElAF2Epq5_Z3rwpjCVwGzJK4ti4ZX8mWauuGKEgZt7W0kcMCQ0XzNMookilTwkSdkQqvqMITzh8te62C6TQ_2I4uPei2B1uekjkvzDb7xfjyR3pz7ZRbDMcCLiCNnkRMSoKL-XTS73_ACr3KcySf6rF9dGin7ut-1gZopDPbqwNFusxTabITYzcIubz--Y7IzBXn3ILIKHAiPEO2dm_yjttgulAqKefidvQCsPtejGk-LbUC2x6f6haXwZLePNuW5VsAtR3EgJ7JlvXsJVnXnu2wYBoEiGgCfrwP370FNZnzjIypKY8TFI9TijP6hOIKtzIxassRESw"
)
context_provider = ContextProvider(
    rag_retriever= retriever,
    memory_manager= memory,
    azure_migrate_provider= azure_provider
)

mcp_server = MCPServer(context_provider)
runtime = AgentRuntime(llm, mcp_server)

result = runtime.run(
    agent_id="cloud_migration_agent",
    query="Assess rediness and suggest migration strategy"
    )

print("FINAL OUTPUT:",result)