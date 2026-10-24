import json, os, unittest
from canonkeeper import core
HERE = os.path.dirname(__file__)
class T(unittest.TestCase):
    def setUp(self):
        self.canon = core.load_canon(os.path.join(HERE, "..", "samples", "canon.json"))
        self.text = open(os.path.join(HERE, "..", "samples", "ch03.md")).read()
    def test_finds_eye_color_and_dead_character(self):
        got = {(f.entity, f.attribute) for f in core.check(self.canon, self.text)}
        self.assertEqual(got, {("Mira", "eyes"), ("Orrin", "status")})
    def test_consistent_facts_pass(self):
        self.assertEqual(core.check(self.canon, "Mira's eyes were grey.\nMira lived in Saltmarsh."), [])
    def test_learn_adds_new_without_overwriting(self):
        n = core.learn(self.canon, self.text, "ch03.md")
        self.assertEqual(self.canon["facts"]["Mira"]["eyes"]["value"], "grey")
        self.assertEqual(self.canon["facts"]["Tavi"]["sister"]["value"], "Wren")
        self.assertGreaterEqual(n, 1)
if __name__ == "__main__": unittest.main()
