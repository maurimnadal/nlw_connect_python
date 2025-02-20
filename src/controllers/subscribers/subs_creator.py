from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
    def __init__(self, subs_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subs_repo
    
    def create(self, http_request: HttpRequest) -> HttpResponse:
        sub_info = http_request.body["data"]
        sub_email = sub_info["email"]
        evento_id = sub_info["evento_id"]
        
        self.__check_sub(sub_email, evento_id)
        self.__insert_sub(sub_info)
        return self.__format_response(sub_info)
        
        
    def __check_sub(self, sub_email: str, evento_id: int) -> None:
        response = self.__subs_repo.select_subs(sub_email, evento_id)
        if response:
            raise Exception("Subscriber already exists")
        
    def __insert_sub(self, sub_info: dict) -> None:
        self.__subs_repo.insert(sub_info)
        
    def __format_response(self, sub_info: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": 1,
                    "attributes": {
                        "event_name": sub_info
                    }
                }
            },
            status_code=201
        )
        