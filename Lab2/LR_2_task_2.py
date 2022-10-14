from sklearn.datasets import load_iris
iris_dataset = load_iris()

print(f"Ключі iris_dataset: \n{iris_dataset.keys()}")
print(iris_dataset['DESCR'][:193] + "\n...")
print(f"Назви відповідей: {iris_dataset['target_names']}")
print(f"Назви ознак: {iris_dataset['feature_names']}")
print(f"Тип масиву data: {type(iris_dataset['data'])}")
print(f"Форма масиву data: {iris_dataset['data'].shape}")
print(f"Перші 5 рядків ознак: \n{iris_dataset['data'][:5]}")

print(f"Тип масиву відповідей: {type(iris_dataset['target'])}")
print(f"Форма масиву відповідей: {iris_dataset['target'].shape}")
print(f"Відповіді: {iris_dataset['target']}")

