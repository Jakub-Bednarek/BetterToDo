import platform


def task_run_app():
    return {"actions": ["python3 src/main.py"]}


def task_pytest():
    if platform.system() == "Windows":
        current_dir_cmd = "%cd%"
    else:
        current_dir_cmd = "$(pwd)"

    return {"actions": [f"PYTHONPATH={current_dir_cmd}/src pytest"], "verbosity": 2}


def task_format_code():
    return {"actions": ["black ."]}


def task_mypy():
    return {"actions": ["mypy ."]}


def task_flake8():
    return {"actions": ["flake8"]}
