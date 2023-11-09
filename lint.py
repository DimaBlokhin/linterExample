import os
import sys
from pylint.lint import Run

def run_linter():
    # Измените путь до вашего проекта, если это необходимо
    project_path = "путь_до_вашего_проекта"
    
    # Опции для запуска pylint, можно настроить под свои нужды
    options = [
        f"--rcfile={project_path}/.pylintrc",
        "--output-format=parseable",
        f"{project_path}/your_python_code_directory"  # Путь до вашего кода
    ]

    results = Run(options, exit=False)
    score = results.linter.stats['global_note']
    return score

if __name__ == "__main__":
    score = run_linter()
    sys.exit(int(score < 9))  # Выберите пороговый балл для прохождения линтера
