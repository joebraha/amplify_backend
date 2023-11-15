# from auth import User, Group, Permission

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.engine import URL
# import psycopg2

engine = create_engine("postgresql+psycopg2://postgres:16684ccc@localhost/Amplify") # needs to be fixed

# conn_string = "host='localhost' dbname='Amplify' user='postgres' password='16684ccc'"
# conn = psycopg2.connect(conn_string)

meta = MetaData()

songs = Table(
   'songs', meta, 
   Column('song_name', String, primary_key = True), 
   Column('length', String), 
   Column('user_id', Integer, ForeignKey('user.user_id'), primary_key = True), 
   Column('genre', String), 
)

music_generator = Table(
   'music_generator', meta, 
   Column('key_words', String, primary_key = True), 
   Column('user_id', Integer, ForeignKey('songs.user_id'),primary_key = True), 
   Column('genres', String), 
   Column('streaming_service_info', String), 
)

user = Table(
   'user', meta, 
   Column('user_id', Integer, primary_key = True), 
   Column('email', String), 
   Column('library_id', Integer, ForeignKey('music_library.user_id')), 
   Column('phone_number', String), 
)

streaming_service = Table(
   'streaming_service', meta, 
   Column('user_id', Integer, ForeignKey('user.user_id'), primary_key = True), 
   Column('email', String), 
   Column('service_songs', String), 
   Column('service_password', String), 
   Column('service_username', String), 
   Column('service_name', String,primary_key = True), 
)  

music_library = Table(
   'music_library', meta, 
   Column('songs', Integer), 
   Column('storage_used', String), 
   Column('user_id', Integer,ForeignKey('user.user_id'), primary_key = True,), 
   Column('storage_left', String), 
)  

meta.create_all(engine)

