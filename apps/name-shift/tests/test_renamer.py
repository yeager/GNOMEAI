from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1]))
import renamer

def test_preview_preserves_extensions_and_changes_stem(tmp_path):
    path = tmp_path / 'holiday.photo.jpg'; path.touch()
    item = renamer.preview([path], 'holiday', 'trip', '2026-', '-edited')[0]
    assert item.target.name == '2026-trip.photo-edited.jpg'
    assert item.error is None

def test_preview_rejects_duplicate_targets(tmp_path):
    first = tmp_path / 'ab.txt'; second = tmp_path / 'ba.txt'; first.touch(); second.touch()
    plans = renamer.preview([first, second], 'a', '')
    assert all(plan.error == 'Two selected files would use this name' for plan in plans)

def test_preview_rejects_existing_target(tmp_path):
    source = tmp_path / 'draft.txt'; target = tmp_path / 'final.txt'; source.touch(); target.touch()
    plan = renamer.preview([source], 'draft', 'final')[0]
    assert plan.error == 'A file with this name already exists'

def test_apply_renames_only_valid_preview(tmp_path):
    source = tmp_path / 'draft.txt'; source.touch()
    plans = renamer.preview([source], prefix='done-')
    assert renamer.apply(plans) == [tmp_path / 'done-draft.txt']
    assert (tmp_path / 'done-draft.txt').exists()
