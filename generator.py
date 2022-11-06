#generator password

import string, secrets

chrs = string.ascii_letters + string.digits

password = ''.join(secrets.choice(chrs) for i in range(10))

print('Ваш сгенерированный пароль:', password)