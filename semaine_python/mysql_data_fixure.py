#!/usr/bin/env python
import mysql.connector
from faker import Faker

#Exercice: Créer un script python qui génère des data fixtures dans la table utilisateur (5000 entrées).


fake = Faker()

def python_seed1(nbr):
        print(fake.name()/"n")
        print(fake.first_name()")
        print(fake.ascii_free_email()")
        print(fake.date(pattern="%Y-%m-%d", end_datetime=None)")
        print(fake.state()")

        print(fake.address())




python_seed1(5)
