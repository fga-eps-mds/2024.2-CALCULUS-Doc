import json
import requests
import sys
from datetime import datetime
from dotenv import load_dotenv

import os
import requests
from packaging import version

load_dotenv()

# Variáveis globais ao repositório
OWNER = "fga-eps-mds"
REPO = os.getenv('REPO')
TODAY = datetime.now()

# Configurar as variáveis de ambiente
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
RELEASE_MAJOR = os.getenv('RELEASE_MAJOR')
RELEASE_MINOR = os.getenv('RELEASE_MINOR')
RELEASE_FIX = os.getenv('RELEASE_FIX')
DEVELOP = os.getenv('DEVELOP')

# Configurar as variáveis do sonar
METRICS_SONAR = [
    'files',
    'functions',
    'complexity',
    'comment_lines_density',
    'duplicated_lines_density',
    'coverage',
    'ncloc',
    'tests',
    'test_errors',
    'test_failures',
    'test_execution_time',
    'security_rating'
]

BASE_URL = 'https://sonarcloud.io/api/measures/component_tree?component=fga-eps-mds_'

# Pega a última release
def get_latest_release():
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/releases'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    releases = response.json()
    
    if releases:
        return releases[0].get('tag_name', '0.0.0')
    return '0.0.0'

# Cria um novo nome de tag
def new_tag_name():
    old_tag = get_latest_release()
    try:
        old_version = version.parse(old_tag)
    except version.InvalidVersion:
        old_version = version.parse('0.0.0')

    if RELEASE_MAJOR == 'true':
        return f'{old_version.major + 1}.0.0'
    elif RELEASE_MINOR == 'true':
        return f'{old_version.major}.{old_version.minor + 1}.0'
    elif RELEASE_FIX == 'true':
        return f'{old_version.major}.{old_version.minor}.{old_version.micro + 1}'
    else:
        return f'{old_version.major}.{old_version.minor}.{old_version.micro + 1}'

# Cria a nova release
def create_release():
    tag = new_tag_name()
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/releases'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'tag_name': tag,
        'name': tag
    }
    response = requests.post(url, headers=headers, json=payload)
    res_data = response.json()
    return res_data.get('upload_url'), tag

if __name__ == '__main__':
    _, tag = create_release()

    response = requests.get(f'{BASE_URL}{REPO}&metricKeys={",".join(METRICS_SONAR)}&ps=500')
    j = json.loads(response.text)

    file_path = f'./analytics-raw-data/fga-eps-mds-{REPO}-{TODAY.strftime("%m-%d-%Y-%H-%M-%S")}-{tag}.json'

    with open(file_path, 'w') as fp:
        fp.write(json.dumps(j))
        fp.close()