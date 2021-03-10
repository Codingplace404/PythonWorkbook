import pytest

from tasks._01_basics.classes import (
    Rectangle, BaseArticle, TShirtArticle, FilmArticle, OrderObject, Order
)

# from solutions._01_basics.classes import (
#     Rectangle, BaseArticle, TShirtArticle, FilmArticle, OrderObject, Order
# )


def test_rectangle_init():
    rectangle = Rectangle(2, 4)
    assert rectangle.a == 2
    assert rectangle.b == 4


class TestReactangle:
    def setup_class(self):
        self.a, self.b = 2, 2.5
        self.rectangle = Rectangle(self.a, self.b)

    def test_get_area(self):
        assert self.rectangle.get_area() == self.a * self.b

    def test_get_scope(self):
        assert self.rectangle.get_scope() == 2 * (self.a + self.b)


def test_base_article_init():
    title = "Testarticle"
    manufacturing_costs = 2.35
    recommended_price = 9.99
    price = 9.99

    article = BaseArticle(
        title=title,
        manufacturing_costs=manufacturing_costs,
        recommended_price=recommended_price,
        price=price
    )
    assert article.title == title
    assert article.manufacturing_costs == manufacturing_costs
    assert article.recommended_price == recommended_price
    assert article.price == price


class TestBaseArticle:
    def setup_class(self):
        self.manufacturing_costs = 2.35
        self.price = 9.99
        self.article = BaseArticle(
            title="Testarticle",
            manufacturing_costs=self.manufacturing_costs,
            recommended_price=9.99,
            price=self.price
        )

    def test_age_verification_is_required(self):
        assert not self.article.age_verification_is_required()

    def test_get_revenue(self):
        expected_revenue = self.price - self.manufacturing_costs
        assert self.article.get_revenue() == expected_revenue


class TestTShirtArticleInit:
    def test_successfull_init(self):
        title = "Test TShirt"
        manufacturing_costs = 2.23
        price = 9.99
        recommended_price = 9.99
        size = "l"
        brand = "test brand"
        tshirt_article = TShirtArticle(
            title=title,
            manufacturing_costs=manufacturing_costs,
            recommended_price=recommended_price,
            price=price,
            size=size,
            brand=brand
        )
        assert tshirt_article.title == title
        assert tshirt_article.manufacturing_costs == manufacturing_costs
        assert tshirt_article.price == price
        assert tshirt_article.recommended_price == recommended_price
        assert tshirt_article.size == size
        assert tshirt_article.brand == brand

    def test_raise_value_error_on_wrong_size(self):
        with pytest.raises(ValueError):
            TShirtArticle(
                title="Test Short",
                manufacturing_costs=2.34,
                recommended_price=9.99,
                price=9.99,
                size="any",
                brand="Testbrand"
            )


class TestFilmArticleInit:
    def test_successfull_init(self):
        title = "Test TShirt"
        manufacturing_costs = 2.23
        price = 9.99
        recommended_price = 9.99
        type_ = "4k"
        age_restriction = 6
        cast = ["Tom Hanks", "Robert De Niro", "Taylor Swift"]
        film_article = FilmArticle(
            title=title,
            manufacturing_costs=manufacturing_costs,
            recommended_price=recommended_price,
            price=price,
            type_=type_,
            age_restriction=age_restriction,
            cast=cast
        )
        assert film_article.title == title
        assert film_article.manufacturing_costs == manufacturing_costs
        assert film_article.price == price
        assert film_article.recommended_price == recommended_price
        assert film_article.type_ == type_
        assert film_article.age_restriction == age_restriction
        assert film_article.cast == cast

    def test_raise_type_error_on_wrong_type(self):
        with pytest.raises(TypeError):
            FilmArticle(
                title="Test TShirt",
                manufacturing_costs=2.23,
                recommended_price=9.99,
                price=9.99,
                type_="INVALID TYPE",
                age_restriction=6,
                cast=["Tom Hanks", "Robert De Niro", "Taylor Swift"]
            )

    def test_raise_value_error_on_wrong_age_restriction(self):
        with pytest.raises(ValueError):
            FilmArticle(
                title="Test TShirt",
                manufacturing_costs=2.23,
                recommended_price=9.99,
                price=9.99,
                type_="dvd",
                age_restriction=None,
                cast=["Tom Hanks", "Robert De Niro", "Taylor Swift"]
            )


