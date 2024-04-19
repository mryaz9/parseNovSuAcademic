import pandas as pd
from bs4 import BeautifulSoup

# Чтение HTML-файла
with open('file.html', 'r', encoding="utf-8'") as file:
    html_content = file.read()

# Парсинг HTML-файла с помощью BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение данных из таблицы
data = []
for row in soup.find_all('tr')[1:]:
    columns = row.find_all('td')
    row_data = [
        columns[0].text.strip(),  # Семестр
        columns[1].text.strip(),  # Название предмета
        columns[5].text.strip(),  # Оценка на 18 неделе
    ]
    data.append(row_data)

# Создание DataFrame и запись в Excel-файл
df = pd.DataFrame(data, columns=['Семестр', 'Название предмета', 'Оценка на 18 неделе'])
df.to_excel('output.xlsx', index=False)
print('Данные успешно записаны в output.xlsx')