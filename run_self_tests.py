from num_series import simple_moving_average, mean, median, random_series

def run_tests():
    print("Запуск ручных тестов...")
    assert simple_moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0], "ошибка в SMA"
    assert mean([2, 4, 6]) == 4.0, "ошибка в среднем"
    assert median([1, 3, 2]) == 2.0, "ошибка в медиане"
    data = random_series(5, seed=42)
    assert len(data) == 5, "ошибка в длине сгенерированного ряда"
    print("все базовые тесты пройдены успешно!")

if __name__ == "__main__":
    run_tests()

