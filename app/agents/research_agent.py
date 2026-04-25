import requests

def research_topic(topic: str):
    """
    Simple research agent (can upgrade later)
    """

    facts = [
        f"{topic} is currently trending globally",
        f"Recent developments related to {topic} increased tensions",
        "Experts believe situation may impact global politics",
        "Economic and military aspects are both involved"
    ]

    sources = [
        "https://news.example.com",
        "https://globaltimes.example.com"
    ]

    return {
        "facts": facts,
        "sources": sources
    }