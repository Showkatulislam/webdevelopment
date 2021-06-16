number="+8801850314705"

import phonenumbers

from phonenumbers import carrier

from phonenumbers import geocoder

from phonenumbers.util import prnt 
from phonenumbers import ph

c_number=phonenumbers.parse(number,"CH")

print('helll')

print(geocoder.description_for_number(c_number,"en"))

service_provide=phonenumbers.parse(number,'R')
print(carrier.name_for_number(service_provide,'en'))