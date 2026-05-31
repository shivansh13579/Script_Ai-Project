from langgraph.graph import StateGraph,END

from app.graph.state import GraphState

from app.agents.research_agent import research_agent
from app.agents.hook_agent import hook_agent
from app.agents.story_agent import story_agent
from app.agents.cta_agent import cta_agent
from app.agents.optimizer_agent import optimizer_agent
from app.agents.critic_agent import critic_agent
from app.agents.revision_agent import revision_agent
from app.agents.load_creator_agent import load_creator_agent

workflow = StateGraph(GraphState)

workflow.add_node(
    "research",research_agent
)

workflow.add_node(
    "creator_loader",
    load_creator_agent
)


workflow.add_node(
    "hook",
    hook_agent
)

workflow.add_node(
    "story",
    story_agent
)

workflow.add_node(
   "cta",
    cta_agent
)

workflow.add_node(
    "optimizer",
    optimizer_agent
)

workflow.add_node(
    "critic",
    critic_agent
)

workflow.add_node(
    "revision",
    revision_agent
)

workflow.set_entry_point("research")

workflow.add_edge(
    "research",
    "creator_loader"
)

workflow.add_edge(
    "creator_loader",
    "hook"
)

workflow.add_edge(
    "hook",
    "story"
)

workflow.add_edge(
    "story",
    "cta"
)

workflow.add_edge(
    "cta",
    "optimizer"
)

workflow.add_edge(
    "optimizer",
    "critic"
)

def should_retry(state):

    if(
        state.get("needs_revision",False)
        and state.get("retry_count", 0) < 2
    ): 
        return "revision"
    return END

workflow.add_conditional_edges(
    "critic",
    should_retry,
    {
        "revision": "revision",
        END: END
    }
)

workflow.add_edge(
    "revision",
    "critic"
)

graph = workflow.compile()

# Research
#    ↓
# Hook
#    ↓
# Story
#    ↓
# CTA
#    ↓
# Optimizer
#    ↓
# Critic
#    ↓
# [Bad?]
#    ↓ YES
# Revision
#    ↓
# Critic Again
#    ↓
# END