import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "store.py"
spec = importlib.util.spec_from_file_location("store", MODULE)
store = importlib.util.module_from_spec(spec)
spec.loader.exec_module(store)


class StoreTests(unittest.TestCase):
    def test_save_deduplicates_and_keeps_newest_items(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "items.json"
            saved = store.save(["one", "two", "one", ""], path)
            self.assertEqual(saved, ["one", "two"])
            self.assertEqual(store.load(path), ["one", "two"])

    def test_prepend_moves_item_to_front(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "items.json"
            self.assertEqual(store.prepend("two", ["one", "two"]), ["two", "one"])
            self.assertEqual(store.save([str(index) for index in range(110)], path),
                             [str(index) for index in range(100)])


if __name__ == "__main__":
    unittest.main()
