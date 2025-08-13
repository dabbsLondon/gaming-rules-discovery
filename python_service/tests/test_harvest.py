import hashlib

from pathlib import Path

from python_service.app import harvest


def test_run_returns_empty_for_empty_dir(tmp_path):
    imgs = harvest.run(tmp_path)
    assert imgs == []


def test_run_deduplicates_images(tmp_path, monkeypatch):
    img1 = tmp_path / "a.png"
    img1.write_bytes(b"same")
    img2 = tmp_path / "b.png"
    img2.write_bytes(b"same")
    img3 = tmp_path / "c.png"
    img3.write_bytes(b"unique")

    # stub out OCR so tests don't depend on an external engine
    def fake_ocr(path):
        name = Path(path).name
        if name == "c.png":
            return "Legion rules for the XVI Legion"
        return f"text from {name}"

    monkeypatch.setattr(harvest.ocr_service, "extract_text", fake_ocr)

    imgs = harvest.run(tmp_path)

    assert len(imgs) == 2
    paths = {img.path for img in imgs}
    assert str(img3) in paths
    assert (str(img1) in paths) ^ (str(img2) in paths)

    expected_digests = {
        hashlib.md5(b"same").hexdigest(),
        hashlib.md5(b"unique").hexdigest(),
    }
    assert {img.digest for img in imgs} == expected_digests

    img_map = {img.path: img for img in imgs}
    assert img_map[str(img3)].is_legion_rule is True
    assert img_map[str(img3)].text == "Legion rules for the XVI Legion"
    for path, img in img_map.items():
        if path != str(img3):
            assert img.is_legion_rule is False


def test_run_skips_non_image_files(tmp_path, monkeypatch):
    txt = tmp_path / "note.txt"
    txt.write_text("not an image")

    def fake_ocr(_):
        raise AssertionError("OCR should not run on non-images")

    monkeypatch.setattr(harvest.ocr_service, "extract_text", fake_ocr)

    imgs = harvest.run(tmp_path)

    assert imgs == []
