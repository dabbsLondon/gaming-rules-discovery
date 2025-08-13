import hashlib

from python_service.app import harvest


def test_run_returns_empty_for_empty_dir(tmp_path):
    imgs = harvest.run(tmp_path)
    assert imgs == []


def test_run_deduplicates_images(tmp_path):
    img1 = tmp_path / "a.png"
    img1.write_bytes(b"same")
    img2 = tmp_path / "b.png"
    img2.write_bytes(b"same")
    img3 = tmp_path / "c.png"
    img3.write_bytes(b"unique")

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
