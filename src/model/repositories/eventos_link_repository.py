import random
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos_link import EventosLink
from .interfaces.eventos_link_repository import EventosLinkRepositoryInterface


class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, event_id: int, sub_id: int) -> None:
        with DBConnectionHandler() as db:
            try:
                final_link = "".join(random.choices("0123456789", k=7))
                formatted_link = f"evento-{event_id}-{sub_id}-{final_link}"
                
                new_event_link = EventosLink(
                    evento_id=event_id,
                    inscrito_id=sub_id,
                    link=formatted_link  
                )
                db.session.add(new_event_link)
                db.session.commit()
                
                return formatted_link
                
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_event_link(self, event_id: int, sub_id: int) -> EventosLink:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(EventosLink)
                .filter(
                    EventosLink.evento_id == event_id, 
                    EventosLink.inscrito_id == sub_id
                )
                .one_or_none()
            )
            return data