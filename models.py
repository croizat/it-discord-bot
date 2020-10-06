from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, Unicode
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_json import NestedMutableJson, MutableJson
import configparser

config = configparser.SafeConfigParser()
config.read('config.ini')
user = config.get('MYSQL', 'USER')
passwd = config.get('MYSQL', 'PASSWD')
host = config.get('MYSQL', 'HOST')
database = config.get('MYSQL', 'DATABASE')

Base = declarative_base()


class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True, unique=True)
    message = Column(Unicode(2000))
    channel = Column(BigInteger)
    time = Column(BigInteger)
    interval = Column(Integer)

    mysql_charset = 'utf8mb4'

    def __repr__(self):
        return '<Reminder "{}" <#{}> {}s>'.format(self.message, self.channel, self.time)


class Server(Base):
    __tablename__ = 'servers'

    map_id = Column(Integer, primary_key=True)
    id = Column(BigInteger, unique=True)
    prefix = Column(String(5))
    language = Column(String(2))
    timezone = Column(String(30))
    blacklist = Column(NestedMutableJson)
    restrictions = Column(NestedMutableJson)
    tags = Column(MutableJson)
    autoclears = Column(MutableJson)

    def __repr__(self):
        return '<Server {}>'.format(self.id)


engine = create_engine(
    'mysql+pymysql://{user}:{passwd}@{host}/{db}?charset=utf8mb4'.format(user=user, passwd=passwd, host=host, db=database))
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
