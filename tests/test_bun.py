from praktikum.bun import Bun
from data import Data
import allure


class TestBun:
	@allure.title('Проверка инициализации булки: name, price')
	def test_initial_name_price(self):
		bun = Bun(Data.bun_name, Data.bun_price)
		assert bun.name == Data.bun_name and bun.price == Data.bun_price

	@allure.title('Проверка метода get_name,возвращающего name булки')
	def test_get_bun_name(self):
		bun = Bun(Data.bun_name, Data.bun_price)
		assert bun.name == bun.get_name()

	@allure.title('Проверка метода get_price,возвращающего price булки')
	def test_get_bun_price(self):
		bun = Bun(Data.bun_name, Data.bun_price)
		assert bun.price == bun.get_price()
