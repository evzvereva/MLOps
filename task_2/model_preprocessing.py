import pandas as pd
from sklearn.preprocessing import StandardScaler


def get_standardscaler(path_file):
    """
    Функция позволяет произвести стандартизацию данных за исключением целевой переменной
    :param file_path:
    :return result_df:
    """
    df = pd.read_csv(path_file, sep=',', encoding='utf-8')

    X = df.drop(columns=['id', 'status'])  # в признаках нам не нужен 'status'и 'id'
    y = df['status']

    scaler = StandardScaler() # инициализируем
    X_scaled = scaler.fit_transform(X) # преобразуем

    result_df = pd.DataFrame(X_scaled, columns=X.columns) # оборачиваем в датафрейм
    # добавляем целевую переменную и id пациента
    result_df['status'] = y
    result_df['id'] = df['id']
    return result_df
