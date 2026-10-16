# Adam Smith — LinkedIn profile

A versioned home for my current LinkedIn experience, with a simple public website and source files that people and AI assistants can improve from any computer.

- [Website](https://adamqjsmith.github.io/linkedin-profile/)
- [LinkedIn](https://www.linkedin.com/in/adam-smith-5bb8661ab/)
- [Readable current profile](PROFILE.md)
- [Editable profile content](content/profile.json)
- [LinkedIn update checklist](LINKEDIN-UPDATE.md)
- [Original pasted text](source/linkedin-original.txt)

## Current version

Updated October 15, 2026 for Adam's move to Engineer, Retail R&D at Shopify. Shopify positions now match the official titles and dates in Workday. Each role is summed up in up to 3 short lines; the longer versions with metrics stay in source/linkedin-original.txt. AGENTS.md has the style rules and writing rules for future edits.

Only the supplied experience section is included. The short website heading is presentation copy and is not a LinkedIn headline. The site does not synchronize with LinkedIn. LINKEDIN-UPDATE.md lists the changes to make there.

## Edit from another computer

Clone this repository, open it in your editor or AI coding tool, and read AGENTS.md:

```sh
git clone https://github.com/AdamQJSmith/linkedin-profile.git
cd linkedin-profile
git switch -c codex/profile-improvements
```

Edit `content/profile.json` for wording and professional details, `styles.css` for appearance, or `build.py` for layout. Then regenerate the page and readable profile:

```sh
python build.py
```

Open `index.html` in a browser, or preview with:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Visit http://127.0.0.1:8000. No packages or API keys are needed. Commit the source changes together with `index.html` and `PROFILE.md`, push your branch, and open a pull request. If you do not have write access, fork the repository first.

Suggested prompt for another AI tool:

> Read README.md, AGENTS.md, PROFILE.md, LINKEDIN-UPDATE.md and content/profile.json. Help improve this professional profile while preserving the supplied facts and contribution attribution. Follow the style and writing rules in AGENTS.md. Make changes on a branch, run python build.py and present the changes for review.

## Hosting

GitHub Pages serves `main` from `/(root)`. The generated HTML is committed, so hosting requires no custom build service. Merging updates to `main` republishes the site. If configuring a fresh copy, use Settings → Pages → Deploy from a branch → main → /(root). See [GitHub's publishing instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

The public website can be viewed without a GitHub account. Editing and submitting pull requests require appropriate GitHub access.
