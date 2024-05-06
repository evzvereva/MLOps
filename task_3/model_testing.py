import model_testing as st
import pandas as pd
from model_preprocessing import get_standardscaler
import pickle
from sklearn.metrics import accuracy_score, classification_report


def get_model_load():
    with open('model_pickle.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


model = get_model_load()


def load_image():
    """
    Функция load_image() позволяет загрузить пользователю файл csv и провести прогноз статуса пациента.
    """
    st.header("Прогноз статуса пациента")
    uploaded_file = st.file_uploader(label="Выберите файл .csv для прогноза")
    if uploaded_file:
        df = get_standardscaler(uploaded_file)

        # отделяем целевую переменную от остальных данных
        X = df.drop(columns=['id', 'status'])  # в признаках нам не нужен 'status' и 'id'
        y = df['status']

        y_pred = model.predict(X)

        # Вычисление метрик
        accuracy = accuracy_score(y, y_pred)
        report = classification_report(y, y_pred, output_dict=True)

        # Преобразование отчета классификации в DataFrame
        report_df = pd.DataFrame(report).transpose()

        # Отображение отчета классификации в виде таблицы
        st.write("Classification Report:")
        st.table(report_df)

        # Отображение метрики точности
        st.write(f"Accuracy: {accuracy}")

        # Добавим id пациента и status, который получили согласно прогнозу
        X['id'] = df['id']
        X['status'] = y_pred

        st.write("Результат прогноза, 1 - выжил, 0 - не выжил: ")
        return st.table(X)


load_image()
