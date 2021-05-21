from app import db
from app.model import *
from app.service.user_service import *
from app.service.team_service import *
from app.service.survey_service import *
import datetime
import random
from sqlalchemy import text

def saveAllToDB(data):
    db.session.add_all(data)
    db.session.commit()


def createUsers():
    try:
        register(username="ChefBesos", email="jeffbezos@gmail.com", lastName="Besos", firstName="Chef", password="Passwort123!")
        register(username="EronMisk", email="eronmisk@gmail.com", lastName="Misk", firstName="Eron", password="Passwort123!")
        register(username="billyShorts", email="billgates@gmail.com", lastName="Gates", firstName="Jill I'm Single", password="Passwort123!")
        register(username="Max", email="max@gmail.com", lastName="Mustermann", firstName="Max", password="Passwort123!")
        register(username="Test1", email="demo@test.de", lastName="Test", firstName="Test2", password="Test")
        print('added: users')
    except Exception as e:
        print(f"Following Error while running createUsers() from generate.py: \n{e}")


def createTeams():
    try:
        add_team("Test-Team#1", 1)
        add_team("Test-Team#2", 2)
        print("Teams added")
        #print([i for i in User.query.all()])
    except Exception as e:
        print(f"Following Error while running createTeams() from generate.py: \n{e}")

def createSurveys():
    try:
        add_survey(1, 2, "This is a question")
        add_survey(2, 1, "This is the second question")
        print("Surveys added")
        add_survey_option({1: "Option #1", 2: "Option #1"}, 1)
    except Exception as e:
        print(f"Following Error while running createSurveys() from generate.py: \n{e}")
# def create_view():
#     last_posts = text("CREATE VIEW last_10_posts AS SELECT * FROM posts LIMIT 10;")
#     db.engine.execute(last_posts)
#     last_trades = text("CREATE VIEW last_10_trades AS SELECT * FROM trades LIMIT 10;")
#     db.engine.execute(last_trades)
#     print('added: view')
#

def create_procedures():
    try:
        new_teammember = text("CREATE PROCEDURE new_teammember(team_id integer, user_id integer) LANGUAGE SQL AS $$ INSERT INTO teammembers VALUES (team_id, user_id); $$;")
        db.engine.execute(new_teammember)
        new_survey = text("CREATE PROCEDURE new_survey(survey_id integer, team_id integer) LANGUAGE SQL AS $$ INSERT INTO teamsurveys VALUES (survey_id, team_id); $$;")
        db.engine.execute(new_survey)
        new_survey_vote = text("CREATE PROCEDURE new_survey_vote(survey_id integer, some_option char(200), user_id integer) LANGUAGE SQL AS $$ INSERT INTO survey_votes VALUES (survey_id, some_option, user_id); $$;")
        db.engine.execute(new_survey_vote)
    except Exception as e:
        print(f"Following Error while running create_procedures() from generate.py: \n{e}")

def create_sequence_and_triggers():
    try:
        sequence = text("""CREATE SEQUENCE table_teammembers_log_id_seq;""")
        table_teammembers_log = text("""CREATE TABLE teammembers_log (log_id INTEGER NOT NULL DEFAULT nextval('table_teammembers_log_id_seq'), team_id INTEGER NOT NULL, user_id INTEGER NOT NULL, date timestamp without time zone NOT NULL, action_type varchar NOT NULL, PRIMARY KEY (log_id), FOREIGN KEY (team_id) REFERENCES public.teams (team_id) MATCH SIMPLE, FOREIGN KEY (user_id) REFERENCES public.users (user_id) MATCH SIMPLE );""")
        procedure_new_teammember = text("""CREATE OR REPLACE FUNCTION trigger_new_teammember() RETURNS trigger AS $$ BEGIN INSERT INTO teammembers_log (team_id, user_id, date, action_type) VALUES (NEW.team_id, NEW.user_id, now(), 'Added user to team'); RETURN NEW; END; $$ LANGUAGE 'plpgsql';""")
        trigger_new_teammember = text("""CREATE TRIGGER trigger_new_teammember AFTER INSERT ON teammembers FOR EACH ROW EXECUTE PROCEDURE trigger_new_teammember();""")
        db.engine.execute(sequence)
        db.engine.execute(table_teammembers_log)
        db.engine.execute(procedure_new_teammember)
        db.engine.execute(trigger_new_teammember)
        print('added: procedure')
    except Exception as e:
        print(f"Following Error while running create_procedures_and_triggers() from generate.py: \n{e}")

def create_view():
    last_appointments = text("CREATE VIEW last_10_appointments AS SELECT * FROM appointments LIMIT 10;")
    db.engine.execute(last_appointments)
    print('added: view')

def generate():
    create_procedures()
    create_sequence_and_triggers()
    createUsers()
    createTeams()
    create_view()
    createSurveys()
    db.session.commit()

