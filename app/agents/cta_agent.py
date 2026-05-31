from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def cta_agent(state):

    topic = state["topic"]

    hook = state["hook"]

    creator_style = state["creator_style"]

    cta_patterns = creator_style.get(
        "cta_patterns",
        []
    )

    vocabulary_patterns = creator_style.get(
        "vocabulary_patterns",
        []
    )

#     prompt = f"""
# You are writing ONLY the CTA part of a viral reel.

# TOPIC:
# {topic}

# HOOK:
# {hook}

# RULES:
# - Write ONLY 1-2 lines
# - Ask engaging question
# - Encourage comments
# - Conversational Hinglish
# - Natural creator tone
# - No intro
# - No outro
# - No screenplay
# - No formatting
# - No markdown
# - No extra explanation

# GOOD EXAMPLES:

# "Kya aapko lagta hai India ka yeh move sahi hai? Comment karo."

# "Aap hote toh kya decision lete? Batao comments me."

# Return ONLY CTA text.
# """
    prompt = f"""
You are writing CTA in creator style.

CTA PATTERNS:
{cta_patterns}

VOCABULARY STYLE:
{vocabulary_patterns}

TOPIC:
{topic}

HOOK:
{hook}

RULES:
- 1-2 lines
- conversational Hinglish
- emotional
- natural sounding
- encourage comments
- match creator personality
- no markdown

Return ONLY CTA text.
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
    
    data = response.choices[0].message.content

    print("data",data)

    return {
        "cta": data
    }