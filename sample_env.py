# you will need to change these variables to your own username and password
# along with the hostname of the sql server that you are connecting to
user = 'your_user_name'
password = 'your_password'
host = 'data.youWant.com'

def get_db_url(db_name, host=host, user=user, password=password):
    '''
    This will return a connection url string for connecting to the specified sql server
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'