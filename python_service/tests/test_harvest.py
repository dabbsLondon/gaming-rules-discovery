from python_service.app import harvest


def test_run_returns_empty_for_empty_dir(tmp_path):
    imgs = harvest.run(tmp_path)
    assert imgs == []
