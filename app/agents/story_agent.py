from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def story_agent(state):

    topic = state["topic"]

    facts = "\n".join(
        state["raw_research"]["facts"]
    )

    hook = state["hook"]

    creator_style = state["creator_style"]

    story_structures = creator_style.get(
        "story_structures",[]
    )

    pacing_patterns = creator_style.get("pacing_patterns",[])

    emotion_patterns = creator_style.get("emotion_patterns", [])

    vocabulary_patterns = creator_style.get("vocabulary_patterns",[])

    research_patterns = creator_style.get("research_patterns",[])

#     prompt = f"""
# You are writing a HIGH-RETENTION Instagram Reel script.

# TOPIC:
# {topic}

# HOOK:
# {hook}

# FACTS:
# {facts}

# STYLE RULES:

# - Write like a modern viral news creator
# - NOT documentary style
# - NOT screenplay style
# - NO scene directions
# - NO narrator labels
# - NO [cut to]
# - NO cinematic instructions

# Use:
# - short punchy lines
# - conversational Hinglish
# - emotional tension
# - curiosity gaps
# - dramatic pacing

# Every 1-2 lines should create curiosity.

# IMPORTANT:
# - Keep sentences short
# - Maximum 12-14 words per sentence
# - Add pauses naturally
# - Sound human
# - Sound urgent
# - Keep audience retention high

# STRUCTURE:
# 1. Explain shocking statement
# 2. Explain WHY it happened
# 3. Explain consequences
# 4. Build tension
# 5. End with open loop

# Do NOT write random motivational lines.
# Every line must push story forward.

# Only use facts from research.
# Do not invent unrelated emotional lines.

# BAD STYLE:
# "[Opening shot]"
# "[Narrator]"
# "[Cut to]"


# Return ONLY plain text body.
# """
    
    prompt = f"""
You are writing a viral reel EXACTLY in this creator style.

CREATOR STORY STRUCTURES:
{story_structures}

CREATOR PACING:
{pacing_patterns}

EMOTIONAL STYLE:
{emotion_patterns}

VOCABULARY STYLE:
{vocabulary_patterns}

RESEARCH USAGE STYLE:
{research_patterns}

TOPIC:
{topic}

HOOK:
{hook}

FACTS:
{facts}

RULES:
- Conversational Hinglish
- Short punchy lines
- Emotional pacing
- Curiosity loops
- High retention
- Human sounding
- No screenplay
- No narration tags
- No scene directions
- No markdown

IMPORTANT:
Match creator pacing and storytelling style strongly.

Return ONLY body text.
"""
    

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.9,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    body = response.choices[0].message.content

    print("body11",body)

    return {
        "body": body
    }