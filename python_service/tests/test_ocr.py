import pytest
from python_service.app import ocr_service


def test_extract_text_raises():
    with pytest.raises(NotImplementedError):
        ocr_service.extract_text("dummy.png")
