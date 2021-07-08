from .base import *

# docker secret 변수 불러오기
def read_secret(secretName):
    file = open('/run/secrets/' + secretName)
    secret = file.read()
    secret = secret.rstrip().lstrip()  # 좌우에 불필요한 공백 제거
    file.close()
    return secret


environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env("SECRET_KEY")
SECRET_KEY = read_secret("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["*"]   # "*" 모든 경로에서 접속 가능

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        # 'USER': 'django',
        # 'PASSWORD': 'password1234',
        'PASSWORD': read_secret('MYSQL_ROOT_PASSWORD'), # docker secret에 저장한 변수 정보
        'HOST': 'mariadb',                              # 컨테이너에서 생성한 mariadb 이름
        'PORT': '3306',
    }
}

