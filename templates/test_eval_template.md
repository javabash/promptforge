---
template: true
name: test_eval_template
description: Evaluate an API response for correctness
tags: [test, langchain, prompt]
---

HUMAN: Here is the response object:

{{response}}

Does it match the expected format?

Expected: status = 200, must include a `data` key.

AI:
{{evaluation}}
