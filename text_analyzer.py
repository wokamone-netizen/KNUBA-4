import re
from collections import Counter


def find_substring(text: str, substring: str) -> int:
    return text.find(substring)


def replace_substring(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def split_text(text: str, delimiter: str = ' ') -> list:
    return text.split(delimiter)


def format_string_f(name: str, age: int) -> str:
    return f"Мене звати {name} і мені {age} років."


def format_string_method(name: str, age: int) -> str:
    return "Мене звати {} і мені {} років.".format(name, age)


def parse_address(address_str: str) -> dict:
    pattern = r'^(?P<street>.+?),\s*м\.\s*(?P<city>[^,]+),\s*(?P<zip>\d{5})$'
    match = re.search(pattern, address_str.strip())
    if match:
        return match.groupdict()
    return {"street": "Не визначено", "city": "Не визначено", "zip": "Не визначено"}


def extract_neurointerfaces(text: str) -> list:
    pattern = r'\b[A-Z]{2,}[A-Za-z0-9]*-[A-Z0-9]+\b'
    return re.findall(pattern, text)


def extract_emails(text: str) -> list:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)


def validate_phone_number(number: str) -> bool:
    pattern = r'^\+?3?8?(0\d{9})$'
    return bool(re.match(pattern, number))


def count_words(text: str) -> int:
    return len(re.findall(r'\b\w+\b', text))


def count_sentences(text: str) -> int:
    return len(re.findall(r'[.!?]+', text))


def word_frequency(text: str) -> Counter:
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


def analyze_text(text: str) -> dict:
    word_cnt = count_words(text)
    sentence_cnt = count_sentences(text)
    freq = word_frequency(text)
    emails = extract_emails(text)
    neurointerfaces = extract_neurointerfaces(text)

    return {
        'word_count': word_cnt,
        'sentence_count': sentence_cnt,
        'word_frequency': freq.most_common(5),
        'emails': emails,
        'neurointerfaces': neurointerfaces
    }


def format_analysis_results(results: dict) -> str:
    output = "Результати аналізу тексту:\n\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n\n"
    
    output += "Топ-5 найчастіших слів:\n"
    for word, count in results['word_frequency']:
        output += f"  {word}: {count}\n"
        
    output += f"\nЗнайдені email адреси: {', '.join(results['emails']) if results['emails'] else 'Не знайдено'}\n"
    output += f"Знайдені нейроінтерфейси: {', '.join(results['neurointerfaces']) if results['neurointerfaces'] else 'Не знайдено'}\n"
    
    return output


def main():
    print("Ласкаво просимо до аналізатора тексту (Варіант 7)!")
    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту")
            print("2. Валідація телефону")
            print("3. Парсинг адреси")
            print("4. Вихід")
            choice = input("Ваш вибір: ").strip()

            if choice == '1':
                text = input("\nВведіть текст для аналізу: ")
                results = analyze_text(text)
                print("\n" + format_analysis_results(results))
            elif choice == '2':
                phone = input("\nВведіть номер телефону для валідації: ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")
            elif choice == '3':
                addr = input("\nВведіть адресу (наприклад, 'вул. Шевченка 10, м. Київ, 01001'): ")
                parsed = parse_address(addr)
                print(f"Результат розбору: Вулиця: {parsed['street']}, Місто: {parsed['city']}, Індекс: {parsed['zip']}")
            elif choice == '4':
                print("Дякуємо за використання аналізатора!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")
        except Exception as e:
            print(f"Виникла помилка: {e}")


if __name__ == '__main__':
    main()