import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name" : "meuNome222",
        "email" : "email22@email.com",
        "evento_id" : 2        
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subs():
    email = "email@email.com"
    evento_id = 2
    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subs(email, evento_id)
    
    print(resp.nome)
    
@pytest.mark.skip("Select in DB")    
def test_ranking():
    evento_id = 3
    subs_repo = SubscribersRepository()
    resp = subs_repo.get_ranking(evento_id)
    print()
    
    for element in resp:
        print(f"Link: {element.link}, total de inscritos: {element.total}")
    