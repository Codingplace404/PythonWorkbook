from typing import List, Union
from numbers import Real


class Rectangle:
    """Class to describe a rectangle

    :attr a: side length a
    :type a: Real
    :attr b: side length b
    :type b: Real

    :method get_area: Calculates area of rectangle object
    :method get_scope: Calculates scope of rectangle object
    """
    def __init__(self, a: Real, b: Real):
        """Constructs all the necessary attributes for the rectangle object.

        :param a: side length a
        :param b: side length b
        """
        self.a = a
        self.b = b

    def get_area(self) -> Real:
        """Calculates area of rectangle object

        :returns: Value of area
        """
        return self.a * self.b

    def get_scope(self) -> Real:
        """Calculates scope of rectangle object

        :returns: Value of scope
        """
        return 2 * (self.a + self.b)


class BaseArticle:
    """This is a Base Class for all articles.

    :attr title: title of article
    :type stock: str
    :attr manufacturing_costs: manufacturing costs of article
    :type manufacturing_costs: float
    :attr recommended_price: recommended price of article
    :type recommended_price: float
    :attr price: current sell price of article
    :type price: float

    :method age_verification_is_required: Default Value False
    :method get_revenue: Revenue of Article
    """

    def __init__(self, title: str, manufacturing_costs: float,
                 recommended_price: float, price: float):
        """Constructs all the necessary attributes for the BaseArticle object.

        :param title: title of article
        :param manufacturing_costs: manufacturing costs of article
        :param recommended_price: recommended price of article
        :param price: current sell price of article
        """
        self.title = title
        self.manufacturing_costs = manufacturing_costs
        self.recommended_price = recommended_price
        self.price = price

    def age_verification_is_required(self) -> bool:
        """Information if a person needs to verify age for buying this
            article.

        :returns: Default False for BaseClass
        """
        return False

    def get_revenue(self) -> float:
        """Returns Article Revenue which is basically difference of price
            and manufacturing_costs

        :returns: Revenue of article
        """
        return self.price - self.manufacturing_costs


class TShirtArticle(BaseArticle):
    """Special article for Tshirts. This class inherits from
        BaseArticle class.

    :attr size: Size of TShirt.
        Allowed values: ["xs", "s", "m", "l", "xl", "xxl"]
    :type size: str
    :attr brand: Brand of TShirt
    :type brand: str
    """

    def __init__(self, title: str, manufacturing_costs: float, price: float,
                 recommended_price: float, size: float, brand: str):
        """Constructs all the necessary attributes for the TShirt object.

        :param title: title of Tshirt
        :param manufacturing_costs: manufacturing costs of Tshirt
        :param recommended_price: recommended price of Tshirt
        :param size: Size of TShirt
            Allowed values: ["xs", "s", "m", "l", "xl", "xxl"]
        :param brand: Brand of TShirt
        :raises: ValueError if size is not in allowed values
        """
        self.title = title
        self.manufacturing_costs = manufacturing_costs
        self.price = price
        self.recommended_price = recommended_price

        if size not in ["xs", "s", "m", "l", "xl", "xxl"]:
            raise ValueError(
                f"Size should be xs, s, m, l, xl, xxl but it's {size}."
            )
        self.size = size

        self.brand = brand


class FilmArticle(BaseArticle):
    """Special article for Films. This class inherits from
        BaseArticle class.

    :attr type_: Type of film.
        Allowed Values: ["dvd", "bluray", "4k"]
    :type type_: str
    :attr age_restriction: Age restriction of film
        Allowed Values: [0, 6, 12, 16, 18]
    :type age_restriction: int
    :attr cast: Cast of Film
    :type cast: List[str]
    """

    def __init__(self, title: str, manufacturing_costs: float, price: float,
                 recommended_price: float, type_: str, age_restriction: int,
                 cast: List[str]):
        """Constructs all the necessary attributes for the TShirt object.

        :param title: title of Tshirt
        :param manufacturing_costs: manufacturing costs of Tshirt
        :param recommended_price: recommended price of Tshirt
        :param type_: Type of film.
            Allowed Values: ["dvd", "bluray", "4k"]
        :param age_restriction: Age restriction of film
            Allowed Values: [0, 6, 12, 16, 18]
        :param cast: Cast of Film
        :raises: TypeError if `type_` is not in allowed values
        :raises: ValueError if `age_restriction` is not in allowed values
        """
        self.title = title
        self.manufacturing_costs = manufacturing_costs
        self.price = price
        self.recommended_price = recommended_price

        if type_ not in ["dvd", "bluray", "4k"]:
            raise TypeError(
                f"Type must be dvd, bluray or 4k but it's {type_}."
            )
        self.type_ = type_

        if age_restriction not in [0, 6, 12, 16, 18]:
            raise ValueError(
                f"Type must be , 6, 12, 16 or 18 but it's {age_restriction}."
            )
        self.age_restriction = age_restriction

        self.cast = cast

    def age_verification_is_required(self) -> bool:
        """Information if a person needs to verify age for buying this
            film.

        :returns: True if age_restriction of object is greater than 0
        """
        return self.age_restriction > 0


class OrderObject:
    """Single Order Object for having a better Order handling.

    :attr article: Article of order obj
    :type article: Union[BaseArticle, TShirtArticle, FilmArticle]
    :attr quantity: Quantity of ordered object
    :type quantity: int
    """

    def __init__(self,
                 article: Union[BaseArticle, TShirtArticle, FilmArticle],
                 quantity: int):
        """Constructs all the necessary attributes for the OrderObject object.

        :param arcticle: Article of ordered Object
        :param quantity: Quantity of ordered Object
        :raises: ValueError if quantity lower than 0
        """
        self.article = article

        if quantity < 0:
            raise ValueError(
                f"quantity must not be lower than 0 but it's {quantity}"
            )
        self.quantity = quantity


class Order:
    """Class for ordering articles

    :attr ordered_objects: Ordered Objects
    :type ordered_objects: List[OrderObject]
    :attr shipping_address: Shipping Address for ordering
    :type shipping_address: str

    :method age_verification_is_required: info if an article has an age
        requirement.
    :method get_price: get price for order
    """

    def __init__(self, ordered_objects: List[OrderObject],
                 shipping_address: str):
        """Constructs all the necessary attributes for the OrderObject object.

        :param ordered_objects: Ordered Objects
        :param shipping_address: Shipping Address for ordering
        """
        self.ordered_objects = ordered_objects
        self.shipping_address = shipping_address

    def age_verification_is_required(self) -> bool:
        """Information if a person needs to verify age for buying this
            order.

        :returns: True if age_restriction else False
        """
        for obj in self.ordered_objects:
            if obj.article.age_verification_is_required():
                return True
        return False

    def get_price(self) -> float:
        """Get Price for this order.

        :returns: Price for order
        """
        return sum([
            obj.article.price * obj.quantity
            for obj in self.ordered_objects
        ])
