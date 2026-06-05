from openai import OpenAI
from app.core.config import settings
from app.utils.json_parser import safe_json_loads

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def revision_agent(state):

    feedback = "\n".join(
        state.get("feedback", [])
    )

    old_script = state["final_script"]

    creator_style = state.get(
        "creator_style",
        {}
    )

    creator_profile = creator_style.get(
        "creator_profile",
        {}
    )

    hook_patterns = creator_style.get(
        "hook_patterns",
        []
    )

    story_structures = creator_style.get(
        "story_structures",
        []
    )

    pacing_patterns = creator_style.get(
        "pacing_patterns",
        []
    )

    emotion_patterns = creator_style.get(
        "emotion_patterns",
        []
    )

    vocabulary_patterns = creator_style.get(
        "vocabulary_patterns",
        []
    )

    psychological_triggers = creator_style.get(
        "psychological_triggers",
        []
    )

    cta_patterns = creator_style.get(
        "cta_patterns",
        []
    )

    print(
        "REVISION RETRY:",
        state.get("retry_count", 0)
    )

    prompt = f"""
You are rewriting a viral reel script.

Your goal:
Improve the script while matching creator style PERFECTLY.

CREATOR PROFILE:
{creator_profile}

HOOK STYLES:
{hook_patterns}

STORY STRUCTURES:
{story_structures}

PACING STYLES:
{pacing_patterns}

EMOTIONAL PATTERNS:
{emotion_patterns}

VOCABULARY STYLE:
{vocabulary_patterns}

PSYCHOLOGICAL TRIGGERS:
{psychological_triggers}

CTA STYLES:
{cta_patterns}

OLD SCRIPT:

HOOK:
{old_script.get("hook", "")}

BODY:
{old_script.get("body", "")}

CTA:
{old_script.get("cta", "")}

CRITIC FEEDBACK:
{feedback}

YOUR TASK:
Rewrite the script better.

IMPORTANT:
- Keep creator tone strong
- Improve emotional pacing
- Increase retention
- Add stronger curiosity
- Make it sound human
- Make transitions smoother
- Make hook stronger
- Avoid robotic writing
- Avoid generic lines
- Keep Hinglish natural
- Make viewers continue watching

RULES:
- No screenplay
- No scene directions
- No markdown
- No narrator tags
- No quotes unless necessary

Return STRICT JSON ONLY:

{{
    "hook": "",
    "body": "",
    "cta": ""
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        response_format={
            "type": "json_object"
        },

        temperature=0.9,

        messages=[
            {
                "role": "system",
                "content": """
You are an elite viral content rewriter.

You specialize in:
- retention engineering
- creator-style rewriting
- emotional pacing
- cinematic storytelling

You rewrite weak scripts into highly engaging reels.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = (
        response.choices[0]
        .message.content
    )

    parsed = safe_json_loads(content)

    print("REVISION RESULT:", parsed)

    return {

        "hook": parsed.get(
            "hook",
            ""
        ),

        "body": parsed.get(
            "body",
            ""
        ),

        "cta": parsed.get(
            "cta",
            ""
        ),

        "final_script": parsed,

        "retry_count": state.get(
            "retry_count",
            0
        ) + 1
    }