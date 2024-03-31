base_number = 16
prime_number = 541
a = 7
b = 12

def calculate_public_key(party_name, base_number, chosen_number, prime_number):
    print(f'Public key for {party_name} is (base number ^ chosen number) mod prime number')
    print(f'For party {party_name}, this will be ({base_number} ^ {chosen_number}) mod {prime_number}')
    base_number_exponent_chosen_number = base_number ** chosen_number
    print(f'Base number ^ chosen number = {base_number_exponent_chosen_number}')
    public_key = base_number_exponent_chosen_number % prime_number
    print(f'Public key = {base_number_exponent_chosen_number} mod {prime_number} = {public_key}')
    return public_key

public_key_a = calculate_public_key(party_name='A', base_number=base_number, chosen_number=a, prime_number=prime_number)
public_key_b = calculate_public_key(party_name='B', base_number=base_number, chosen_number=b, prime_number=prime_number)

def calculate_secret_key(party_name_one, party_name_two, public_key, chosen_number, prime_number):
    print(f'The secret key for party {party_name_one} will be (public key for party {party_name_two} ^ chosen number) mod {prime_number}')
    print(f'({public_key} ** {chosen_number}) mod {prime_number}')
    public_key_exponent_chosen_number = public_key ** chosen_number
    print(f'Secret key = {public_key_exponent_chosen_number} mod {prime_number} = {public_key_exponent_chosen_number % prime_number}')

calculate_secret_key(party_name_one='A', party_name_two='B', public_key=public_key_b, chosen_number=a, prime_number=prime_number)
calculate_secret_key(party_name_one='B', party_name_two='A', public_key=public_key_a, chosen_number=b, prime_number=prime_number)


