from typing import TypedDict, List, Dict

class GraphState(TypedDict, total=False):

    topic: str
    tone: str
    creator: str
    creator_style: Dict

    raw_research: Dict

    hook: str
    body: str
    cta: str

    final_script: Dict

    formatted_script: str

    hashtags: List[str]

    sources: List[str]

    quality_score: int

    retry_count: int

    feedback: List[str]

    needs_revision: bool

    draft_script: Dict