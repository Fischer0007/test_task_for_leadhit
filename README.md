 <h1 align="center">Test task for LeadHit</h1>
 
 ## Requirements

- [Pip == 22.3.1](https://pypi.org/project/pip/)
- [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)

 ## Local development in Ubuntu v.20.04
 
Clone the project to the directory we need:

```shell
git clone https://github.com/Fischer0007/test_task_for_leadhit.git
```

Go to  test_task_for_leadhit:

```shell
cd test_task_for_leadhit
```

Installing requerements for python:

```shell
pip install -r req.txt
```

Run Flask app:

```shell
export FLASK_APP=app
export FLASK_DEBUG=True
flask run
```

Run tests for the app with full report and app coverage report:

```shell
python3 -m pytest tests/
```
