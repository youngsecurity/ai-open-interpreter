import jwt
import datetime

def create_jwt(subject, sub):
    # Define your secret key. Replace this with a secure key for production use
    SECRET_KEY = "my_super_secret_key"

    # Set the payload (claims) of the token
    payload = {
        'sub': sub,  # Subject
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),  # Expiration time
        'iat': datetime.datetime.utcnow(),  # Issued at time
    }

    # Sign the payload with the secret key to generate a JWT
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    # Decode and print the JWT for verification
    decoded_jwt = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])

    return decoded_jwt, jwt_token

subject1 = "user1"
sub1 = "12345"
decoded_jwt1, token1 = create_jwt(subject1, sub1)
print("Decoded JWT for user1:")
print(decoded_jwt1)

subject2 = "user2"
sub2 = "67890"
decoded_jwt2, token2 = create_jwt(subject2, sub2)
print("\nDecoded JWT for user2:")
print(decoded_jwt2)