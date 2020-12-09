import sys
import os
import datetime
from flask_app import app, mongodb, db, current_app
from models.sqlacodegen_models import Place, Location
from helper import get_local_functions


def import_from_old_db():
    # engine_db2 = db.get_engine(current_app, 'db2')
    # results = engine_db2.execute("select * from places")
    # for result in results:
    #     place = Place(
    #         name=result["name"],
    #         htaccess=result["htaccess"],
    #         short_text=result["short_text"],
    #         loc_id=result["loc_id"],
    #         description=result["description"],
    #         latitude=result["latitude"],
    #         longitude=result["longitude"],
    #         status=result["status"],
    #     )
        # results2 = engine_db2.execute("select * from locations limit 1").first()
        # place.save()
        # db.session.add( place )
        # db.session.commit()

    # db.session.commit()


print(get_local_functions(locals(), __name__))
if __name__ == '__main__' and len(sys.argv) > 1:
    with app.app_context():
        globals()[sys.argv[1]]()
