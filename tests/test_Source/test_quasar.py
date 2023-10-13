from astropy.cosmology import FlatLambdaCDM
from astropy.units import Quantity
from slsim.Sources.quasars import Quasars
from slsim.Sources.quasar_catalog.simple_quasar import quasar_catalog
import pytest


@pytest.fixture
def Quasar_class():
    sky_area = Quantity(value=0.1, unit="deg2")
    kwargs_quasars = {
        "number": 50000,
        "z_min": 0.1,
        "z_max": 5,
        "m_min": 17,
        "m_max": 25,
    }
    quasar_list = quasar_catalog(**kwargs_quasars)
    cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
    return Quasars(quasar_list=quasar_list, cosmo=cosmo, sky_area=sky_area)


def test_source_number(Quasar_class):
    number = Quasar_class.source_number()
    assert number > 0


def test_draw_source(Quasar_class):
    quasar = Quasar_class.draw_source()
    assert len(quasar) > 0


if __name__ == "__main__":
    pytest.main()
