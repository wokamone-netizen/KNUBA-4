import unittest
from text_analyzer import (
    find_substring,
    replace_substring,
    split_text,
    format_string_f,
    format_string_method,
    parse_address,
    extract_neurointerfaces,
    extract_emails,
    validate_phone_number,
    count_words,
    count_sentences
)


class TestTextAnalyzer(unittest.TestCase):

    def test_find_substring(self):
        self.assertEqual(find_substring("Hello, world!", "world"), 7)

    def test_replace_substring(self):
        self.assertEqual(
            replace_substring("Hello, world!", "world", "Python"),
            "Hello, Python!"
        )

    def test_split_text(self):
        self.assertEqual(
            split_text("Hello, world!", ", "),
            ["Hello", "world!"]
        )

    def test_format_string_f(self):
        self.assertEqual(
            format_string_f("Alice", 30),
            "Мене звати Alice і мені 30 років."
        )

    def test_format_string_method(self):
        self.assertEqual(
            format_string_method("Bob", 25),
            "Мене звати Bob і мені 25 років."
        )

    # Тести Варіанту 7
    def test_parse_address(self):
        addr = "вул. Перемоги 15, м. Львів, 79000"
        expected = {"street": "вул. Перемоги 15", "city": "Львів", "zip": "79000"}
        self.assertEqual(parse_address(addr), expected)

    def test_extract_neurointerfaces(self):
        text = "Нові моделі NI-X7 та BRAIN-9000 пройшли тестування."
        self.assertEqual(extract_neurointerfaces(text), ["NI-X7", "BRAIN-9000"])

    def test_extract_emails(self):
        text = "Зв'яжіться з нами: info@neoterra.com або support@neo.org"
        self.assertEqual(extract_emails(text), ["info@neoterra.com", "support@neo.org"])

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertFalse(validate_phone_number("12345"))

    def test_count_words(self):
        self.assertEqual(count_words("Це тестове речення для перевірки."), 5)

    def test_count_sentences(self):
        self.assertEqual(count_sentences("Перше речення. Друге! Третє?"), 3)


if __name__ == '__main__':
    from io import StringIO
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTextAnalyzer)
    output = StringIO()
    runner = unittest.TextTestRunner(stream=output, verbosity=2)
    result = runner.run(suite)

    print(output.getvalue())
    print(f"\nУспішних тестів: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Невдалих тестів: {len(result.failures)}")
    print(f"Помилок: {len(result.errors)}")