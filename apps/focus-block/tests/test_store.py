import importlib.util
import tempfile
import unittest
from pathlib import Path

source = Path(__file__).parents[1] / 'store.py'
spec = importlib.util.spec_from_file_location('store', source)
store = importlib.util.module_from_spec(spec)
spec.loader.exec_module(store)


class StoreTests(unittest.TestCase):
    def test_load_defaults_for_missing_file(self):
        self.assertEqual(store.load(Path('/nonexistent/focus-block.json')), store.DEFAULT)

    def test_save_filters_invalid_values(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'settings.json'
            self.assertEqual(store.save({'focus_minutes': 50, 'break_minutes': 0}, path),
                             {'focus_minutes': 50, 'break_minutes': 5})
            self.assertEqual(store.load(path), {'focus_minutes': 50, 'break_minutes': 5})


if __name__ == '__main__':
    unittest.main()
