import project.frontend

from unittest import mock


def test_a_method(monkeypatch):
    fake_get_area = mock.Mock(return_value=2.0)

    monkeypatch.setattr(
        project.frontend.services.utils.Calculations, "get_area", fake_get_area
    )

    res = project.frontend.a_method()

    assert res == 2.0
