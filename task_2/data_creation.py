import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Создание папок для сохранения данных, если они еще не существуют
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')


def get_random_date(low_val, high_val, round_val):
    """
      Функция позволяет создать случайный набор данных для дальнейшего сбора в датафрейм.
      :param low_val:
      :param high_val:
      :param round_val:
      :return result:
      """
    result = np.round(np.random.uniform(low=low_val, high=high_val, size=(3000, 1)), round_val)
    return result


id = get_random_date(1, 3000, 0).astype(int)  # id пациента
age = get_random_date(18, 122, 0).astype(int)  # возраст
temperature = get_random_date(23, 41, 1)  # температура
pulse = get_random_date(11, 180, 0).astype(int)  # пульс
pressure = get_random_date(40, 240, 2)  # давление

# объединение данных в датафрейм
df = pd.DataFrame({
    'id': id.flatten(),
    'age': age.flatten(),
    'temperature': temperature.flatten(),
    'pulse': pulse.flatten(),
    'pressure': pressure.flatten()
})

# запишем данные, в результате которых вероятность летальности высока
min_pulse = 0.64 * df['age']  # min пульс при котором умирает пациент
max_pulse = 211 - (0.64 * df['age'])  # мах пульс при котором умирает пациент

min_temperature = 25  # min температура при котором умирает пациент
max_temperature = 41  # мах температура при котором умирает пациент

min_pressure = 40  # min давление при котором умирает пациент
max_pressure = 220  # мах давление при котором умирает пациент

# добавление столбца, где значения 0 - выжил, 1 - не выжил на основании условий
df['status'] = np.where(
    (df['pulse'] <= min_pulse) | (df['pulse'] >= max_pulse) |
    (df['temperature'] <= min_temperature) | (df['temperature'] >= max_temperature) |
    (df['pressure'] <= min_pressure) | (df['pressure'] >= max_pressure)
    , 1, 0)

# добавим шумы в столбец с температурой
df['temperature'] = np.where((df['temperature'] < 35) & (df['temperature'] > 30), df['temperature'] - 20,
                             df['temperature'])

# добавим шумы в столбец с давлением
df['pressure'] = np.where((df['pressure'] < 45) & (df['pressure'] > 42), df['pressure'] - 30, df['pressure'])

# разделим данные на тестовую и обучающую выборку, сохраним в файлы и поместим в соответствующие директории
train, test = train_test_split(df, test_size=0.3, random_state=42)
train.to_csv('train/train.csv', index=False)
test.to_csv('test/test.csv', index=False)
