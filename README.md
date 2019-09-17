## Development

*Build*

```bash
pipenv install -r requirements.txt
pipenv install pip setuptools wheel tqdm twine
pipenv run python setup.py sdist bdist_wheel
```

*Install*

```bash
pipenv run pip install dist/wk_issue_train-0.0.2-py3-none-any.whl
pipenv run pip uninstall -y dist/wk_issue_train-0.0.2-py3-none-any.whl
```

*Load issues*

```bash
pipenv run wk-load-issue <token> <user/repository> <output-dir>
pipenv run wk-load-issue $GITHUB_TOKEN  bcircle/easy-capture issues
```

*Train*

```bash
pipenv run wk-train-model <issue-dir>
pipenv run wk-train-model issues
```