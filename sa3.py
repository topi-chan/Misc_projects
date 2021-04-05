import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, create_engine
from sqlalchemy import MetaData, ForeignKey, inspect, delete
from sqlalchemy.sql import text


class SqlAlchemyCreate():
    """Allows to write a simple table; put database type/name in 'engine'"""

    def __init__(self, engine, table_name):
        self.engine = engine
        self.table_name = table_name

    def sql_create_test(self):
        metadata = MetaData()
        users = Table(self.table_name, metadata, Column('id', Integer))
        engine = create_engine(self.engine)
        metadata.create_all(engine)

    def sql_create_3col(self, column1, column2, type1, type2):
        metadata = MetaData()
        books = Table(self.table_name, metadata,
          Column('id', Integer),
          Column(column1, type1),
          Column(column2, type2),
        )
        engine = create_engine(self.engine)
        metadata.create_all(engine)


    def sql_create_4col_cstr(self, column1, type1, column2, type2,
    column3, type3, column4, type4):
        metadata = MetaData()
        books = Table(self.table_name, metadata,
          Column(column1, type1, primary_key=True, unique=True),
          Column(column2, type2, nullable=True),
          Column(column3, type3, nullable=True),
          Column(column4, type4, nullable=True),
        )
        engine = create_engine(self.engine)
        metadata.create_all(engine)


    def sql_create_5col_cstr(self, column1, type1, column2, type2,
    column3, type3, column4, type4, column5, type5):
        metadata = MetaData()
        books = Table(self.table_name, metadata,
          Column(column1, type1, primary_key=True),
          Column(column2, type2, nullable=False),
          Column(column3, type3, unique=True),
          Column(column4, type4, nullable=True),
          Column(column5, type5, nullable=True),
        )
        engine = create_engine(self.engine)
        metadata.create_all(engine)

    def sql_create_5col_cstr_2(self, column1, type1, column2, type2,
    column3, type3, column4, type4, column5, type5):
        metadata = MetaData()
        books = Table(self.table_name, metadata,
          Column(column1, type1, primary_key=True),
          Column(column2, type2, nullable=True),
          Column(column3, type3, nullable=True),
          Column(column4, type4, nullable=True),
          Column(column5, type5, nullable=True),
        )
        engine = create_engine(self.engine)
        metadata.create_all(engine)

    def sql_create_6col(self, column1, type1, column2, type2, column3, type3,
    column4, type4, column5, type5, column6, type6):
        metadata = MetaData()
        books = Table(self.table_name, metadata,
          Column(column1, type1),
          Column(column2, type2),
          Column(column3, type3),
          Column(column4, type4),
          Column(column5, type5),
          Column(column6, type6),
        )
        engine = create_engine(self.engine)
        metadata.create_all(engine)

    def sql_create_9col_cstr(self, column1, type1, column2, type2,
    column3, type3, column4, type4, column5, type5, column6, type6, column7,
    type7, column8, type8, column9, type9):
        metadata = MetaData()
        books = Table(self.table_name, metadata,
          Column(column1, type1, primary_key=True),
          Column(column2, type2, unique=False),
          Column(column3, type3, nullable=False),
          Column(column4, type4, nullable=True),
          Column(column5, type5, nullable=True),
          Column(column6, type6, nullable=True),
          Column(column7, type7, nullable=True),
          Column(column8, type8, nullable=True),
          Column(column9, type9, nullable=True),
        )
        engine = create_engine(self.engine)
        metadata.create_all(engine)


class SqlAlchemyWrite():
    """Allows to pass a command into a database;
    put database type/name in 'engine'"""

    def __init__(self, engine, command):
        self.engine = engine
        self.command = command

    def sql_write(self, data):
        engine = create_engine(self.engine)
        with engine.connect() as con:
            statement = text(self.command)
            for line in data:
                con.execute(statement, **line)

    def sql_any(self):
        engine = create_engine(self.engine)
        with engine.connect() as con:
            rs = con.execute(self.command)

    def sql_any_print(self):
        engine = create_engine(self.engine)
        with engine.connect() as con:
            rs = con.execute(self.command)
            for row in rs:
                print(row)

#
#
# def sql_delete(col_id):
#     engine = create_engine('sqlite:///Lista Prezentów.db')
#     with engine.connect() as con:
#         table = 'Prezenty_2020'
#         table.delete().where(table.c.name==col_id)
