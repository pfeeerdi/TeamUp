from app import db
from app.model import *
from app.service.user_service import *
import datetime
import random
from sqlalchemy import text

def saveAllToDB(data):
    db.session.add_all(data)
    db.session.commit()


def createUsers():
    try:
        register(username="ChefBesos", email="jeffbezos@gmail.com", lastName="Besos", firstName="Chef", password="Passwort123!", birthdate=str(datetime.datetime.today() - datetime.timedelta(days=20*365)))
        register(username="EronMisk", email="eronmisk@gmail.com", lastName="Misk", firstName="Eron", password="Passwort123!", birthdate=str(datetime.datetime.today() - datetime.timedelta(days=21*365)))
        register(username="billyShorts", email="billgates@gmail.com", lastName="Gates", firstName="Jill I'm Single", password="Passwort123!", birthdate=str(datetime.datetime.today() - datetime.timedelta(days=22*365)))
        register(username="Max", email="max@gmail.com", lastName="Mustermann", firstName="Max", password="Passwort123!", birthdate=str(datetime.datetime.today() - datetime.timedelta(days=23*365)))
        register(username="Herbert", email="herbert@gmail.com", lastName="Herbert", firstName="Herbert", password="Passwort123!", birthdate=str(datetime.datetime.today() - datetime.timedelta(days=90*365)))
        print('added: users')
    except Exception as e:
        print(e)

# def create_view():
#     last_posts = text("CREATE VIEW last_10_posts AS SELECT * FROM posts LIMIT 10;")
#     db.engine.execute(last_posts)
#     last_trades = text("CREATE VIEW last_10_trades AS SELECT * FROM trades LIMIT 10;")
#     db.engine.execute(last_trades)
#     print('added: view')
#
# def create_procedure():
#     new_follow = text("CREATE PROCEDURE new_follow(src_user integer, tgt_user integer) LANGUAGE SQL AS $$ INSERT INTO followers VALUES (src_user, tgt_user); $$;")
#     delete_follow = text("CREATE PROCEDURE delete_follow(src_user integer, tgt_user integer) LANGUAGE SQL AS $$ DELETE FROM followers WHERE follower_id = src_user AND followed_id = tgt_user; $$;")
#     db.engine.execute(new_follow)
#     db.engine.execute(delete_follow)
#     print('added: procedure')

def generate():
    createUsers()
    # create_view()
    # create_procedure()
