import pickle

from model_preprocessing import get_standardscaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# получение датафрейма
result_df = get_standardscaler('train/train.csv')

X = result_df.drop(columns=['id', 'status'])  # в признаках нам не нужен 'status'и 'id'
y = result_df['status']

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание экземпляра LogisticRegression
model = RandomForestClassifier(random_state=16)

# Обучение модели на обучающей выборке
model.fit(X_train, y_train)

# Предсказание на тестовой выборке
y_pred = model.predict(X_test)

# Вычисление метрик
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# сохранение модели
pickle.dump(model, open('model_pickle.pkl', 'wb'))
