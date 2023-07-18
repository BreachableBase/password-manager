# imports
from Cryptodome.PublicKey import RSA
from client_side import generate_user
import os
# constants

# functions
# THIS FUNCTION IS FUTILE. WILL BE REMOVED WHEN SQL IS INTRODUCED.
def check_user_unique():
    new_user = generate_user()
    users_path = r'/home/kali/vsc/projects/password_manager/users/'
    if not os.path.exists(users_path+new_user):
        user_id_path = os.makedirs(users_path+new_user)
    return user_id_path



def generate_user_key():
    pass

check_user_unique()





















