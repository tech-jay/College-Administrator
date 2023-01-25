import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919000543234")
phone_number2 = phonenumbers.parse("+917997136315")

print("PhoneNumbers Location")
print(geocoder.description_for_number(phone_number1,"te"));
print(geocoder.description_for_number(phone_number2,"te"));
