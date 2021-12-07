import random
import string

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




def unique_code_generator(instance, new_code=None):
    if new_code is not None:
        code = new_code
    else:
        code = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(code=code).exists()
    if qs_exists:
        randstr = random_string_generator(size=4)
        code=code
        new_code= f'{code}-{randstr}'
        return unique_code_generator(instance, new_code=new_code)
    return code
