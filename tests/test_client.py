import pytest

from vibermsg import ViberClient


class TestMessengerClient:
    def test_init(self):
        with pytest.raises(TypeError):
            ViberClient(123)
        try:
            ViberClient('asda')
        except Exception as e:
            assert str(e) == 'failed with status: 2, message: invalidAuthToken'
