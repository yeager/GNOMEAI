import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from model import parse_list
def test_parse_list():
 assert parse_list('org.demo.App\tDemo\n')[0].app_id == 'org.demo.App'
def test_skips_empty_rows():
 assert parse_list('\n') == []
