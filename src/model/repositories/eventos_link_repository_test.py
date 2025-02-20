import pytest
from .eventos_link_repository import EventosLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_event_link():
    event_id = 12
    sub_id = 8
    event_link_repo = EventosLinkRepository()
    
    event_link_repo.insert(event_id, sub_id)
    
