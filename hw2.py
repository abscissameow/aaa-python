import csv
from typing import List, Dict

def read_csv(filename: str) -> List[Dict[str, str]]:
    """
    эта функция читает csv файлики и удобно записывает
    """
    with open(filename, 'r') as f:
        return list(csv.DictReader(f, delimiter=';'))


def write_csv(filename: str, data: List[Dict[str, str]]) -> None:
    """
    эта функция сохранит твои данные в csv файл
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def get_departments(data: List[Dict[str, str]]) -> Dict[str, set]:
    """
    эта функция группирует данные по департаментам и отделам внутри департамента. она возвращает словарь, 
    где ключи - названия департаментов, а значения - команды
    """
    departments = {}
    for row in data:
        if row['Департамент'] not in departments:
            departments[row['Департамент']] = set()
        departments[row['Департамент']].add(row['Отдел'])
        
    return departments


def calculate_stats(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    эта функция считает всякую информацию по департаментам
    """
    departments = get_departments(data)
    stats = []
    for department, teams in departments.items():
        salaries = [int(row['Оклад']) for row in data if row['Департамент'] == department]
        stats.append({
            'Департамент': department,
            'Численность': len(salaries),
            'Вилка зарплат': f"{min(salaries)} - {max(salaries)}",
            'Средняя зарплата': round(sum(salaries) / len(salaries))
        })
    return stats

def choice():
    """
    основная функция! тут описано, что делать при выборе пользователя
    """
    data = read_csv('/Users/l.bril/Desktop/avito/Corp_Summary.csv')

    while True:
        print('1. иерархия команд')
        print('2. отчёт по департаментам')
        print('3. сохранить отчёт')

        choice = input('выбери действие: ')

        if choice == '1':
            departments = get_departments(data)
            for department, teams in departments.items():
                print(f'{department}: {", ".join(set(teams))}')
            break
        elif choice == '2':
            stats = calculate_stats(data)
            for department in stats:
                print(department)
            break
        elif choice == '3':
            stats = calculate_stats(data)
            write_csv('report.csv', stats)
            print("отчёт сохранён!")
            break
        else:
            print('вы ввели какую-то фигню. введите чиселку от 1 до 3, пожалуйста')

if __name__ == "__main__":
    choice()

