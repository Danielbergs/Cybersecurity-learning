import secrets
import string 

punctuation = string.punctuation
digits = string.digits 
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

all_pools = punctuation + digits + lowercase + uppercase

length = input("How many symbols do you want your password to be?")
length = int(length)

if length < 8:
        raise ValueError("Password length must be at least 8 characters.")      

password_list = [secrets.choice(punctuation), 
secrets.choice(digits), secrets.choice(lowercase), secrets.choice(uppercase)]


for _ in range (length - 4):
    password_list.append(secrets.choice(all_pools))

secrets.SystemRandom().shuffle(password_list)

password = "".join(password_list)

print (f"This is your new password with {length} symbols.")
print (password)
