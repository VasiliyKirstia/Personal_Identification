__author__ = 'vasiliy'

from db_provider import Provider
from  models import Unit

provider = Provider("database/research_db.sqlite3")
i = 0;
for unit in provider.getAllUnitsBySubjectId(4):
    print(unit)
    i += 1
    if i > 1000:
        break