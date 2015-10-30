__author__ = 'vasiliy'
"""
    в базе в таблице нажатий фактически хранятся отпускания,
    а в таблице отпусканий - нажатия.
    Прескорбнейшая оплошность, но легко поправимая :)
"""


import sqlite3
from models import Unit, KEY_PRESS_UNIT_TYPE, KEY_RELEASE_UNIT_TYPE, Input

class Provider():
    """
    предоставляет набор методов для получения данных из базы
    """
    def __init__(self, connection_string):
        self.__connection_string = connection_string

    def get_all_subjects(self):
        """
        возвращает список идентификаторов всех субъектов
        """
        try:
            connection = sqlite3.connect(self.__connection_string)
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM research_work_subject")
            return [ tuple[0] for tuple in cursor.fetchall() ]

        except Exception as e:
            print(e)
        finally:
            connection.close()

    def get_all_units_by_subject_id(self, subject_id):
        """
        возвращает список, отсортированных по дате создания, всех юнитов конкретного пользователя
        """
        try:
            connection = sqlite3.connect(self.__connection_string)
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT key, time
                    FROM research_work_keypresstime AS kp_time,
                         (SELECT id
                            FROM research_work_pack AS pack
                            WHERE pack.subject_id = ?) AS pack
                    WHERE kp_time.pack_id = pack.id
                """,
                (subject_id,)
            )
            #интерпретируем эти юниты как отпускания
            result_seq = [ Unit(unit[1], unit[0], unit_type=KEY_RELEASE_UNIT_TYPE) for unit in cursor.fetchall() ]

            cursor.execute(
                """
                SELECT key, time
                    FROM research_work_keyreleasetime AS kr_time,
                         (SELECT id
                            FROM research_work_pack AS pack
                            WHERE pack.subject_id = ?) AS pack
                    WHERE kr_time.pack_id = pack.id
                """,
                (subject_id,)
            )
            #интерпретируем эти юниты как нажания
            result_seq += [ Unit(unit[1], unit[0], unit_type=KEY_PRESS_UNIT_TYPE) for unit in cursor.fetchall() ]
            result_seq.sort(key=(lambda x: x.time_stamp))
            return result_seq

        except Exception as e:
            print(e)
        finally:
            connection.close()

