__author__ = 'vasiliy'

from db_provider import Provider
from  models import Unit, KEY_PRESS_UNIT_TYPE, KEY_RELEASE_UNIT_TYPE
from chapter_one.utils import getKeyActivationSequenceFromUnitSequence, getAverage
import matplotlib.pyplot as plt

provider = Provider("database/research_db.sqlite3")
"""
subjects = provider.getAllSubjects()

for subject in subjects:
    avr = getAverage(
        getKeyActivationSequenceFromUnitSequence(
            provider.getAllUnitsBySubjectId(
                subject
            )
        )
    )
    plt.plot(list(avr.keys()), list(avr.values()), 'x')
plt.show()
"""
acts = getKeyActivationSequenceFromUnitSequence(
    provider.getAllUnitsBySubjectId(
        10
    )
)
keys = []
dur = []
for act in acts:
    keys.append(act.key)
    dur.append(act.activity_duration)
plt.plot(keys, dur, 'x')
plt.show()

