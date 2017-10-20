# -*- coding: utf-8 -*-

from constraint import *
from random import shuffle

from mail import create_msg_html, send_email
from config import FAMILIES, NB_FAMILIES, EMAILS, NAMES, FROM_ADDR, LOGIN, PASSWORD

people = [sbd for family in FAMILIES for sbd in family]
shuffle(people)

problem = Problem()

for sbd in people:
    problem.addVariable(sbd, people)

problem.addConstraint(AllDifferentConstraint())

for family in FAMILIES:
    for sbd in family:
        problem.addConstraint(NotInSetConstraint(family), [sbd])

sol = problem.getSolution()
print(sol)

input("Press Enter if OK...")

# send mails
for k, v in sol.items():
    msg = create_msg_html(NAMES[k], NAMES[v])
    send_email(FROM_ADDR, [EMAILS[k]], [], "Noël en Bretagne", msg, LOGIN, PASSWORD)

print('Mails sent!')
