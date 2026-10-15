# Working on Adam's profile

This repository preserves Adam Smith's current LinkedIn experience and provides a GitHub Pages website that can be improved from different computers and AI tools.

- Read README.md, PROFILE.md, and content/profile.json before editing.
- content/profile.json is the editable source of truth. Run `python build.py` after changes and commit the generated index.html and PROFILE.md with it.
- Keep source/linkedin-original.txt unchanged as the original baseline.
- Preserve facts, dates, metrics, and attribution unless Adam supplies a correction. Do not turn a contribution into sole ownership or invent experience, credentials, skills, or project details.
- Only the experience section was supplied. Missing headline, About, education, and other details should be requested when needed, never invented.
- Keep the site static and dependency-free unless a requested feature requires more. Relative asset paths must work under /linkedin-profile/ on GitHub Pages.
- Use a focused branch and pull request for proposed improvements. Do not rewrite history or force-push.
- Validate JSON, run the builder, and inspect changed content. For visual edits, check desktop and mobile layouts and all navigation links.
- Updating this repository does not edit the LinkedIn profile itself.
