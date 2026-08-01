import os
from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

# Set your API key
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# 1. Define the Shared State Schema
class LoopState(TypedDict):
    topic: str
    draft: str
    critique: str
    revision_number: int
    approved: bool

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

# 2. Define the Writer Node
def writer_node(state: LoopState) -> dict:
    topic = state["topic"]
    draft = state.get("draft", "")
    critique = state.get("critique", "")
    revision = state.get("revision_number", 0)

    if revision == 0:
        prompt = f"Write a clear, comprehensive, and engaging 2-paragraph overview about: {topic}"
    else:
        prompt = (
            f"Rewrite the following draft about '{topic}' based on this critique:\n\n"
            f"CRITIQUE: {critique}\n\n"
            f"CURRENT DRAFT:\n{draft}"
        )

    response = llm.invoke(prompt)
    return {
        "draft": response.content,
        "revision_number": revision + 1
    }

# 3. Define the Critic Node
def critic_node(state: LoopState) -> dict:
    draft = state["draft"]
    
    prompt = (
        f"Review this draft. Is it clear, factual, and well-written? "
        f"If it is acceptable, reply with 'APPROVED'. "
        f"If it needs changes, reply with 'NEEDS_WORK' followed by a short critique.\n\n"
        f"DRAFT:\n{draft}"
    )
    
    response = llm.invoke(prompt)
    content = response.content
    
    if "APPROVED" in content:
        return {"critique": "Approved", "approved": True}
    else:
        return {"critique": content, "approved": False}

# 4. Define Conditional Routing Logic (The Loop Controller)
def should_continue(state: LoopState) -> str:
    # Exit loop if approved
    if state["approved"]:
        return "end"
    
    # Exit loop if max revisions (e.g., 3) are reached to avoid infinite token waste
    if state["revision_number"] >= 3:
        return "end"
        
    # Otherwise, loop back to the writer
    return "revise"

# 5. Build and Compile the Graph
workflow = StateGraph(LoopState)

# Add nodes
workflow.add_node("writer", writer_node)
workflow.add_node("critic", critic_node)

# Set entry point
workflow.set_entry_point("writer")

# Add sequential flow from writer to critic
workflow.add_edge("writer", "critic")

# Add conditional loop edge from critic back to writer (or exit)
workflow.add_conditional_edges(
    "critic",
    should_continue,
    {
        "revise": "writer",
        "end": END
    }
)

# Compile into an executable application
app = workflow.compile()

# 6. Execute the Multi-Agent Loop
if __name__ == "__main__":
    initial_state = {
        "topic": "The mechanics of black hole event horizons",
        "draft": "",
        "critique": "",
        "revision_number": 0,
        "approved": False
    }
    
    print("--- Starting Multi-Agent Loop ---")
    final_state = app.invoke(initial_state)
    
    print(f"\nFinished after {final_state['revision_number']} iterations.")
    print(f"Final Approval Status: {final_state['approved']}")
    print(f"\nFinal Output:\n{final_state['draft']}")