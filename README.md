# github-summarizer

Python library to generate SQLite database for versioned WikiPathways data releases.

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
pip install -e .
```

Try it:

```
python ./run.py
```

### Protip
If you ever need to install another dependency, here's an example of how to do it
(in this case for the dependency `SQLAlchemy`):

```
pip install SQLAlchemy
pip freeze > requirements.txt
```
