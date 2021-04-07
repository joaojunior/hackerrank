flake8 .
isort --check-only --diff .
radon cc . -a -s -na
