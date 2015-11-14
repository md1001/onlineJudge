# -*- coding: utf-8 -*-

db.define_table('ocj_user_login',
                Field('First_Name', 'string', requires=IS_NOT_EMPTY()),
                Field('Last_Name', 'string', requires=IS_NOT_EMPTY()),
                Field('Handle', 'string', requires=IS_NOT_EMPTY()),
                Field('Password', 'password', requires=IS_NOT_EMPTY()),
                Field('e_mail', 'string', requires=IS_NOT_EMPTY()),
                Field('Registered_On', 'datetime', requires=IS_NOT_EMPTY()))
