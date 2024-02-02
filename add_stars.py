import sys
import re


def match_repos(text):
    pattern = r"(\[(\w+/?\w*)\]\(https?://github\.com/([\w-]+)/([\w-]+)/?\w*\))"
    
    match = re.findall(pattern, text)
    if match:
        return match


def add_star(text, repos):
    """
<img src="https://img.shields.io/github/stars/OWNER/REPO?style=social" alt="Stars">
<img src="https://img.shields.io/github/forks/OWNER/REPO?style=social" alt="Forks">
    """
    for repo in repos:
        repo_text = repo[0]
        owner = repo[2]
        repo_name = repo[3]
        #star_text = f'![Stars](https://img.shields.io/github/stars/{owner}/{repo_name}?style=social)'
        star_text = f' <img src="https://img.shields.io/github/stars/{owner}/{repo_name}?style=social" alt="Stars" width="80">'
        text = text.replace(repo_text, f'{repo_text}{star_text}')
    return text



tmp_f = open('tmp.md', 'w')
for l in open(sys.argv[1]):
    # * [Fractalide](https://github.com/fractalide/fractalide) 
    print(l)
    if 'stars' not in l:
        repos = match_repos(l)
        if repos:
            l = add_star(l, repos)
    tmp_f.write(l)
tmp_f.close()

