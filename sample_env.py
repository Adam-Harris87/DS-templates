user = 'your_user_name'
password = 'your_password'
host = 'data.youWant.com'

def get_db_url(db_name, host=host, user=user, password=password):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url