from github import Github
import io
import pygount
import requests
import tempfile
import zipfile

g = Github()

repo_count = 0
commit_count = 0
loc_count = 0

user = 'wikipathways'

for repo in g.get_user(user).get_repos():
    print(str(repo_count) + ') analyzing ' + repo.name + '...')
    repo_count += 1
    for commit in repo.get_commits():
        commit_count += 1

    url_vars = {'user': user, 'repo': repo.name}
    url = 'https://github.com/{user}/{repo}/archive/master.zip'.format(
        **url_vars)

    r = requests.get(url, stream=True)
    if r.ok:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        with tempfile.TemporaryDirectory() as tmpdirname:
            z.extractall(tmpdirname)
            scanner = pygount.analysis.SourceScanner([tmpdirname])
            source_paths = list(scanner.source_paths())
            for source_path in source_paths:
                analysis = pygount.source_analysis(
                    source_path[0], repo.name)
                loc_count += analysis[3]

print('repo count: ' + str(repo_count))
print('commit count: ' + str(commit_count))
print('LOC count: ' + str(loc_count))
