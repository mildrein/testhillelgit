import jwt
import datetime
def generate_jwt_token():
    payload = {
        'my_name': 'Arkhip',
        'age': 10,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
    }
    encode_jwt = jwt.encode(
        payload=payload,
        key='pass',
        algorithm='HS256',
    )
    return encode_jwt

def main():
    token = generate_jwt_token()
    print(token)
if __name__ == "__main__":
    main()
