import unittest
from pathlib import Path


class GymLingoHtmlRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = Path('GymLingo.html').read_text(encoding='utf-8')

    def test_row_transliteration_typo_fixed(self):
        self.assertIn('Бэнт оувер барбэл роу', self.html)
        self.assertIn('Ситид кэйбл роу', self.html)
        self.assertNotIn('роув', self.html)

    def test_trainer_completion_state_keeps_original_card_nodes(self):
        self.assertNotIn("document.getElementById('flashcard').innerHTML", self.html)
        self.assertIn('id="completionState"', self.html)
        self.assertIn("completionState.classList.remove('hidden')", self.html)

    def test_completion_state_resets_controls_safely(self):
        self.assertIn("if (state.activeCards.length === 0) return;", self.html)
        self.assertIn("document.getElementById('currentCardNum').textContent = 0;", self.html)
        self.assertIn("document.getElementById('progressBar').style.width = '100%';", self.html)


if __name__ == '__main__':
    unittest.main()
