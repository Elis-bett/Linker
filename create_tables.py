from database.models import Links
from database.session import engine

Links.metadata.create_all(bind=engine)

