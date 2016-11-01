# github-summarizer

Python library to get summary github stats for a single user or organization.

Get library:

```
git clone https://github.com/ariutta/github-summarizer.git
cd github-summarizer
```

Isolate environment (optional):

```
workon github-summarizer
```

Install dependencies:

```
pip3 install -e .
```

Try it:

```
python3 ./run.py
```

### Protip
If you ever need to install another dependency, here's an example of how to do it
(in this case for the dependency `SQLAlchemy`):

```
pip3 install SQLAlchemy
pip3 freeze > requirements.txt
```
