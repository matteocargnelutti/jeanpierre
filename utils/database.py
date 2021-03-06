#! /usr/bin/env python3
# coding: utf-8
"""
Jean-Pierre [Prototype]
A Raspberry Pi robot that helps people make their grocery list.
Matteo Cargnelutti - github.com/matteocargnelutti

utils/cls.py - SQlite connector
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import os
import re
import sqlite3

#-----------------------------------------------------------------------------
# Database class
#-----------------------------------------------------------------------------
class Database:
    """
    This class handles :
    - Provides a link and a cursor to the database as class attributes
    Usage :
    - Database.on()
    - Database.CURSOR.execute(query, params)
    - ... etc
    - Database.off()
    Available class attributes :
    - LINK
    - CURSOR
    - FILE (path to the database file)
    """
    DATABASE_PRODUCTION = 'database.db'
    """ Normal database filename """
    DATABASE_TEST = 'database_test.db'
    """ Test database filename : this database is temporary """
    TEST_MODE = False
    """ Does it need to use the test database ? """

    @classmethod
    def on(cls):
        """
        Connect to the database
        :rtype: bool
        """
        # Don't reconnect if already connected
        if cls.is_ready():
            return False

        # Filename
        cls.FILE = cls.DATABASE_PRODUCTION

        if cls.TEST_MODE:
            cls.FILE = cls.DATABASE_TEST

        # Connect
        cls.LINK = sqlite3.connect(cls.FILE)
        cls.LINK.row_factory = sqlite3.Row
        cls.CURSOR = cls.LINK.cursor()

        return True

    @classmethod
    def off(cls):
        """
        Ends connection with the database.
        :rtype: bool
        """
        if cls.LINK:
            cls.LINK.close()
        cls.LINK = None
        cls.CURSOR = None
        return True

    @classmethod
    def is_ready(cls):
        """
        Is the connection open ?
        :rtype: bool
        """
        return hasattr(cls, 'LINK') and cls.LINK != None
