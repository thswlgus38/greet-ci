# greet-ci

인사말 프로그램 및 GitHub Actions CI 구성 실습

## 실행 방법

```bash
uv run --locked python greet.py Hee
uv run --locked python greet.py

## 검사 방법

```bash
uv run --locked pytest -q greet.py
uv run --locked black --check greet.py
uv run --locked flake8 greet.py
uv run --locked mypy greet.py
uv build
