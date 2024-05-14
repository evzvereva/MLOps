from model_preprocessing import get_standardscaler
import pickle
from sklearn.metrics import accuracy_score, classification_report


def get_model_load():
    with open('model_pickle.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


model = get_model_load()
df = get_standardscaler('test/test.csv')
# отделяем целевую переменную от остальных данных
X = df.drop(columns=['id', 'status'])  # в признаках нам не нужен 'status'и 'id'
y = df['status']

y_pred = model.predict(X)

# Вычисление метрик
print("Accuracy:", accuracy_score(y, y_pred))
print("Classification Report:\n", classification_report(y, y_pred))

with open('predict_data.csv', 'w') as f:
    f.write(str(y_pred))
