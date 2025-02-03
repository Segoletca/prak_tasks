- Установил flake8, посмотрел как он работает
- Установил расширения для flake8 (pep8-naming, flake8-return, flake8-isort)


```bash
-> % flake8 *.py
annotations.py:1:36: W291 trailing whitespace
```

### Аннотация типов
- Установил mypy `pip install mypy`

```bash
-> % mypy annotations.py
annotations.py:5: error: Argument 1 to "we_crash_all" has incompatible type "int"; expected "str"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

- Включил подсветку mypy в ide
- Не до конца понял как лучше перенести строку в задаче 1 (уже разобрался)

- Правила использования комментариев в файле `комментарии.py`
- Задание по код-стайлу `code_style.py`