class TestFilmArticle:
    def test_age_verification_is_required_true(self):
        for age in [6, 12, 16, 18]:
            film = FilmArticle(
                title="Test TShirt",
                manufacturing_costs=2.23,
                recommended_price=9.99,
                price=9.99,
                type_="4k",
                age_restriction=age,
                cast=["Tom Hanks", "Robert De Niro", "Taylor Swift"]
            )
            assert film.age_verification_is_required()

    def test_age_verification_is_required_false(self):
        film = FilmArticle(
            title="Test TShirt",
            manufacturing_costs=2.23,
            recommended_price=9.99,
            price=9.99,
            type_="4k",
            age_restriction=0,
            cast=["Tom Hanks", "Robert De Niro", "Taylor Swift"]
        )
        assert not film.age_verification_is_required()


class TestOrderObjectInit:
    def setup_class(self):
        self.article = BaseArticle(
            title="Testarticle",
            manufacturing_costs=2.00,
            recommended_price=9.99,
            price=9.99
        )

    def test_successfull_init(self):
        quantity = 3
        order_object = OrderObject(article=self.article, quantity=quantity)
        assert order_object.article == self.article
        assert order_object.quantity == quantity

    def test_raise_value_error_on_wrong_quantity(self):
        quantity = -1
        with pytest.raises(ValueError):
            OrderObject(article=self.article, quantity=quantity)


def test_order_init():
    ordered_objects = [
        OrderObject(
            article=BaseArticle(
                title="Testarticle 1",
                manufacturing_costs=2.00,
                recommended_price=9.99,
                price=9.99
            ),
            quantity=1
        )
    ]
    shipping_address = "Test Name, Test City, Test Country"
    order = Order(
        ordered_objects=ordered_objects,
        shipping_address=shipping_address
    )
    assert order.ordered_objects == ordered_objects
    assert order.shipping_address == shipping_address


class TestOrder:
    def setup_class(self):
        self.ordered_objects = [
            OrderObject(
                BaseArticle(
                    title="Testarticle 1",
                    manufacturing_costs=2.00,
                    recommended_price=9.99,
                    price=9.99
                ),
                quantity=2
            ),
            OrderObject(
                FilmArticle(
                    title="Testfilm 1",
                    manufacturing_costs=0.35,
                    recommended_price=9.99,
                    price=7.99,
                    type_="4k",
                    age_restriction=0,
                    cast=["Tom Hanks"]
                ),
                quantity=1
            ),
            OrderObject(
                TShirtArticle(
                    title="Testshirt 1",
                    manufacturing_costs=4.00,
                    recommended_price=19.99,
                    price=15.99,
                    size="l",
                    brand="Testshirt Brand"
                ),
                quantity=3
            )
        ]
        shipping_address = "Test Name, Test City, Test Country"
        self.order = Order(
            ordered_objects=self.ordered_objects,
            shipping_address=shipping_address
        )

    def test_age_verification_is_required_false(self):
        assert not self.order.age_verification_is_required()

    def test_age_verification_is_required_true(self):
        ordered_list = [obj for obj in self.ordered_objects]
        ordered_list.append(
            OrderObject(
                article=FilmArticle(
                    title="Testfilm 2",
                    manufacturing_costs=0.35,
                    recommended_price=9.99,
                    price=7.99,
                    type_="4k",
                    age_restriction=16,
                    cast=["Tom Hanks"]
                ),
                quantity=1
            )
        )
        order = Order(
            ordered_objects=ordered_list,
            shipping_address="dummy"
        )
        assert order.age_verification_is_required()

    def test_get_price(self):
        assert self.order.get_price() == 75.94
