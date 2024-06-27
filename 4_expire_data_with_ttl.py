"""
Для очистки данных из MongoDB по истечению заданного времени
мы можем воспользоваться функцией TTL (Time To Live)
"""

from datetime import datetime, timedelta, timezone

from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["your_database"]
collection = db["your_collection"]

# Создание TTL индекса
collection.create_index("expireAt", expireAfterSeconds=0)


def insert_document(data):
    # Добавляем поле expireAt со значением через 24 часа
    data["expireAt"] = datetime.now(timezone.utc) + timedelta(hours=24)
    collection.insert_one(data)


def update_document(document_id, data):
    # Обновляем документ и устанавливаем новое время удаления
    data["expireAt"] = datetime.now(timezone.utc) + timedelta(hours=24)
    collection.update_one({"_id": document_id}, {"$set": data})


# Пример использования
sample_data = {"name": "Example", "value": 42}
insert_document(sample_data)

# Обновление документа (если нужно)
# update_document(document_id, {"value": 43})
