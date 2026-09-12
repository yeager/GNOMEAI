import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from checker import check
def test_finds_unknown_word(): assert 'mispellled' in check('A mispellled word.', 'en_US')
def test_accepts_common_words(): assert check('A simple sentence.', 'en_US') == []
