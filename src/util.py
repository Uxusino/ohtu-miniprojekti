#bibtexien käsittelyyn:
#from sqlalchemy import create_engine, Table, MetaData, Column, String
#from pybtex.database import parse_string
#from pybtex.plugin import find_plugin

#funktiot bibtex_parser ja bibtex_writer puuttuvat

class UserInputError(Exception):
    pass

def validate_reference(data):
    if len(data["title"]) < 2:
        raise UserInputError("Title must be at least 2 characters long")

    if len(data["title"]) > 100:
        raise UserInputError("Title must be under 100 characters long")

    if not data["year"].isdigit() or not 1000 <= int(data["year"]) <= 9999:
        raise UserInputError("Year must be a valid 4-digit number between 1000 and 9999")

    if len(data["publisher"]) < 2:
        raise UserInputError("Publisher must be at least 2 characters long")

    if len(data["publisher"]) > 100:
        raise UserInputError("Publisher must be under 100 characters long")
