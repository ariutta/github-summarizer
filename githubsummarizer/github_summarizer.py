#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from github import Github
import io
import os
import pygount
import requests
import tempfile
import zipfile


def main():
    parser = argparse.ArgumentParser(
        description='''Summarize github stats for a user or organization.''')
    parser.add_argument('user',
                        type=str,
                        help='Github user or organization')
    parser.add_argument('--include',
                        type=str,
                        help='''One or more repos to include, separated by commas.
                        Note that --exclude takes priority over --include.
                        ''')
    parser.add_argument('--exclude',
                        type=str,
                        help='''One or more repos to exclude, separated by commas.
                        Note that --exclude takes priority over --include.
                        ''')
    parser.add_argument('-d', '--debug',
                        default=False,
                        type=bool,
                        help='Show debug messages (default = False)')
    args = parser.parse_args()
    # "user" means user or organization
    user = args.user
    include = [] if args.include is None else args.include.split(',')
    exclude = [] if args.exclude is None else args.exclude.split(',')

    g = None
    environ = os.environ
    github_username = None
    if 'GITHUB_USERNAME' in environ:
        github_username = environ['GITHUB_USERNAME']
    github_pwd = None
    if 'GITHUB_PWD' in environ:
        github_pwd = environ['GITHUB_PWD']
    if (github_username is not None) and (github_pwd is not None):
        g = Github(github_username,  github_pwd)
    else:
        g = Github()

    repo_count = 0
    commit_count = 0
    loc_count = 0

    for repo in g.get_user(user).get_repos():
        repo_name = repo.name
        if ((len(exclude) == 0 or repo_name not in exclude) and
                (len(include) == 0 or repo_name in include)):
            repo_count += 1
            print(str(repo_count) + ') analyzing ' + repo_name + '...')
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

    print('Totals')
    print('************************')
    print('repos: ' + str(repo_count))
    print('commits: ' + str(commit_count))
    print('lines (LOC): ' + str(loc_count))

    return {
        'repos': repo_count,
        'commits': commit_count,
        'lines': loc_count,
        }

if __name__ == '__main__':
    main()
