import os
import yaml
import json
import re

repository_path = '.'  # root of your repository

def is_md_file(filename):
    return filename.endswith('.md')

def extract_frontmatter(md_content):
    pattern = r'^---\s*\n(.*?\n?)^---\s*\n'
    matches = re.search(pattern, md_content, re.DOTALL | re.MULTILINE)
    return matches.group(1) if matches else None

# Walk through the repository
for subdir, _, files in os.walk(repository_path):
    for file in files:
        if is_md_file(file):
            file_path = os.path.join(subdir, file)
            with open(file_path, 'r') as f:
                content = f.read()
                frontmatter = extract_frontmatter(content)
                if frontmatter:
                    data = yaml.safe_load(frontmatter)
                    output_path = os.path.splitext(file_path)[0] + '-frontmatter.json'
                    with open(output_path, 'w') as f:
                        json.dump(data, f, indent=4)