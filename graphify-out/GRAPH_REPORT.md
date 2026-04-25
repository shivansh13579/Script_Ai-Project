# Graph Report - C:\Users\shiva\Desktop\script_ai\backend_ai  (2026-04-19)

## Corpus Check
- 10 files · ~545 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 35 nodes · 40 edges · 9 communities detected
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 8 edges (avg confidence: 0.57)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]

## God Nodes (most connected - your core abstractions)
1. `ScriptBase` - 6 edges
2. `Script` - 6 edges
3. `ScriptCreate` - 6 edges
4. `Settings` - 3 edges
5. `ScriptResponse` - 3 edges
6. `create_script()` - 3 edges
7. `Naya script save karo` - 3 edges
8. `Saare scripts fetch karo` - 3 edges
9. `ID se ek script fetch karo` - 3 edges
10. `lifespan()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Naya script save karo` --uses--> `ScriptCreate`  [INFERRED]
  C:\Users\shiva\Desktop\script_ai\backend_ai\app\services\script_service.py → C:\Users\shiva\Desktop\script_ai\backend_ai\app\db\models.py
- `Saare scripts fetch karo` --uses--> `ScriptCreate`  [INFERRED]
  C:\Users\shiva\Desktop\script_ai\backend_ai\app\services\script_service.py → C:\Users\shiva\Desktop\script_ai\backend_ai\app\db\models.py
- `ID se ek script fetch karo` --uses--> `ScriptCreate`  [INFERRED]
  C:\Users\shiva\Desktop\script_ai\backend_ai\app\services\script_service.py → C:\Users\shiva\Desktop\script_ai\backend_ai\app\db\models.py
- `lifespan()` --calls--> `init_db()`  [INFERRED]
  C:\Users\shiva\Desktop\script_ai\backend_ai\app\main.py → C:\Users\shiva\Desktop\script_ai\backend_ai\app\db\database.py
- `Naya script save karo` --uses--> `Script`  [INFERRED]
  C:\Users\shiva\Desktop\script_ai\backend_ai\app\services\script_service.py → C:\Users\shiva\Desktop\script_ai\backend_ai\app\db\models.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.31
Nodes (7): Script, create_script(), get_all_scripts(), get_script_by_id(), Naya script save karo, Saare scripts fetch karo, ID se ek script fetch karo

### Community 1 - "Community 1"
Cohesion: 0.36
Nodes (7): POST request ke liye -- user yeh bhejega, Response ke liye -- yeh user ko milega, Common fields -- shared between create and response, ScriptBase, ScriptCreate, ScriptResponse, SQLModel

### Community 2 - "Community 2"
Cohesion: 0.33
Nodes (2): init_db(), lifespan()

### Community 3 - "Community 3"
Cohesion: 0.5
Nodes (4): BaseSettings, Config, get_settings(), Settings

### Community 4 - "Community 4"
Cohesion: 1.0
Nodes (0): 

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (0): 

### Community 6 - "Community 6"
Cohesion: 1.0
Nodes (0): 

### Community 7 - "Community 7"
Cohesion: 1.0
Nodes (0): 

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **4 isolated node(s):** `Config`, `Common fields -- shared between create and response`, `POST request ke liye -- user yeh bhejega`, `Response ke liye -- yeh user ko milega`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 4`** (2 nodes): `health.py`, `health_check()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 5`** (2 nodes): `logger.py`, `setup_logger()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 6`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 7`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ScriptBase` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `ScriptCreate` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Script` (e.g. with `Naya script save karo` and `Saare scripts fetch karo`) actually correct?**
  _`Script` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `ScriptCreate` (e.g. with `Naya script save karo` and `Saare scripts fetch karo`) actually correct?**
  _`ScriptCreate` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Config`, `Common fields -- shared between create and response`, `POST request ke liye -- user yeh bhejega` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._