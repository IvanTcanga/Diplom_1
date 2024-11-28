import pytest
import allure
from data import TestDataDB


class TestDatabase:
    @allure.title('test_initialization')
    def test_initialization(self, db):
        assert len(db.available_buns()) == 3 and len(db.available_ingredients()) == 6

    @allure.title('Проверка работы метода available_buns, получающего список доступных булок из db')
    @allure.description('Через параметризацию проверяем имя и стоимость каждой булки')
    @pytest.mark.parametrize('bun_index, bun_name, bun_price', TestDataDB.test_data_buns)
    def test_available_buns(self, db, bun_index, bun_name, bun_price):
        buns = db.available_buns()
        assert buns[bun_index].name == bun_name and buns[bun_index].price == bun_price

    @allure.title('Проверка работы метода available ingredients, получающего список доступных ingredients из db')
    @allure.description('Через параметризацию проверяем тип, имя и стоимость ингредиентов')
    @pytest.mark.parametrize('ing_index, ing_type, ing_name, ing_price', TestDataDB.test_data_ingredients)
    def test_available_ingredients(self, db, ing_index, ing_type, ing_name, ing_price):
        ingredients = db.available_ingredients()
        assert ingredients[ing_index].name == ing_name and ingredients[ing_index].price == ing_price and ingredients[ing_index].type == ing_type
