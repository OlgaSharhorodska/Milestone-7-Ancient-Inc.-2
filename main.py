from flask import Flask, jsonify

app = Flask(__name__)

# Предположим, что у нас есть база данных с информацией о сотрудниках
# и мы можем ее использовать для генерации отчетов

employees = [
    {"id": 1, "name": "John Doe", "birthday": "April 18"},
    {"id": 2, "name": "Patrick Brown", "birthday": "April 10"},
    {"id": 3, "name": "John Wood", "birthday": "April 11"},
    {"id": 4, "name": "Helen King", "birthday": "April 30"}
]

@app.route('/api/report/<month>/<department>', methods=['GET'])
def generate_report(month, department):
    # Здесь мы могли бы выполнить запрос к базе данных для получения информации о сотрудниках
    # в указанном месяце и отделе, но для простоты просто возвращаем фиктивные данные
    filtered_employees = [employee for employee in employees if employee["birthday"].split()[0].lower() == month.lower()]
    return jsonify({
        "total": len(filtered_employees),
        "employees": filtered_employees
    })

if __name__ == '__main__':
    app.run(debug=True)
