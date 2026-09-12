import importlib.util
import tempfile
import unittest
from pathlib import Path

source = Path(__file__).parents[1] / 'store.py'
spec = importlib.util.spec_from_file_location('store', source)
store = importlib.util.module_from_spec(spec)
spec.loader.exec_module(store)


class StoreTests(unittest.TestCase):
    def test_save_filters_empty_and_duplicate_items(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'items.json'
            items = store.save([
                {'name': 'Status', 'command': 'git status'},
                {'name': 'Status', 'command': 'git status'},
                {'name': '', 'command': 'ignored'},
            ], path)
            self.assertEqual(items, [{'name': 'Status', 'command': 'git status'}])
            self.assertEqual(store.load(path), items)


if __name__ == '__main__':
    unittest.main()
