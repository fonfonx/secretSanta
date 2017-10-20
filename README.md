# Secret Santa

This project finds a random permutation between the members of a family for a Secret Santa and sends emails. Constraints are imposed in order to avoid giving a present to a close family member (brother, sister, spouse).

## Requirements
This program works with **Python3** and requires *python-constraint* which can be installed as follows

```
sudo pip3 install git+https://github.com/python-constraint/python-constraint.git
```

## Run the program

You have to create a `config.py` file on this format

```
# -*- coding: utf-8 -*-

FROM_ADDR = 'SENDING_ADDR@gmail.com'
LOGIN = 'SENDING_ADDR@gmail.com'
PASSWORD = 'PASSWORD'

EMAILS = {}
NAMES = {}

NB_FAMILIES = NBR_OF_FAMILIES
FAMILIES = [[]] * NB_FAMILIES
FAMILIES[0] = ['Member1_Family1', 'Member2_Family2', ...]
FAMILIES[1] = ['Member1_Family2', 'Member2_Family2', ...]
FAMILIES[2] = ['Member1_Family3', ...]
FAMILIES[3] = ...

EMAILS['Member1_Family1'] = 'Email_Member1_Family1'
EMAILS['Member2_Family2'] = ...

NAMES['Member1_Family1'] = 'CompleteName_Member1_Family1'
NAMES['Member2_Family2'] = ...

```

Then run `python3 main.py` and press Enter if the permutation is good.
