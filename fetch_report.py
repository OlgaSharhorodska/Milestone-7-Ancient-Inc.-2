import requests
import sys

def fetch_report(month, department):
    url = f'http://localhost:5000/api/report/{month}/{department}'
    response = requests.get(url)
    if response.status_code == 200:
        report = response.json()
        print(f'Отчет за {month} {department} получен:')
        print(f'Всего: {report["total"]}')
        print('Сотрудники:')
        for employee in report["employees"]:
            print(f'- {employee["birthday"]}, {employee["name"]}')
    else:
        print('Ошибка при получении отчета')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Использование: python fetch_report.py <месяц> <отдел>')
        sys.exit(1)
    month = sys.argv[1]
    department = sys.argv[2]
    fetch_report(month, department)
