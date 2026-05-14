from langgraph.graph import StateGraph, END

from app.state import GraphState
from app.retrieve import retrieve
from app.generate import generate
from app.critic import critic
from app.rewrite import rewrite

workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_node("critic", critic)
workflow.add_node("rewrite", rewrite)

workflow.set_entry_point("retrieve")

workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "critic")

def route_decision(state):
    if state["critic_decision"] == "PASS":
        return END

    if state["retries"] >= 3:
        return END

    return "rewrite"

workflow.add_conditional_edges(
    "critic",
    route_decision,
    {
        "rewrite": "rewrite",
        END: END
    }
)

workflow.add_edge("rewrite", "retrieve")

graph = workflow.compile()