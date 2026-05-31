from tavily import TavilyClient
from app.core.config import settings
from app.core.logger import logger

client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)

def research_agent(state):
    print("state",state)
    topic = state["topic"]
    print("topic",topic)

    response = client.search(
        query=topic,
        search_depth="advanced",
        max_results=5
    )

    print("response",response)

    facts = []
    sources = []

    blocked_words = [
        "sign in",
        "create account",
        "advertisement",
        "watch live",
        "login"
    ]

    for result in response.get("results", []):

        title = result.get("title", "")
        content = result.get("content", "")
        url = result.get("url", "")

        clean_content = content.lower()

        if any(word in clean_content for word in blocked_words):
            continue

        short_fact = (
            f"{title}: "
            f"{content[:200].replace(chr(10), ' ')}"
        )
        
        print("short_fact",short_fact)
        facts.append(short_fact)
        sources.append(url)

    logger.info(f"Research completed for topic: {topic}")

    print("facts",facts)
    print("sources",sources)

    return {
        "raw_research": {
            "facts": facts
        },
        "sources": sources
    }