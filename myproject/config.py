import os
dir=os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(dir,'pybo.db'))
#DB위치는 flask db run을 수행한 즉 migrations 폴더가 있는 곳
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY = "dev"