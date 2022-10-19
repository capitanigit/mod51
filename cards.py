#Mod 5 Zad 1
print("Mod 5 zad 1") 
print()

from faker import Faker
temp = Faker(locale="pl_PL")


class BaseContact:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

        self._label_length = len(f'{self.first_name} {self.last_name}')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self._label_length} {self.email} {self.phone}'

    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}'

    @property
    def label_length(self):
        return self._label_length


class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone

        self._label_length = len(f'{self.first_name} {self.last_name}')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self._label_length} {self.email} {self.phone} {self.position} {self.company} {self.business_phone}'
    
    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}'
    

    @property
    def label_length(self):
        return self._label_length

def create_contacts(category, cards_number):
    temp_card_list = []
    for _ in range(int(cards_number)):
        if category == '1':
            card = BaseContact(first_name=temp.first_name(), last_name=temp.last_name(), email=temp.email(), phone=temp.phone_number())
        elif category == '2':
            card = BusinessContact(first_name=temp.first_name(), last_name=temp.last_name(), email=temp.email(), phone=temp.phone_number(), position=temp.job(), company=temp.company(), business_phone=temp.phone_number())
        temp_card_list.append(card)
    return temp_card_list

if __name__ == "__main__":
    cards_number = input("Liczba wizytówek: ")
    cat_number = input("Rodzaj wizytówki (1-BaseContact, 2-BusinessContact): ")
    while cat_number not in {"1", "2"}:
            cat_number = input("Niepoprawna wartość, podaj liczbę 1 lub 2: ")
    card_list = create_contacts(cat_number, cards_number)
    for i in card_list:
        print(i.contact())
    for i in card_list:
        print(i)