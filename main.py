from tools.calculator import CalculatorTool
from tools.registry import ToolRegistry
from model.llm import LLMClient
from vectorstore.store import VectorStore
from rag.ingestor import DocumentIngestor
from rag.retriever import Retriever
from rag.embedder import Embedder
from memory.memory_manager import MemoryManager
from agent.context import AgentContext
from agent.runtime import AgentRuntime
from orchestration.executor import AgentExecutor
from orchestration.workflow_engine import WorkflowEngine
from api.controller import AgentController

#setup
tool_registry = ToolRegistry()
tool_registry.register(CalculatorTool())

llm = LLMClient()
runtime = AgentRuntime(llm, tool_registry)
executor = AgentExecutor(runtime)
workflow = WorkflowEngine(executor)
controller = AgentController(workflow)

#RAG
Embedder = Embedder()
store = VectorStore()
ingestor = DocumentIngestor(store)
retriever = Retriever(store)

ingestor.ingest([
    "AI agents observe, reason, and act autonomously.",
    "RAG improves factual accuracy by grounding responses.",
    "Vector databases enable semantic similarity search"
])

#Memory
memory = MemoryManager()

#Run Agent
query = "How does RAG improves AI Agensts?"
knowledge = retriever.retrieve(query)
context = AgentContext(
    query=query,
    knowledge=knowledge, 
    memery=memory.recall())

result = controller.run_agent(context)
print("FINAL OUTPUT:",result)