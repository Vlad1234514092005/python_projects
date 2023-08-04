def add_product(product, lst):
    global all_products
    if product not in all_products:
        all_products.append(product)
    if product not in lst:
        lst.append(product)
    return lst, all_products


def remove_product(product, lst):
    global all_products
    if product in all_products:
        all_products.remove(product)
    if product in lst:
        lst.remove(product)
    return lst, all_products


def print_order(order_list):
    for i in order_list:
        print(f"{i.name}: {i.cost}")


def prepare_order(order_list, product, total_cost):
    amount = int(input("Кількість продукту --> "))
    product.cost = product.price * amount
    total_cost += (product.price * amount)
    order_list.append(product)
    print_order(order_list)
    print(f"Ваше замовлення буде коштувати вам {total_cost}")
    return total_cost, order_list, amount


# class Digit:
#     @classmethod
#     def __check_value(cls, value):
#         return True if type(value) in (int, float) else False
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.__check_value(value)
#         setattr(instance, self.name, value)
#
#
# class String:
#     @classmethod
#     def __check_value(cls, value):
#         return True if type(value) == str else False
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
#
# class SetDictList:
#     @classmethod
#     def __check_value(cls, value):
#         return True if type(value) in (set, dict, list) else False
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)


class Product:
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        global current_offer
        self._name = name
        self._price = price
        self._description = description
        self._ingredients = ingredients
        self._nutritional_values = nutritional_values
        self._current_offer = is_current_offer
        self._amount = amount

    def to_current_offer(self):
        if not self.current_offer:
            self.current_offer = True
            current_offer.append(self)

    def not_current_offer(self):
        if self.current_offer:
            self.current_offer = False
            current_offer.remove(self)

    def show(self):
        print(f"Name: {self._name} \nPrice: {self._price} \nDescription: {self._description} \nIngredients: {self._ingredients} \nNutritial values: {self._nutritional_values} \nCurrent offer: {self._current_offer}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if type(value) in (int, float):
            self._price = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if type(value) == str:
            self._description = value

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        if type(value) == str:
            self._ingredients = value

    @property
    def nutritional_values(self):
        return self._nutritional_values

    @nutritional_values.setter
    def nutritional_values(self, value):
        if type(value) == type(self):
            self._nutritional_values = value

    @property
    def is_current_offer(self):
        return self._description

    @is_current_offer.setter
    def is_current_offer(self, value):
        self._is_current_offer = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if type(value) == str:
            self._amount = value


class BeefBurgers(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description,  ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == BeefBurgers:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Chicken(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Chicken:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Veggie(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Veggie:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Salads(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Salads:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Attachments(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Attachments:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class SaucesAndDressings(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == SaucesAndDressings:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Desserts(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Desserts:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Beverages(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, hot_or_cold, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        if type(hot_or_cold) == str and hot_or_cold == 'Охолоджений' or hot_or_cold == 'Гарячий' or hot_or_cold == 'Холодний':
            self._hot_or_cold = hot_or_cold
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Beverages:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)

    def sort_drinks(self):
        cold_drinks = filter(lambda x: x._hot_or_cold in ('Охолоджений', 'Холодний'), self._product_list)
        hot_drinks = filter(lambda x: x._hot_or_cold == 'Гарячий', self._product_list)
        return cold_drinks, hot_drinks


class Breakfast(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, type_, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        if type(type_) in (Attachments, Desserts, str) and type_ in ('Бублики і бургери', 'Макмаффіни і тости'):
            self._type = type_
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)

    def sort_breakfast_meals(self):
        bagels_and_burgers = filter(lambda x: x._type == 'Бублики і бургери', self._product_list)
        eggs = filter(lambda x: 'Яйця' in x._ingredients or 'Яйце' in x._ingredients, self._product_list)
        McMuffins_and_toasts = filter(lambda x: x._type == 'Макмаффіни і тости', self._product_list)
        attachments = filter(lambda x: type(x._type) == Attachments, self._product_list)
        sweet = filter(lambda x: type(x._type) == Desserts, self._product_list)
        return bagels_and_burgers, eggs, McMuffins_and_toasts, attachments, sweet

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        if type(value) == str and value in ('Бублики і бургери', 'Яйця', 'Макмаффіни і тости', 'Вкладення', 'Вкладення'):
            self._type = value


class McCafe(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, kind, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        if kind in ('Поточна пропозиція', 'Пропозиція McCafe в McDonald\'s', 'Пропозиція в McCafe'):
            self._kind = kind
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if value in ('Поточна пропозиція', 'Пропозиція McCafe в McDonald\'s', 'Пропозиція в McCafe'):
            self._kind = value


class HappyMeal(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


current_offer = []
all_products = []
your_order = []
cancelling_order = False
total_cost = 0
order_status = False

cheeseburger = BeefBurgers('Чизбургер', 42, 'Зачаровує смак сиру і яловичини.'
                                            ' Фарш з яловичини, сиру, цибулі,'
                                            ' маринований огірок і кетчуп з гірчицею в булочці пшениці.', ['Яловочина', 'Цибуля', 'Лист чеддера', 'Кисло-солодкі огірки',
                                                                                                           'Пшенична булочка', 'Кетчуп', 'Гірчиця', 'Сіль', 'Перець'],
                           {'Енергія': '254 ккал', 'Жири': '13г', 'Насичені жирні кислоти': '6.1 г', 'Цукор': '29г', 'Целюлоза': '2г', 'Білків': '16г', 'Сіль': '1.6г'})

hamburger = BeefBurgers('Гамбургер', 39, 'Константа нашої пропозиції.'
                                         ' Яловичий фарш з маринованим огірком, цибулею, кетчупом і гірчицею.'
                                         ' Пшенична булочка.', ['Яловочина', 'Цибуля', 'Лист чеддера', 'Кисло-солодкі огірки',
                                                                'Пшенична булочка', 'Кетчуп', 'Гірчиця', 'Сіль', 'Перець'],
                                            {'Енергія': '254 ккал', 'Жири': '9г', 'Насичені жирні кислоти': '3.6г', 'Цукор': '29.6г', 'Целюлоза': '2г', 'Білки': '13г', 'Сіль': '1.2г'})

crispy_bacon_McWrap = Chicken('Хрусткий бекон МакРол', 109, 'Соковиті курячі смужки, шматочок хрусткого бекону,'
                                ' тертий чеддер, свіжий салат, помідор, соління,'
                                ' кетчуп і гірчиця базиліка, загорнуті в коржі.', ['Куриця', 'Лаваш пшеничеий', 'Бекон', 'Тертий чеддер', 'Свіжі помідори', 'Салат айсберг', 'Кисло-солодкі огірки', 'Кетчуп', 'Гірчиця з базіліком'],
                              {'Енергія': '445 ккал', 'Жири': '18г', 'Насичені жирні кислоти': '4.2г', 'Цукор': '29.6г', 'Целюлоза': '2г', 'Білки': '13г', 'Сіль': '1.2г'})

grilled_italian_McWrap = Chicken("Італ'янський МакРол на грилі", 109, 'Шматочок курячої грудки гриль, свіжий огірок, помідор, рукола,'
                                ' цибуля, поєднання тонкого томатного соусу з орегано і вершковим часником умочити в розігріту коржик.',
                                 ['Куриця', 'Лаваш пшеничний', 'Огірки', 'Свіжі помідори', 'Рукола', 'Цибуля', 'Часничковий соус', 'Томатний соус орегано'],
                                 {'Енергія': '296 ккал', 'Жири': '12г', 'Насичені жирні кислоти': '1.7г', 'Цукор': '28г', 'Целюлоза': '1.9г', 'Білки': '17г', 'Сіль': '1.5г'})

single_big_tasty_chicken = Chicken('Біг-Тейсті', 105, 'Соковитий курячий бургер з злегка копченим соусом Смачні дві скибочки бекону - це смак для справжніх гурманів.',
                                   ['Куриця', 'Салат айсберг', 'Свіжі помідори', 'Булочка з насінням кунжуту', 'Емменталер', 'Цибуля', 'Великий смачний соус', 'Бекон'],
                                   {'Енергія': '427 ккал', 'Жири': '17г', 'Насичені жирні кислоти': '2г', 'Цукор': '45г', 'Волокна': '2,7г', 'Білки': '20г', 'Сіль': '1.8г'})

McChicken = Chicken('МакЧікен', 95, "Ніжне куряче м'ясо в пряних панірувальних сухарях, свіжому салаті айсберг і майонезному соусі."
                    " Ідеальне поєднання смаків у булочці, посипаній кунжутом.", ['Куриця', 'Салат айсберг', 'Булочка з насінням кунжуту', 'Соус для сендвіча'],
                    {'Енергія': '718 ккал', 'Жири': '39г', 'Насичені жирні кислоти': '10г', 'Цукор': '58г', 'Целюлоза': '3,4 г', 'Білки': '31г', 'Сіль': '4.2г'})

tasty_chicken = Chicken('Смачна курка', 59, 'Бургер з куркою в поєднанні з оригінальним смачним соусом і салатом.'
                                               'Правильний вибір, коли ви любите курку.', ["Салат айсберг", "Лист чедера", "Великий смачний соус", "Пшенична булочка", "Куриця", "Бекон"],
                        {'Енергія': '467 ккал', 'Жири': '26г', 'Насичені жирні кислоти': '6.3г', 'Цукор': '40г', 'Целюлоза': '2.3г', 'Білки': '17г', 'Сіль': '2.3г'})

chicken_burger = Chicken('Бургер з куриці', 42, "Відмінний сендвіч."
                                                " Смажене куряче філе в паніровці з дрібно нарізаного м'яса,"
                                                " свіжий салат і солодкий соус чилі.", ["Куриця", "Салат айсберг", "Пшенична булочка", "Солодкий соус чилі"],
                         {'Енергія': '342 ккал', 'Жири': '11г', 'Насичені жирні кислоти': '1.7г', 'Цукор': '49г', 'Целюлоза': '2.2г', 'Білки': '12г', 'Сіль': '1.8г'})

chicken_McNuggets = Chicken('Курячі мак-наггетси', 99, 'Куряче ласощі з соусом на ваш вибір. Золотисті смажені шматочки курячої грудки.'
                                                       ' Виберіть власний розмір порції.'
                                                       ' Ви можете вибрати з 6, 9 або 20 штук відмінних курячих макнуггетів.', [],
                            {'Енергія': '268 ккал', 'Жири': '14г', 'Насичені жирні кислоти': '1.7г', 'Цукор': '19г', 'Целюлоза': '1.4г', 'Білки': '17г', 'Сіль': '1.3г'})

chicken_strips = Chicken('Курячі стріпси', 65, 'Два соковитих шматочка курячої грудки в спеціальній панірувальній сухарях відмінно доповнять будь-яке меню.'
                                               ' Насолоджуйтесь ними, як ніколи раніше, з одним із наших соусів! Не можете насититися ними?'
                                               ' Так що в меню є чотири з картоплею фрі і напоєм.', [],
                         {'Енергія': '217 ккал', 'Жири': '10г', 'Насичені жирні кислоти': '1.1г', 'Цукор': '19г', 'Целюлоза': '2г', 'Білки': '13г', 'Сіль': '1.2г'})

snack_wrap = Chicken('Закусочний рол', 42, 'Свіжий салат, майонезний соус і сир.'
                                           ' Правильний вибір, коли ви отримаєте смак до чогось.', ["Куриця", "Чеддер", "Салат айсберг", "Лаваш пшеничний", "Сендвіч соус"],
                     {'Енергія': '204 ккал', 'Жири': '8г', 'Насичені жирні кислоти': '1.7г', 'Цукор': '23г', 'Целюлоза': '1.5г', 'Білки': '9г', 'Сіль': '1.6г'})


fried_cheese_fresh = Veggie('Смажений сир свіжий', 59, 'Улюблений смажений сир з соусом тартар і салатом красиво сидить в булочці.'
                                                       ' Є тільки один такий.', ["Пшенична булочка", "Соус тартар", "Салат айсберг", "Смажений сир ейдам"],
                            {'Енергія': '373 ккал', 'Жири': '16г', 'Насичені жирні кислоти': '4.6г', 'Цукор': '41г', 'Целюлоза': '2.5г', 'Білки': '15г', 'Сіль': '1.7г'})

veggie_burger = Veggie('Веггі-бургер', 115, 'Хрусткий, соковитий і повний чудового овочевого смаку. Побалуйте себе бургером з хрусткими млинцями Veggie,'
                       ' сиром чеддер і часниковим соусом.', ["Млинець з овочами", "Булочки із насінням кунжуту", "Салат айсберг", "Лист чеддера", "Свіжі помідори", "Часничковий соус"],
                       {'Енергія': '617 ккал', 'Жири': '34г', 'Насичені жирні кислоти': '7.6г', 'Цукор': '58г', 'Целюлоза': '8.3г', 'Білки': '17г', 'Сіль': '3.8г'})

veggie_wrap = Veggie('Рол з овочами', 115, "Шматочки податливих овочевих млинців в хрустких панірувальних сухарях зі свіжими помідорами, салатом і чеддером."
                    "Все це приправляють смачною гірчицею базиліка."
                    "Просто свіжа обгортка, яка чудово смакує навіть без м'яса.",["Млинець з овочами", "Свіжі помідори", "Третій чеддер", "Салат айсберг", "Руколла", "Гірчиця з базіліком", "Лаваш"],
                     {'Енергія': '453 ккал', 'Жири': '27г', 'Насичені жирні кислоти': '4.1г', 'Цукор': '39г', 'Целюлоза': '2.7,', 'Білки': '8.4г', 'Сіль': '4г'})


veggie_salad = Salads('Салат з овочами', 149, 'Шматочки хрустких млинців з овочами з щедрою порцією нещодавно змішаної салатної суміші,'
                       ' повної руколи, буряка, салату ромен і салату фрізе.'
                       ' А також з помідорами черрі, огірком, грінками і тертим чеддером.'
                       ' Овочева симфонія буде доповнена заправкою на ваш смак.',
                      ["Млинець з овочами", "Третій чеддер", "Огірки", "Помідори черрі", "Мікс для салатів", "Сухарі"],
                      {'Енергія': '443 ккал', 'Жири': '24г', 'Насичені жирні кислоти': '7г', 'Цукор': '35г', 'Целюлоза': '9г', 'Білки': '14г', 'Сіль': '3г'})

crispy_chicken_salad = Salads('Хрусткий курячий салат', 135, 'Велика порція щойно змішаного хрусткого салату змішати.'
                                'Курячі смужки в хрустких панірувальних сухарях, свіжих овочах, грінках і тертому чеддері.'
                                'З заправкою за смаком.', ["Куриця", "Третій чеддер", "Огірки", "Помідори черрі", "Мікс для салатів", "Сухарі"],
                              {'Енергія': '374 ккал', 'Жири': '15.7г', 'Насичені жирні кислоти': '5.1г', 'Цукор': '35г', 'Целюлоза': '4.3г', 'Білки': '21г', 'Сіль': '2г'})

grilled_chicken_salad = Salads('Салат з курки гриль', 135, 'Соковита куряча грудка гриль з новою хрусткою салатною сумішшю, помідори черрі, огірок, грінки, тертий сир чеддер і заправка на ваш смак.',
                               ["Куриця", "Третій чеддер", "Огірки", "Помідори черрі", "Мікс для салатів", "Сухарі"],
                               {'Енергія': '241 ккал', 'Жири': '7.7г', 'Насичені жирні кислоти': '4.3г', 'Цукор': '16.6г', 'Целюлоза': '3.5г', 'Білки': '24г', 'Сіль': '1.9г'})

garden_salad = Salads('Садовий салат', 49, 'Ідеальний свіжий гарнір.'
                      'З новим поєднанням хрустких салатів, помідорів черрі і огірка.'
                      'Все це з підгодівлею на ваш вибір.',
                      ["Помідори черрі", "Мікс для салатів", "Сухарі"],
                      {'Енергія': '55 ккал', 'Жири': '0.3г', 'Насичені жирні кислоти': '0г', 'Цукор': '10.6г', 'Целюлоза': '2.1г', 'Білки': '1.5г', 'Сіль': '0.65г'})


McShakerFries = Attachments('Макшакер Фрі', 55, 'Середні порції картоплі фрі зі спеціальними сирними спеціями, які роблять їх унікальним сирним делікатесом.'
                            'Просто покладіть їх в пакет, посипте, струсіть. Ось і все!', [],
                            {'Енергія': '308 ккал', 'Жири': '14г', 'Насичені жирні кислоти': '1.5г', 'Цукор': '39г', 'Целюлоза': '3.7г', 'Білки': '3.9г', 'Сіль': '0.89г'})

camembert = Attachments('Камамбер', 99, "Перекус або ціле меню?"
                        " Якщо вам ніколи не вистачає камамберів, тепер ви можете мати п'ять з них в меню з картоплею фрі, напоєм і соусом."
                        " А потім навіть самостійно. П'ять чи три? Вирішувати тільки вам.", [],
                        {'Енергія': '188 ккал', 'Жири': '11г', 'Насичені жирні кислоти': '5.5г', 'Цукор': '12г', 'Целюлоза': '0.5г', 'Білки': '8.9г', 'Сіль': '0.96г'})

french_fries = Attachments('Картопля фрі', 45, 'Улюблений гарнір і ласощі.'
                            'З ретельно відібраних видів картоплі.'
                            'Виберіть власний розмір порції.'
                            'Ми пропонуємо невелику, середню та велику порцію картоплі фрі.', [],
                           {'Енергія': '231 ккал', 'Жири': '11г', 'Насичені жирні кислоти': '1г', 'Цукор': '29г', 'Целюлоза': '2.8г', 'Білки': '2.8г', 'Сіль': '0.55г'})


cheese_king_sauce = SaucesAndDressings('Соус «Сир Кінг»', 15, 'Чарівний сирний соус,'
                                        'який ви любите в Cheese King,'
                                        'тепер можна їсти окремо.', [],
                                       {'Енергія': '125 ккал', 'Жири': '13г', 'Насичені жирні кислоти': '1.3г', 'Цукор': '2.1г', 'Целюлоза': '0.1г', 'Білки': '0.6г', 'Сіль': '0.53г'})

ketchup = SaucesAndDressings('Кетчуп', 12, 'Що я можу сказати?'
                            'Класика з усіх томатних класиків.'
                            'Більш популярного соусу в світі ви не знайдете.', [],
                            {'Енергія': '14 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '3.1г', 'Целюлоза': '0г', 'Білки': '0.2г', 'Сіль': '0.25г'})

pommes_frites_sauce = SaucesAndDressings('Соус Pommes frites', 12, "Після кетчупу другий за популярністю соус для картоплі фрі,"
                                         "але відмінно поєднується він і з м'ясом.", [],
                                         {'Енергія': '56 ккал', 'Жири': '4.5г', 'Насичені жирні кислоти': '0.3г', 'Цукор': '3.6г', 'Целюлоза': '0.1г', 'Білки': '0.2г', 'Сіль': '0.24г'})

hellmann_s_tartar_sauce = SaucesAndDressings('Соус тартар Хеллмана', 17, 'Старий знайомий зубний камінь! Це чудово для всього!', [],
                                             {'Енергія': '120 ккал', 'Жири': '12г', 'Насичені жирні кислоти': '0.7г', 'Цукор': '0.4г', 'Целюлоза': '0г', 'Білки': '0.5г', 'Сіль': '0.44г'})

sweet_and_sour_sauce = SaucesAndDressings('Кисло-солодкий соус', 15, 'Протилежності притягуються.'
                                          'Смачний соус, який відмінно присмачить будь-яку з улюблених страв.', [],
                                          {'Енергія': '42 ккал', 'Жири': '0.3г', 'Насичені жирні кислоти': '0г', 'Цукор': '9.7', 'Целюлоза': '0г', 'Білки': '0.1г', 'Сіль': '0.25г'})

barbecue_sauce = SaucesAndDressings('Соус для барбекю', 15, "Американська класика."
                                    "Своїм «димним» ароматом він прекрасно поєднується з усіма видами м'яса.", [],
                                    {'Енергія': '40 ккал', 'Жири': '0.3г', 'Насичені жирні кислоти': '0г', 'Цукор': '9.2г', 'Целюлоза': '0.2г', 'Білки': '0.2г', 'Сіль': '0.47г'})

curry_sauce = SaucesAndDressings('Соус каррі', 15, 'Що я можу сказати?'
                                                   ' Чіткий вибір для тих, хто любить додавати в їжу «східний» хист.', [],
                                 {'Енергія': '163 ккал', 'Жири': '0.3г', 'Насичені жирні кислоти': '0г', 'Цукор': '8.6г', 'Целюлоза': '0.4г', 'Білки': '0.2г', 'Сіль': '0.28г'})

mustard_sauce = SaucesAndDressings('Гірчичний соус', 15, 'Специфічний, злегка пряний смак, що нагадує Францію.', [],
                                   {'Енергія': '226 ккал', 'Жири': '3г', 'Насичені жирні кислоти': '0.3г', 'Цукор': '6.4г', 'Целюлоза': '0г', 'Білки': '0.5г', 'Сіль': '0.48г'})

lemon_chili = SaucesAndDressings('Лимонний чилі', 15, 'Комусь це подобається гостро!'
                                ' Назва говорить про те, що цей соус особливо оцінять любителі чилі.', [],
                                 {'Енергія': '298 ккал', 'Жири': '0.3г', 'Насичені жирні кислоти': '0г', 'Цукор': '17г', 'Целюлоза': '0.4г', 'Білки': '0.3г', 'Сіль': '0.68г'})

caesar_grout = SaucesAndDressings('Затірка цезаря', 17, 'Вдарте між начинками!'
                                ' Популярний в основному в прибережних районах,'
                                ' але також має чудовий смак усередині країни', [],
                                  {'Енергія': '427 ккал', 'Жири': '9.1г', 'Насичені жирні кислоти': '1.4г', 'Цукор': '3г', 'Целюлоза': '0.1г', 'Білки': '1.4г', 'Сіль': '0.82г'})

cocktail_dressing = SaucesAndDressings('Коктейльна заправка', 17, 'Свіжа йогуртова заправка з легкою ноткою помідорів найкращим чином доповнить смак улюбленого салату.', [],
                                       {'Енергія': '432 ккал', 'Жири': '10г', 'Насичені жирні кислоти': '0.8г', 'Цукор': '3.4г', 'Целюлоза': '0.2г', 'Білки': '0.6г', 'Сіль': '0.77г'})

yogurt_dressing = SaucesAndDressings('Йогуртова заправка', 17, 'Варіант для тих, хто хоче свіжої заправки, яка підкреслить смак овочів.', [],
                                     {'Енергія': '432 ккал', 'Жири': '9.9г', 'Насичені жирні кислоти': '0.9г', 'Цукор': '3.3г', 'Целюлоза': '0.2г', 'Білки': '0.6г', 'Сіль': '0.76г'})

cheese_dressing = SaucesAndDressings('Сирна заправка', 17, "Ви тип сиру? Обов'язково спробуйте заправку зі смаком блакитного сиру!"
                                    " Він додасть салату абсолютно новий, несподіваний розмір.", [],
                                     {'Енергія': '520 ккал', 'Жири': '12г', 'Насичені жирні кислоти': '2.1г', 'Цукор': '2.5г', 'Целюлоза': '0.2г', 'Білки': '1.6г', 'Сіль': '1.1г'})

balsamic = SaucesAndDressings('Бальзамічний', 17, 'Бальзамічний в поєднанні з оливковою олією - проста, але перевірена класика.'
                                                  ' Тут просто не помилишся.', [],
                              {'Енергія': '27 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '1.5г', 'Целюлоза': '0г', 'Білки': '0.1г', 'Сіль': '0.3г'})

olive_oil = SaucesAndDressings('Оливкова олія', 17, 'Оливкова олія в поєднанні з бальзамічним - проста, але перевірена класика.'
                                                    ' Тут просто не помилишся.', [],
                               {'Енергія': '315 ккал', 'Жири': '8.4г', 'Насичені жирні кислоти': '1.3г', 'Цукор': '0г', 'Целюлоза': '0г', 'Білки': '0г', 'Сіль': '0г'})


pastry_chocolate_and_salted_caramel = Desserts('Кондитерські, шоколадні та солона карамель', 42, 'Якщо ви любите і солоне, і солодке, спробуйте ці ласощі!'
                                                ' Поєднання солоної карамелі і шоколаду в хрусткому пакеті вижене відразу всю вашу тягу!', [],
                                               {'Енергія': '1282 ккал', 'Жири': '16г', 'Насичені жирні кислоти': '5г', 'Цукор': '37г', 'Целюлоза': '2г', 'Білки': '3г', 'Сіль': '0г'})

McFlurry_oreo = Desserts('Макфлурі Орео', 75, "Ваше улюблене молочне морозиво тепер у новій обмеженій серії з хрусткими посипаннями печива Oreo та шоколадною глазур'ю."
                                              " Так що викиньте ласунів за борт!", [],
                         {'Енергія': '1773 ккал', 'Жири': '13г', 'Насичені жирні кислоти': '8.3г', 'Цукор': '67г', 'Целюлоза': '1.4г', 'Білки': '8.2г', 'Сіль': '0.52г'})

McFlurry = Desserts('Макфлурі', 72, 'Чудовий десерт з молочним морозивом! Налаштуйте його так, як вам найбільше подобається.'
                    ' Комбінуйте топінги і топінги – один топінг і один топінг, два топінга або два топінга.'
                    ' Є вибір начинок: шоколадний, полуничний, карамельний. Кіт Кет, Сочевиця, Лотос Біскофф або відповідно до сезонної пропозиції.', [],
                    {'Енергія': '790 ккал', 'Жири': '5г', 'Насичені жирні кислоти': '3.4г', 'Цукор': '31г', 'Целюлоза': '0г', 'Білки': '4.9г', 'Сіль': '0.2г'})

McSundae_caramel = Desserts('Карамель Мак-Сунді', 49, "Задоволення від молока. Пломбір з смачною карамельною глазур'ю. Незабутній смак!", [],
                            {'Енергія': '1207 ккал', 'Жири': '6.1г', 'Насичені жирні кислоти': '4.1г', 'Цукор': '53г', 'Целюлоза': '0г', 'Білки': '4.7г', 'Сіль': '0.3'})

McSundae_chocolate = Desserts('Шоколад Мак-Сунді', 49, "Задоволення від молока. Пломбір з смачною шоколадною глазур'ю. Незабутній смак!", [],
                              {'Енергія': '1171 ккал', 'Жири': '8.2г', 'Насичені жирні кислоти': '6.4г', 'Цукор': '45г', 'Целюлоза': '1.3г', 'Білки': '5.5г', 'Сіль': '0.38г'})

McSundae_strawberry = Desserts('Полуниця Мак-Сунді', 49, "Задоволення від молока. Пломбір з смачною полуничною глазур'ю. Незабутній смак!", [],
                               {'Енергія': '959 ккал', 'Жири': '4.1г', 'Насичені жирні кислоти': '2.8г', 'Цукор': '43г', 'Целюлоза': '0.6г', 'Білки': '4.1г', 'Сіль': '0.16г'})

grand_McSundae_chocolate = Desserts('Шоколад Grand McSundae', 69, "Популярне вершкове морозиво, увінчане шоколадною глазур'ю з бісквітною посипкою з популярного карамельного печива Lotus Biscoff."
                                    " Крім того, прикрашена густа збитою вершками шапочка.", [],
                                    {'Енергія': '1925 ккал', 'Жири': '21г', 'Насичені жирні кислоти': '13г', 'Цукор': '61г', 'Целюлоза': '1г', 'Білки': '7.4г', 'Сіль': '0.56г'})

grand_McSundae_caramel = Desserts('Гранд Максунді Карамель', 69, "Популярне вершкове морозиво, увінчане карамельною глазур'ю з бісквітним посипкою з популярного карамельного печива Lotus Biscoff."
                                " Крім того, прикрашена густа збитою вершками шапочка.", [],
                                  {'Енергія': '1963 ккал', 'Жири': '19г', 'Насичені жирні кислоти': '11г', 'Цукор': '69г', 'Целюлоза': '0.2г', 'Білки': '6.6г', 'Сіль': '0.5г'})

grand_McSundae_strawberry = Desserts('Полуниця Гранд Мак-Сунді', 69, "Популярне вершкове морозиво, увінчане полуничною глазур'ю з бісквітними посипаннями з популярного карамельного печива Lotus Biscoff."
                                    " Крім того, прикрашена густа збитою вершками шапочка.", [],
                                     {'Енергія': '1706 ккал', 'Жири': '17г', 'Насичені жирні кислоти': '10г', 'Цукор': '58г', 'Целюлоза': '0.9г', 'Білки': '6г', 'Сіль': '0.38'})

ice_cream_in_cone = Desserts('Морозиво в конусі', 42, 'Літнє частування в конусі. Чесне морозиво так, як вам подобається.', [],
                             {'Енергія': '591 ккал', 'Жири': '3.55г', 'Насичені жирні кислоти': '2.1г', 'Цукор': '23.39г', 'Целюлоза': '0.3г', 'Білки': '3.5г', 'Сіль': '0.14г'})

milk_shake_with_vanilla_flavour = Desserts('Молочний коктейль з ванільним смаком', 45, 'Побалуйте себе ароматом ванілі. Заморожений молочний коктейль з ванільним смаком вас вразить.'
                                        ' Дозвольте собі бути зачарованими винятковим досвідом.'
                                        ' Вибирайте маленький або великий молочний коктейль на свій смак.', [],
                                        {'Енергія': '745 ккал', 'Жири': '3.3г', 'Насичені жирні кислоти': '2.2г', 'Цукор': '32г', 'Целюлоза': '0г', 'Білки': '4.6г', 'Сіль': '0.16г'})

milk_shake_with_strawberry_flavour = Desserts('Молочний коктейль з суничним смаком', 45, 'Побалуйте себе суничним захопленням. Заморожений молочний коктейль з суничним ароматом вас вразить.'
                                                ' Дозвольте собі бути зачарованими винятковим досвідом.'
                                                ' Вибирайте маленький або великий молочний коктейль на свій смак.', [],
                                              {'Енергія': '750 ккал', 'Жири': '3.3г', 'Насичені жирні кислоти': '2.2г', 'Цукор': '32г', 'Целюлоза': '0г', 'Білки': '4.6г', 'Сіль': '0.17г'})

milk_shake_with_chocolate_flavour = Desserts('Молочний коктейль зі смаком шоколаду', 45, 'Побалуйте себе шоколадом. Заморожений молочний коктейль з шоколадним смаком вас вразить.'
                                            ' Дозвольте собі бути зачарованими винятковим досвідом.'
                                            ' Вибирайте маленький або великий молочний коктейль на свій смак.', [],
                                             {'Енергія': '773 ккал', 'Жири': '3.6г', 'Насичені жирні кислоти': '2.4г', 'Цукор': '32г', 'Целюлоза': '0.6г', 'Білки': '5г', 'Сіль': '0.35г'})

shake_deluxe_with_vanilla_whipped_cream = Desserts('Shake Deluxe з ванільними збитими вершками', 55, 'Заморожений молочний коктейль з ванільним смаком вас вразить.'
                                                ' Класика від Макдональдса, прикрашена збитими вершками.', [],
                                                {'Енергія': '1112 ккал', 'Жири': '12г', 'Насичені жирні кислоти': '7.3г', 'Цукор': '33г', 'Целюлоза': '0г', 'Білки': '5.4г', 'Сіль': '0.2г'})

shake_deluxe_with_strawberry_whipped_cream = Desserts('Шейк Делюкс з полуничними збитими вершками', 55, 'Заморожений молочний коктейль з суничним ароматом вас вразить.'
                                                    ' Класика від Макдональдса, прикрашена збитими вершками.', [],
                                                    {'Енергія': '1117 ккал', 'Жири': '12г', 'Насичені жирні кислоти': '7.3г', 'Цукор': '34г', 'Целюлоза': '2г', 'Білки': '13г', 'Сіль': '1.2г'})

shake_deluxe_with_whipped_cream_chocolate = Desserts('Shake Deluxe зі збитими вершками шоколаду', 55, 'Заморожений молочний коктейль з шоколадним смаком вас вразить.'
                                                    ' Класика від Макдональдса, прикрашена збитими вершками.', [],
                                                     {'Енергія': '955 ккал', 'Жири': '12г', 'Насичені жирні кислоти': '2.8г', 'Цукор': '28г', 'Целюлоза': '1.5г', 'Білки': '2.3г', 'Сіль': '0.33г'})

apple_pastry = Desserts('Яблучна випічка', 42, 'Солодке захоплення. Десерт, наповнений фруктовою начинкою.'
                        ' Відмінне доповнення до кави або просто самостійно.', [],
                        {'Енергія': '445 ккал', 'Жири': '18г', 'Насичені жирні кислоти': '4.2г', 'Цукор': '29.6г', 'Целюлоза': '2г', 'Білки': '13г', 'Сіль': '1.2г'})

fruit_mix = Desserts('Фруктовий мікс', 37, 'Легкий перекус.'
                    ' Свіжі фрукти відповідно до сезонного меню, в якому повно соку і енергії.', [],
                     {'Енергія': '146 ккал', 'Жири': '0.2г', 'Насичені жирні кислоти': '0.1г', 'Цукор': '8.5г', 'Целюлоза': '1.2г', 'Білки': '0.3г', 'Сіль': '0г'})


coca_cola = Beverages('Кока-кола', 42, 'Легендарний напій, який підкорив весь світ!'
                        ' Подається охолодженим з льодом. Освіжає і заряджає енергією!', [],
                      {'Енергія': '434 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '26г', 'Целюлоза': '0г', 'Білки': '0г', 'Сіль': '0г'}, 'Холодний')

fanta = Beverages('Фанта', 42, 'Традиційна Фанта, як ви її знаєте!'
                ' Фруктова спокуса у чудовому напої. Подається охолодженим з льодом.', [],
                  {'Енергія': '401 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '4.2г', 'Цукор': '24г', 'Целюлоза': '0г', 'Білки': '0г', 'Сіль': '0г'}, 'Холодний')

coca_cola_zero = Beverages('Кока-Кола Нуль', 42, 'Легендарний напій, який підкорив весь світ!'
                            ' Подається охолодженим з льодом.'
                            ' Освіжає і заряджає енергією!', [],
                           {'Енергія': '0.6 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '0г', 'Целюлоза': '0г', 'Білки': '0г', 'Сіль': '0г'}, 'Холодний')

coca_cola_zero_cinnamon = Beverages('Кока-Кола Нуль кориці', 42, 'Легендарний напій, який підкорив весь світ!'
                                    ' Подається охолодженим з льодом.'
                                    ' Освіжає і заряджає енергією!'
                                    ' Тепер зі смаком кориці.', [],
                                    {'Енергія': '2.8 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '0г', 'Целюлоза': '0г', 'Білки': '0г', 'Сіль': '0.05г'}, 'Холодний')

sprite = Beverages('Спрайт', 42, 'Традиційний спрайт, як ви його знаєте!'
                    ' Фруктова спокуса у чудовому напої.'
                    ' Подається охолодженим з льодом.', [],
                   {'Енергія': '301 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '18г', 'Целюлоза': '0г', 'Білки': '0г', 'Сіль': '0г'}, 'Холодний')

lipton_ice_tea_lemon = Beverages('Ліптон Айс Ті Лимон', 42, 'Холодний чай для максимального освіження.'
                                ' Відмінне поєднання смаку чаю і лимона.'
                                ' Подається охолодженим з льодом.', [],
                                 {'Енергія': '192 ккал', 'Жири': '1.3г', 'Насичені жирні кислоти': '0.3г', 'Цукор': '11г', 'Целюлоза': '0г', 'Білки': '1.3г', 'Сіль': '0.05г'}, 'Холодний')

kitl_raspberry = Beverages('Малина Кітл', 42, 'Малинівка Кітл для максимального освіження.'
                            ' Подається охолодженим з льодом.', [],
                           {'Енергія': '304 ккал', 'Жири': '0.4г', 'Насичені жирні кислоти': '0г', 'Цукор': '17г', 'Целюлоза': '0г', 'Білки': '0.3г', 'Сіль': '0г'}, 'Холодний')

vinea = Beverages('Вінея', 42, 'Унікальний повний виноградний смак перенесе вас у світ чуттєвого винограду, насолоди, темпераменту та спонтанності.', [],
                  {'Енергія': '398 ккал', 'Жири': '1.3г', 'Насичені жирні кислоти': '0.3г', 'Цукор': '24г', 'Целюлоза': '0г', 'Білки': '1.3г', 'Сіль': '0.03г'}, 'Холодний')

soda_water = Beverages('Газована вода', 29, 'Вони освіжають соду, повну бульбашок, саме так, як вам подобається.'
                        ' Завжди ідеально охолоджений, подається з льодом.', [], {}, 'Холодний')

orange_juice = Beverages('Апельсиновий сік', 42, 'Натуральний апельсиновий сік сповнений відмінного смаку.'
                        ' Завжди подається без льоду.', [],
                         {'Енергія': '392 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '22г', 'Целюлоза': '0г', 'Білки': '1.8г', 'Сіль': '0г'}, 'Холодний')

apple_juice = Beverages('Яблучний сік', 42, 'Натуральний яблучний сік сповнений відмінного смаку.'
                        ' Завжди подається без льоду.', [],
                        {'Енергія': '444 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '27г', 'Целюлоза': '0г', 'Білки': 'г', 'Сіль': '0г'}, 'Холодний')

pilsner_urquell = Beverages('Пілснер Уркелл', 49, "Затребувана марка пива."
                            " Для моментів благополуччя з друзями в McDonald's."
                            " Декларація виробника: підходить для целіакії при вживанні Pilsner Urquell до 1,5 л на добу.", [],
                            {'Енергія': '534 ккал', 'Жири': '0г', 'Насичені жирні кислоти': '0г', 'Цукор': '2г', 'Целюлоза': '0г', 'Білки': '2г', 'Сіль': '0г'}, 'Холодний')

still_water = Beverages('Тиха вода', 42, 'Навесні ще поливають. Подається в заводській упаковці виробника.', [], {}, 'Холодний')

gently_sparkling_water = Beverages("М'яко газована вода", 42, 'Навесні акуратно газована вода.'
                                    ' Подається в заводській упаковці виробника.', [], {}, 'Холодний')

espresso = Beverages('Еспресо', 45, 'Традиційний еспресо McCafé подається в чашці, тепер також в обраних McDrive і ресторанах без McCafé.', [], {}, 'Гарячий')

double_espresso = Beverages('Подвійний еспресо', 59, 'Подвійний еспресо-бренд McCafé, що подається в чашці,'
                            ' тепер також пропонується в обраних McDrive і ресторанах без McCafé.', [], {}, 'Гарячий')

coffee = Beverages('Кава', 45, 'Відмінна кава. Завжди свіжоприготований.'
                               ' Справедлива доза кави і води точно вимірюється автоматом.'
                               ' Подавати за запитом з цукром і вершками.', [], {}, 'Гарячий')

coffee_with_milk = Beverages('Кава з молоком', 45, 'Смачна кава з чесної 100% арабіки з гарячим молоком вже в чашці,'
                                                   ' щоб навіть водій міг легко ним насолодитися.', [],
                             {'Енергія': '134 ккал', 'Жири': '1.8г', 'Насичені жирні кислоти': '1.1г', 'Цукор': '2г', 'Целюлоза': '0г', 'Білки': '1.7г', 'Сіль': '0.14г'}, 'Гарячий')

espresso_grande = Beverages('Еспресо Гранде', 49, 'McCafé Grande еспресо подається в чашці, тепер також в обраних McDrive і ресторанах без McCafé.', [], {}, 'Гарячий')

latte = Beverages('Латте', 65, 'Популярне вишукане кафе Латте з пінним молоком.'
                ' Який можна тонко налаштувати за допомогою ванільного або горіхового аромату.'
                ' Справедлива доза кави і молока точно вимірюється автоматом. Подавати за бажанням з цукром.', [],
                  {'Енергія': '315 ккал', 'Жири': '3г', 'Насичені жирні кислоти': '1г', 'Цукор': '7г', 'Целюлоза': '0г', 'Білки': '5г', 'Сіль': '0.2г'}, 'Гарячий')

cappuccino = Beverages('Капучино', 55, 'Ароматний капучино. Гарячий еспресо, молоко і молочна піна.'
                    ' Бенкет для очей. Перед подачею декорують обраним візерунком.'
                    ' Ніжний смак, яким можна побалувати себе в будь-який час.', [],
                    {'Енергія': '159 ккал', 'Жири': '2г', 'Насичені жирні кислоти': '1г', 'Цукор': '3г', 'Целюлоза': '0г', 'Білки': '2г', 'Сіль': '0.1г'}, 'Гарячий')

Tea = Beverages('Чай', 39, 'Виберіть улюблений смак чаю. За бажанням замовника ми можемо подати чай з цукром.', [], {}, 'Гарячий')

iced_coffee_with_ice_cream = Beverages('Кава з льодом з морозивом', 65, 'Кава з неабиякою порцією морозива.'
                                    ' Доза кави і води точно вимірюється автоматом.'
                                    ' Кава з льодом подається з цукром, вершками.', [],
                                       {'Енергія': '638 ккал', 'Жири': '4г', 'Насичені жирні кислоти': '2.7г', 'Цукор': '25г', 'Целюлоза': '0г', 'Білки': '3.9г', 'Сіль': '0.15г'}, 'Гарячий')


cheese_bagel_fresh_luchina = Breakfast('Сирний бублик Фреш Лучина', 85, 'Почніть свій день зі смачного бублика з вершковою Люциною,'
                            ' скибочками чеддера, свіжою руколою і помідором.', ['Бублик', 'Пасовища', 'Лист чеддера', 'Свіжі помідори', 'Руколла'],
                             {'Енергія': '1596 ккал', 'Жири': '14г', 'Насичені жирні кислоти': '7.3г', 'Цукор': '49г', 'Целюлоза': '2.7г', 'Білки': '15г', 'Сіль': '1.7г'}, 'Бублики і бургери')

egg_bagel = Breakfast('Яєчний бублик', 75, 'Для любителів хороших і ситних сніданків.'
                                        ' Бублик з яєчнею, сиром і хрустким беконом.', ["Бублик", "Лист чеддера", "Яйце", "Шинка", "Бекон", "Масло", "Сіль", "Перець"],
                                       {'Енергія': '1831 ккал', 'Жири': '18г', 'Насичені жирні кислоти': '7.4г', 'Цукор': '43г', 'Целюлоза': '3г', 'Білки': '25г', 'Сіль': '2.09г'}, 'Бублики і бургери')

Mc_Country_breakfast = Breakfast('Сніданок Маккантрі', 85, 'Правильний сніданок?'
                    ' Це бургер з двома скибочками свинини, чеддером і популярним соусом DeLuxe.', ['Свинина', 'Булочки з насінням кунджуту,', 'Лист чеддера', 'Свіжі помідори', 'Соус делюкс', 'Салат айсберг'],
                      {'Енергія': '2193 ккал', 'Жири': '33г', 'Насичені жирні кислоти': '12.2г', 'Цукор': '33г', 'Целюлоза': '2.8г', 'Білки': '22г', 'Сіль': '2.6г'}, 'Бублики і бургери')

pork_bagel = Breakfast('Бублик зі свинини', 85, 'Правильний бублик робить день!'
                        ' Приходьте в знаменитий бублик зі свининою, беконом і чеддером.', ['Свинина', 'Бекон', 'Лист челлера', 'Бублик', 'Соус делюкс'],
                       {'Енергія': '2382 ккал', 'Жири': '32г', 'Насичені жирні кислоти': '13г', 'Цукор': '43г', 'Целюлоза': '3.4г', 'Білки': '27г', 'Сіль': '2.7г'}, 'Бублики і бургери')

egg_McMuffin_fresh = Breakfast('Яйце Макмаффін фреш', 59, 'Зробіть ставку на це смажене яйце з руколою та чеддером в англійській здобі,'
                                ' яка зробить вас трохи краще вранці.', ["Бублик", "Пасовища", "Лист чеддера", "Свіжі помідори", "Руколла"],
                               {'Енергія': '1209 ккал', 'Жири': '13г', 'Насичені жирні кислоти': '6.4г', 'Цукор': '26г', 'Целюлоза': '1.6г', 'Білки': '16г', 'Сіль': '1.2г'}, 'Макмаффіни і тости')

Mc_Muffin_with_egg = Breakfast('Макмаффін з яйцем', 52, 'Ласкаво просимо до ранку!'
                                ' Смажене яйце в теплому бутерброді з сиром зробить ваш початок дня приємніше.', ["Англійська здоба", "Лист чеддера", "Яйце", "Масло"],
                               {'Енергія': '1831 ккал', 'Жири': '18г', 'Насичені жирні кислоти': '7.4г', 'Цукор': '43г', 'Целюлоза': '3г', 'Білки': '25г', 'Сіль': '2.09г'}, 'Макмаффіни і тости')

pork_McMuffin_with_egg = Breakfast('Свинячий макмаффін з яйцем', 69, 'Ситний сніданок!'
                                ' Яєчня в теплому бутерброді з сиром зробить ваш початок дня приємніше.', ["Свинина", "Англійська здоба", "Лист чеддера", "Яйце", "Масло"],
                                {'Енергія': '1593 ккал', 'Жири': '21г', 'Насичені жирні кислоти': '8.9г', 'Цукор': '26г', 'Целюлоза': '1.8г', 'Білки': '21г', 'Сіль': '1.7г'}, 'Макмаффіни і тости')

Mc_Muffin_with_egg_and_bacon = Breakfast('Макмаффін з яйцем і беконом', 69, 'Ароматний і хороший сніданок.'
                                        ' Смажене яйце, смачний бекон і сир в теплому бутерброді.', ["Бекон", "Англійська здоба", "Лист чеддера", "Яйце", "Масло" ],
                                         {'Енергія': '1327 ккал', 'Жири': '15г', 'Насичені жирні кислоти': '6.8г', 'Цукор': '26г', 'Целюлоза': '1.9г', 'Білки': '18г', 'Сіль': '1.3г'}, 'Макмаффіни і тости')

scrambled_eggs_with_ham_and_cheese = Breakfast('Яєчня з шинкою і сиром', 79, 'Традиційний рецепт. Яєчня з шинкою і сиром.'
                                                ' Подавати з ароматним, розтопленим вершковим маслом, змащеним солоною здобою.'
                                                ' Сіль і перець за смаком подаються окремо в одноразовому пакеті.', ["Англійська здоба", "Яйце", "Масло", "Шинка", "Третій чеддер"],
                                               {'Енергія': '2607 ккал', 'Жири': '39г', 'Насичені жирні кислоти': '14г', 'Цукор': '26г', 'Целюлоза': '2.2г', 'Білки': '41г', 'Сіль': '2.7г'}, 'Макмаффіни і тости')

proper_breakfast = Breakfast('Правильний сніданок', 135, 'Яєчня з шинкою, двома свининами і солоною здобою.'
                            ' Правильний сніданок, як і годиться.', ["Англійська здоба", "Яйце", "Масло", "Шинка", "Третій чеддер", "Свинина"],
                             {'Енергія': '445 ккал', 'Жири': '18г', 'Насичені жирні кислоти': '4.2г', 'Цукор': '29.6г', 'Целюлоза': '2г', 'Білки': '13г', 'Сіль': '1.2г'}, 'Макмаффіни і тости')

chicken_McMuffin_fresh = Breakfast('Курячий Макмаффін Фреш', 69, 'Чудовий смак! Свіжі овочі, шматочок курки і сиру в теплому бутерброді. Супроводжується майонезним соусом. Смачний і чесний сніданок.',
                                   ["Куриця", "Салат айсберг", "Англійська здоба", "Лист чеддера", "Свіжі помідори", "Сендвіч-соус"],
                                   {'Енергія': '1551 ккал', 'Жири': '17г', 'Насичені жирні кислоти': '5г', 'Цукор': '38г', 'Целюлоза': '3г', 'Білки': '16г', 'Сіль': '1.8г'}, 'Макмаффіни і тости')

McMuffin_luchina = Breakfast('Макмаффін Лючіна', 65, 'Свіжий сир з редискою і руколою в пухнастому кексі ідеально підходить для легкого початку дня.',
                             ["Англійська здоба", "Масло", "Руколла", "Редька", "Пасовища"],
                             {'Енергія': '1014 ккал', 'Жири': '10г', 'Насичені жирні кислоти': '4.6г', 'Цукор': '27г', 'Целюлоза': '2.3г', 'Білки': '9.2г', 'Сіль': '1.3г'}, 'Макмаффіни і тости')

pork_McMuffin_fresh = Breakfast('Свинина Макмаффін Фреш', 75, 'Чудовий смак!'
                                ' Свіжі овочі, шматочок свинини і сиру в теплому бутерброді.'
                                ' Супроводжується гострим соусом.', ["Англійська здоба", "Руколла", "Редька", "Салат айсберг", "Свіжі помідори", "Соус делюкс"],
                                {'Енергія': '1452 ккал', 'Жири': '19г', 'Насичені жирні кислоти': '7.6г', 'Цукор': '27г', 'Целюлоза': '2.2г', 'Білки': '15.5г', 'Сіль': '1.8г'}, 'Макмаффіни і тости')

toast_with_cheese = Breakfast('Тост з сиром', 39, 'Швидкий і смачний сніданок. Пшенична булочка, запечена з сиром.', ["Пшенична булочка", "Лист чеддера"],
                              {'Енергія': '1027 ккал', 'Жири': '9.9г', 'Насичені жирні кислоти': '5.7г', 'Цукор': '28г', 'Целюлоза': '1.5г', 'Білки': '10г', 'Сіль': '1.4г'}, 'Макмаффіни і тости')

toast_with_ham_and_cheese = Breakfast('Тост з шинкою і сиром', 42, 'Швидкий і смачний сніданок.'
                                    ' Шинку і сир запікають в пшеничній булочці.'
                                    ' Для цього народжується чай або кава і ідеальний легкий сніданок.', ["Пшенична булочка", "Лист чеддера", "Колбаса із свинини"],
                                      {'Енергія': '1086 ккал', 'Жири': '10.3г', 'Насичені жирні кислоти': '5.8г', 'Цукор': '28г', 'Целюлоза': '1.6г', 'Білки': '13г', 'Сіль': '1.7г'}, 'Макмаффіни і тости')

toast_with_ham_bacon_cheese = Breakfast('Тост з беконом і сиром', 42, 'Швидкий і смачний сніданок.'
                                        ' Бекон і сир, запечені в пшеничній булочці.', ["Пшенична булочка", "Лист чеддера", "Бекон"],
                                        {'Енергія': '1288 ккал', 'Жири': '15г', 'Насичені жирні кислоти': '8г', 'Цукор': '28г', 'Целюлоза': '1.5г', 'Білки': '14г', 'Сіль': '1.9г'}, 'Макмаффіни і тости')

pancakes = Desserts("Млинці з Прібіначеком і глазур'ю", 69, "Пухнасті млинці з вершковим прібіначеком і шоколадною глазур'ю поліпшать ранок для всіх любителів солодких сніданків.",
                     ["Млинці", "Прібіначек", "Шоколадна глазур"],
                     {'Енергія': '1593 ккал', 'Жири': '20г', 'Насичені жирні кислоти': '8.5г', 'Цукор': '42г', 'Целюлоза': '1г', 'Білки': '9.2г', 'Сіль': '0.86г'})

butter_croissant = Desserts('Круасан вершковий', 45, 'Відмінна французька випічка.'
                            ' Круасан з маслянистим смаком.'
                            ' Можна додати варення або Нутеллу.'
                            ' Для тих, хто любить солодкий сніданок.', [],
                             {'Енергія': '832 ккал', 'Жири': '10г', 'Насичені жирні кислоти': '6.5г', 'Цукор': '22г', 'Целюлоза': '1.7г', 'Білки': '4.5г', 'Сіль': '0.63г'})


hamburger.add_product_()
cheeseburger.add_product_()
crispy_bacon_McWrap.add_product_()
grilled_italian_McWrap.add_product_()
single_big_tasty_chicken.add_product_()
McChicken.add_product_()
tasty_chicken.add_product_()
chicken_burger.add_product_()
chicken_McNuggets.add_product_()
chicken_strips.add_product_()
snack_wrap.add_product_()
fried_cheese_fresh.add_product_()
veggie_wrap.add_product_()
veggie_salad.add_product_()
veggie_burger.add_product_()
crispy_chicken_salad.add_product_()
grilled_chicken_salad.add_product_()
garden_salad.add_product_()
McShakerFries.add_product_()
camembert.add_product_()
french_fries.add_product_()
cheese_king_sauce.add_product_()
ketchup.add_product_()
pommes_frites_sauce.add_product_()
sweet_and_sour_sauce.add_product_()
hellmann_s_tartar_sauce.add_product_()
barbecue_sauce.add_product_()
curry_sauce.add_product_()
mustard_sauce.add_product_()
lemon_chili.add_product_()
caesar_grout.add_product_()
cocktail_dressing.add_product_()
yogurt_dressing.add_product_()
cheese_dressing.add_product_()
balsamic.add_product_()
olive_oil.add_product_()
pastry_chocolate_and_salted_caramel.add_product_()
McFlurry_oreo.add_product_()
McFlurry.add_product_()
McSundae_caramel.add_product_()
McSundae_chocolate.add_product_()
McSundae_strawberry.add_product_()
grand_McSundae_chocolate.add_product_()
grand_McSundae_caramel.add_product_()
grand_McSundae_strawberry.add_product_()
ice_cream_in_cone.add_product_()
milk_shake_with_vanilla_flavour.add_product_()
milk_shake_with_strawberry_flavour.add_product_()
milk_shake_with_chocolate_flavour.add_product_()
shake_deluxe_with_vanilla_whipped_cream.add_product_()
shake_deluxe_with_strawberry_whipped_cream.add_product_()
shake_deluxe_with_whipped_cream_chocolate.add_product_()
apple_pastry.add_product_()
fruit_mix.add_product_()
coca_cola.add_product_()
fanta.add_product_()
coca_cola_zero.add_product_()
coca_cola_zero_cinnamon.add_product_()
sprite.add_product_()
lipton_ice_tea_lemon.add_product_()
kitl_raspberry.add_product_()
vinea.add_product_()
soda_water.add_product_()
orange_juice.add_product_()
apple_juice.add_product_()
pilsner_urquell.add_product_()
still_water.add_product_()
gently_sparkling_water.add_product_()
espresso.add_product_()
double_espresso.add_product_()
coffee.add_product_()
coffee_with_milk.add_product_()
espresso_grande.add_product_()
latte.add_product_()
cappuccino.add_product_()
Tea.add_product_()
iced_coffee_with_ice_cream.add_product_()
cheese_bagel_fresh_luchina.add_product_()
egg_bagel.add_product_()
pork_bagel.add_product_()
Mc_Country_breakfast.add_product_()
egg_McMuffin_fresh.add_product_()
Mc_Muffin_with_egg.add_product_()
pork_McMuffin_with_egg.add_product_()
Mc_Muffin_with_egg_and_bacon.add_product_()
scrambled_eggs_with_ham_and_cheese.add_product_()
proper_breakfast.add_product_()
chicken_McMuffin_fresh.add_product_()
McMuffin_luchina.add_product_()
pork_McMuffin_fresh.add_product_()
toast_with_cheese.add_product_()
toast_with_ham_and_cheese.add_product_()
toast_with_ham_bacon_cheese.add_product_()
pancakes.add_product_()
butter_croissant.add_product_()

sauces = filter(lambda x: type(x) == SaucesAndDressings, all_products)
sauce_names_list = []

for i in sauces:
    sauce_names_list.append(i.name)


while order_status == False:
    ordering = input("Що ви б хотіли замовити --> ")
    for i in all_products:
        if i.name == ordering:
            if i.name in ('Макшакер Фрі', 'Курячі мак-наггетси', 'Курячі стріпси', 'Картопля фрі', 'Камамбер'):
                sauce = input("Бажаєте соус? (y/n) ")
                if sauce == 'y':
                    for j in sauce_names_list:
                        print(j, "\n")
                    sauce_name = input("Оберіть будь-який запропонований соус безкоштовно --> ")
                    i.name += f"+ {sauce_name}"
            total_cost, your_order, amount = prepare_order(your_order, i, total_cost)
            push = input('Прибрати цей предмет? (y/n) ')
            if push == 'y':
                while push == 'y':
                    total_cost -= i.price * amount
                    your_order.pop()
                    print('Цей предмет прибранний')
                    print_order(your_order)
                    print(f"Ваше замовлення буде коштувати вам {total_cost}")
                    push = input('Прибрати цей предмет? (y/n) ')
                    if push == 'n':
                        break
            is_over = input("Ви б хотіли б додати щось? (y/n) ")
            if is_over == 'n':
                print(f"Ваше замовлення буде коштувати вам {total_cost}")
                print("Дякуємо за замовлення в McDonald's!")
                order_status = True
                break

# Салат з курки гриль, МакЧікен