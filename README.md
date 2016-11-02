# github-summarizer

Python library to get summary github stats for a user or organization.

Get library:

```
git clone https://github.com/ariutta/github-summarizer.git
cd github-summarizer
```

Isolate environment (optional):

```
workon github-summarizer
```

Install dependencies (not sure whether this is working yet -- if not, install what's in requirements.txt):

```
pip3 install -e .
```

View options:
```
githubsummarizer/github_summarizer.py --help
```

Try it:

```
githubsummarizer/github_summarizer.py wikipathways --include pvjs
```

### Protip
If you ever need to install another dependency, here's an example of how to do it
(in this case for the dependency `SQLAlchemy`):

```
pip3 install SQLAlchemy
pip3 freeze > requirements.txt
```
