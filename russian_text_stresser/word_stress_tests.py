import unittest
from russian_dictionary import RussianDictionary
from text_stresser import RussianTextStresser


class StressTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rd = RussianDictionary("russian_dict.db")
        self.stresser = RussianTextStresser()

    def test_simple_case(self):
        self.assertEqual(self.rd.get_stressed_word_and_set_yo("тупо"), "ту́по")

    def test_uppercase_simple_case(self):
        self.assertEqual(self.rd.get_stressed_word_and_set_yo(
            "Огромный"), "Огро́мный")

    def test_ambiguous_case(self):
        self.assertEqual(
            self.rd.get_stressed_word_and_set_yo("головы"), "головы")

    def test_upper_ambiguous_case(self):
        self.assertEqual(
            self.rd.get_stressed_word_and_set_yo("Потом"), "Потом")

    def test_yo(self):
        self.assertEqual(self.rd.get_stressed_word_and_set_yo("еж"), "ёж")

    def test_ambiguous_yo_case(self):
        self.assertEqual(
            self.rd.get_stressed_word_and_set_yo("копье"), "копье")

    def test_uppercase_yo(self):
        self.assertEqual(
            self.rd.get_stressed_word_and_set_yo("Зеленый"), "Зелёный")

    def test_uppercase_ambiguous_yo_case(self):
        self.assertEqual(
            self.rd.get_stressed_word_and_set_yo("Копье"), "Копье")

    def test_genitive(self):
        self.assertEqual(
            self.stresser.stress_text("Лица сияют."), "Ли́ца сия́ют.")
    
    # Test "Э́то шу́тер от первого лица́.""
    def test_sentence_plural(self):
        self.assertEqual(
            self.stresser.stress_text("Это шутер от первого лица."), "Э́то шу́тер от первого лица́.")

    def test_sentence_one_syllable(self):
        self.assertEqual(
            self.stresser.stress_text("Эти красивые леса!"), "Э́ти краси́вые леса́!")
        
    def test_sentence_genitive(self):
        self.assertEqual(
            self.stresser.stress_text("Это магия этого леса."), "Э́то ма́гия э́того ле́са.")


if __name__ == '__main__':
    unittest.main()
