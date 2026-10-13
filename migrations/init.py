import os
import re


def verify(ctx):
    issues = []
    p = os.path.join(ctx.root, "wiki", "projects.md")
    if not os.path.exists(p):
        issues.append(("error", "wiki/projects.md declaration page missing"))
    elif not re.search(r"^type:\s*project\s*$", open(p, encoding="utf-8").read(), re.M):
        issues.append(("error", "wiki/projects.md missing `type: project`"))
    return issues
