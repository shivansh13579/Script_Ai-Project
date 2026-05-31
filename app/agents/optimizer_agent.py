def optimizer_agent(state):

    final_script = {
        "hook": state.get("hook", ""),
        "body": state.get("body", ""),
        "cta": state.get("cta", "")
    }

    print("final_script",final_script)

    return {
        "final_script": final_script,

        "hashtags": [
            "#news",
            "#india",
            "#worldnews",
            "#viral",
            "#geopolitics"
        ],

        "sources": state.get("sources", [])
    }