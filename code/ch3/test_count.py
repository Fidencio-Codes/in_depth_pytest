from pathlib import Path
from tempfile import TemporaryDirectory
import cards

import pytest


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def test_empty(cards_db):
    assert cards_db.count() == 0


# 'cards_db()' fixture used to push all database initialization 
#   "setting up" for test by getting db ready 
#   'yield' is the "teardown", will always run regardless of the test results

# fixture functions run before the tests that use them 
#   if 'yield' is in the function, then fixture pauses at that step for the tests to run, and then finishes remaining lines in the fixture 'db.close'
#   yield is inside of the 'with' code block for the temporary directory 
#   temporary directory is active while the fixture is in use and tests run 


# using fixture in multiple tests
def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2

