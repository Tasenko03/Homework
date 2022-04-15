"""Задача 1 (3 балла). Определите и вызовите функцию stats_from_file(). Данная функция принимает в качестве аргумента
имя файла, из которого необходимо считать данные. Данные представляют собой числа, каждое из которых записано на
новой строке. Функция stats_from_file возвращает минимальное число из этого файла, максимальное число, а также сумму
всех чисел, которые записаны в файле."""


def stats_from_file(file):
    with open(file, encoding="utf-8") as f:
        text = f.read()
        print("Содержимое файла some_numbers:")
        print(text, "\n")
        text1 = text.split("\n")
        result = [int(item) for item in text1]
        smallest = min(result)
        biggest = max(result)
        sum = 0
        for i in result:
          sum += i
        print(smallest, biggest, sum, sep=", ")
        return smallest, biggest, sum


stats_from_file('some_numbers.txt')
