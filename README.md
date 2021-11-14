# Requirements

You need python version >=3.6

# Installation

Run `sh install.sh` to download language models and required python packages.
This space necessary is approximately 2 gb.

# Server

Start with python `app.py`
There are three endpoint:

- `/all` - Gets all words `nouns`, `verbs`, `enteties`
- `/nouns` - Gets all `nouns`
- `/verbs` - Gets all `verbs`
- `/enteties` - Gets all `enteties`

**Type of word that gets returned**
`NOUN`, `VERB`, `LOC`(location), `PRS`(person) `ORG`(organization)

## Test

You can test and see that it all works by running `python test.py`
