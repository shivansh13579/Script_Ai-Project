from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def hook_agent(state):

    topic = state["topic"]

    print("topic111",topic)

    facts = "\n".join(
        state["raw_research"]["facts"]
    )

    creator_style = state["creator_style"]

    creator_profile = creator_style.get("creator_profile",{})

    hook_patterns = creator_style.get(
        "hook_patterns",
        []
    )

    emotion_patterns = creator_style.get(
        "emotion_patterns",
        []
    )

    vocabulary_patterns = creator_style.get(
        "vocabulary_patterns",[]
    )

    psychological_triggers = creator_style.get(
        "psychological_triggers",
        []
    )

    print("facts111",facts)

    prompt = f"""
You are writing hooks EXACTLY like this creator.

CREATOR PROFILE:
{creator_profile}

HOOK STYLES:
{hook_patterns}

EMOTIONAL PATTERNS:
{emotion_patterns}

VOCABULARY STYLE:
{vocabulary_patterns}

PSYCHOLOGICAL TRIGGERS:
{psychological_triggers}

TOPIC:
{topic}

FACTS:
{facts}

YOUR TASK:
Create ONLY 1 viral hook.

RULES:
- Maximum 2 lines
- Curiosity-driven
- Emotional tension
- Conversational Hinglish
- Human sounding
- High-retention
- No fake claims
- No quotes
- No screenplay
- No markdown
- Match creator personality strongly

Return ONLY hook text.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("response11",response)

    hook = (
        response.choices[0]
        .message.content
        .replace('"', "")
        .strip()
    )

    print("hook",hook)

    return {
        "hook": hook
    }