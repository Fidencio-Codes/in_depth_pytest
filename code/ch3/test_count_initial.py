from pathlib import Path
from tempfile import TemporaryDirectory
import cards


def test_empty():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)

        count = db.count()
        db.close()

        assert count == 0


# to call the 'count()' function, we need a database object 
    # db object is called by 'cards.CardsDB(db_path)'

# 'cards.CardsDB()' function is a constructor and returns a 'CardsDB' object 

# 'db_path' parameter needs to be a 'pathlib.path' object that points to database directory 
    # 'pathlib.Path' objects is standard way to represent file system paths 
    # a temporary directory is created for this purpose, 'tempfile.Temporary-Directory()'

# code to set up database before calling 'count()' 

# call to db.close()
    # need to close database before assert statement
    # if the assert statement fails it wont run 




