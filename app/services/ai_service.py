from openai import OpenAI
from app.core.config import settings
import json

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_script_ai(topic: str, tone: str, context: dict):

    facts_text = "\n".join(context.get("facts", []))

    prompt = f"""
You are an elite viral short-form reel script writer.

Your job is to create highly engaging Instagram Reel / YouTube Shorts scripts.

TOPIC:
{topic}

TONE:
{tone}

REAL RESEARCH FACTS:
{facts_text}

IMPORTANT INSTRUCTIONS:

1. Use ONLY the provided research facts.
2. Do NOT create fake timelines, fake news, or imaginary facts.
3. Script should feel dramatic, emotional, and curiosity-driven.
4. Use conversational Hinglish.
5. Write short punchy lines.
6. Every sentence should feel cinematic.
7. Keep audience retention very high.
8. Avoid robotic language.
9. Avoid repeating the topic too much.
10. Make the hook extremely attention-grabbing.

HOOK RULES:
- Maximum 2 lines
- Create curiosity instantly
- Should emotionally trigger viewer
- Should feel like "wait... what?!"

BODY RULES:
- Use storytelling flow
- Add suspense naturally
- Use short impactful sentences
- Keep rhythm dynamic
- Do not use giant paragraphs
- Each sentence max 15-18 words
- Explain facts in simple Hinglish

CTA RULES:
- Ask engaging question
- Encourage comments/shares
- Sound natural, not spammy

HASHTAG RULES:
- Generate 5 highly relevant hashtags
- Avoid generic hashtags like #viral #fyp
- Use niche/topic-specific hashtags

OUTPUT FORMAT:
Return ONLY valid JSON.

{{
  "hook": "...",
  "body": "...",
  "cta": "...",
  "hashtags": [
    "#IndiaIran",
    "#Geopolitics",
    "#MiddleEast",
    "#WorldNews",
    "#IndiaNews"
  ]
}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        temperature=0.9,
        messages=[
            {
            "role": "system",
            "content": """
You are a world-class viral short-form content strategist.
Never invent fake facts.
Keep scripts cinematic and emotional.
"""
        },
        {
            "role": "user",
            "content": prompt
        }
        ]
    )

    content = response.choices[0].message.content

    parsed = json.loads(content)

    return {
        "script": {
            "hook": parsed.get("hook"),
            "body": parsed.get("body"),
            "cta": parsed.get("cta")
        },
        "hashtags": parsed.get("hashtags", []),
        "sources": context.get("sources", []),
        "quality_score": calculate_score(parsed)
    }


def calculate_score(script: dict) -> float:

    score = 0

    if len(script.get("hook", "")) > 20:
        score += 3

    if len(script.get("body", "")) > 100:
        score += 3

    if "?" in script.get("hook", ""):
        score += 2

    if "comment" in script.get("cta", "").lower():
        score += 2

    return min(score, 10)


def format_script(script: dict) -> str:

    return f"""
🎯 HOOK:
{script.get("hook")}

📖 BODY:
{script.get("body")}

📢 CTA:
{script.get("cta")}
"""