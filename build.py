"""Build the static page and readable profile. Python 3, no dependencies."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
profile = json.loads((ROOT / 'content/profile.json').read_text(encoding='utf-8'))
e = escape
sections = []
current = []
markdown = [f"# {profile['name']}: Experience", '',
            f"[LinkedIn]({profile['linkedin']})", '',
            f"Updated {profile['updated']}. Edit content/profile.json and run python build.py. The original LinkedIn text from {profile['snapshot_date']} is in source/linkedin-original.txt.", '',
            '## About', '', *[p + '\n' for p in profile['about']]]
for company in profile['companies']:
    roles = []
    markdown += [f"## {company['name']}", '']
    for role in company['roles']:
        body = ''.join(f'<p>{e(p)}</p>' for p in role['paragraphs'])
        if role['bullets']:
            body += '<ul>' + ''.join(f'<li>{e(b)}</li>' for b in role['bullets']) + '</ul>'
        skills = ''.join(f'<span>{e(s)}</span>' for s in role['skills'])
        skills_html = f'<div class="skills" aria-label="Listed skills">{skills}</div>' if skills else ''
        if role['dates'].endswith('Present'):
            current.append((role['title'], company['name'], role['dates'].split(' to ')[0]))
        roles.append(f'''<article class="role">
          <div class="role-heading"><h3>{e(role['title'])}</h3><p class="dates">{e(role['dates'])}</p></div>
          <p class="meta">{e(role['employment'])} · {e(role['location'])}</p>
          <div class="role-body">{body}</div>
          {skills_html}
        </article>''')
        markdown += [f"### {role['title']}", '', role['dates'], '',
                     f"{role['employment']} · {role['location']}", '',
                     *[p + '\n' for p in role['paragraphs']],
                     *['- ' + b for b in role['bullets']], '',
                     *(['Listed skills: ' + ', '.join(role['skills']), ''] if role['skills'] else [])]
    sections.append(f'''<section class="company" id="{e(company['id'])}" aria-labelledby="{e(company['id'])}-heading">
      <div class="company-label"><span class="company-number">{len(sections)+1:02d}</span><h2 id="{e(company['id'])}-heading">{e(company['name'])}</h2></div>
      <div class="company-roles">{''.join(roles)}</div>
    </section>''')

now = '<hr>'.join(f'<p class="now-title">{e(t)}</p><p>{e(c)} <span>· Since {e(d)}</span></p>' for t, c, d in current)
nav = ''.join(f'<a href="#{e(c["id"])}">{e(c["short_name"])}</a>' for c in profile['companies'])
html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(profile['name'])} | Professional experience</title>
  <meta name="description" content="Adam Smith’s professional experience across Shopify, VersaStrength, customer development and operations.">
  <meta name="theme-color" content="#153e35">
  <link rel="stylesheet" href="./styles.css">
  <link rel="icon" href="./favicon.svg" type="image/svg+xml">
</head>
<body id="top">
  <a class="skip-link" href="#experience">Skip to experience</a>
  <div class="page">
    <header class="site-header">
      <a class="brand" href="#top"><span class="monogram" aria-hidden="true">AS</span>{e(profile['name'])}</a>
      <a class="header-link" href="{e(profile['linkedin'])}">LinkedIn <span aria-hidden="true">↗</span></a>
    </header>
    <main>
      <section class="hero" aria-labelledby="intro-heading">
        <div>
          <p class="eyebrow">Professional experience</p>
          <h1 id="intro-heading">{e(profile['hero']['line1'])}<br><em>{e(profile['hero']['line2'])}</em></h1>
          {''.join(f'<p class="intro">{e(p)}</p>' for p in profile['about'])}
          <a class="button" href="#experience">Explore my experience <span aria-hidden="true">↓</span></a>
        </div>
        <aside class="now" aria-label="Current roles">
          <p class="eyebrow">Currently</p>
          {now}
        </aside>
      </section>
      <div class="experience-top" id="experience"><h2>Experience</h2><p>2010 to Present</p></div>
      <nav class="company-nav" aria-label="Jump to company">{nav}</nav>
      {''.join(sections)}
      <section class="connect" aria-labelledby="connect-heading">
        <div><p class="eyebrow">Continue the conversation</p><h2 id="connect-heading">Find me on LinkedIn.</h2></div>
        <a class="button" href="{e(profile['linkedin'])}">Visit my profile <span aria-hidden="true">↗</span></a>
      </section>
    </main>
    <footer><p>{e(profile['name'])} <span>· Updated {e(profile['updated'])}</span></p><a href="{e(profile['repository'])}">Source &amp; contributions <span aria-hidden="true">↗</span></a></footer>
  </div>
</body>
</html>
'''
(ROOT / 'index.html').write_text(html, encoding='utf-8')
(ROOT / 'PROFILE.md').write_text('\n'.join(markdown), encoding='utf-8')
print(f"Built index.html and PROFILE.md: {len(profile['companies'])} companies, {sum(len(c['roles']) for c in profile['companies'])} roles.")
