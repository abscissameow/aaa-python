## мяу? :pig:

в папочке [testing](https://github.com/abscissameow/omd/tree/abscissameow-testing/testing) лежат файлы `test1.py`, `test2.py`, `test3.py`, `test4.py`, `test5.py` – в этих файлах функции и тесты (для пятого теста функция импортируется из `what_is_year_now.py`, но я её немного поправила, добавив `# pragma: no cover`)

прикрепила результаты запусков в соответствующих файлах, полученные как-то так: `python -m pytest -v testN.py > resultN` (pytest/doctest/unittest)

в папочку [html report](https://github.com/abscissameow/omd/tree/abscissameow-testing/testing/html%20report) положила все файлы, которые образовались по команде `python3 -m pytest -q  --cov=what_is_year_now --cov-report html test5.py` – можем посмотреть, что покрытие 100%

<img src="/testing/html%20report/coverage.png" width="500" height="75"/> 
