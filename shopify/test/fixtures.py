import pytest

@pytest.fixture
def create_admin_user(django_user_model):
    return django_user_model.objects.create_superuser("admin", "sp@uw.ca", 'pw')
