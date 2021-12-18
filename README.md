![TeamGetServedLogo.png](../../../_resources/TeamGetServedLogo.png)

# Get Served

<details><summary>Click to Expand</summary>

## Table of Contents

1.  About The Project
    
    - Aims and Objectives
2.  Getting Started
    
    - Prerequisites
    - Installation
3.  Usage
    
    - How To Use
    - Rules And That
4.  Testing and Evaluation
    

</details>

## Documentation

[Documentation](https://linktodocumentation) \- Dummy link at the mo

## About the project

### Aims and Objectives

Really fun game

## Getting started

### Prerequisites

To run this program locally you need to have the following installed/setup:

- Python v3.9 or above
- API key for superheroAPI (please see API Reference below) - [Click Here For Link](https://superheroapi.com/)
- MySQL Database - [Link to SQL query to set up database](/C:/Users/User/AppData/Local/Temp/20dGyoUwWkPKMir6aoqSslqIDpw/resources/save/game_database.sql "../save/game_database.sql")
- A really swanky looking terminal to increase the viewing experience

### Installation

1.  Clone the repo.
2.  Setup a MySQL database, the information to create the DB is in an SQL file under the 'save' directory.
3.  Install dependencies by using *requirements.txt*, this can be done using the following command:
    *If using a virtual environment set it up first, then install the requirements.txt.
    `pip install -r requirements.txt`
4.  Copy the *.env.example* file and rename it to *.env* within the same directory.
5.  Fill in the *.env* information with your own API keys and DB details.

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type | Description |
| --- | --- | --- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | **Required**. Id of item to fetch |

#### some(stuff1, stuff2)

Takes two stuffs and returns the stuff.

## Features

- Cross platform
- Other stuff

### How to Use

To run the game, run the following command from the root directory:
`python -m main`

### Rules and that

The aim of the game is to keep/get as many 'pints' as possible while navigating through perilous scenes which constantly change. Your play-through at the end will be recorded in a database and a score board will be rendered at the end.

Mechanics:

- Go Home - sometimes you'll get an option to 'reset' however, your score will be carried over and you will be penalised.
- Events - some events will depend on your character, choices or just pure luck, these can affect your point score too - so choose wisely!
- Death *cough*, I mean Tee-total - If you lose too many 'pints' you'll become sober for life and enjoy a long and fruitful life (but, yeah, you lose mate).

## Demo

![Bar-Sim-Demo.gif](../../../_resources/Bar-Sim-Demo.gif)

(keep file in repo rather than external hosting to make life easier)

## Known issues/bugs

## Testing

*To run all unit tests, the tests directory needs to have an empty `__init__.py` file.*
To run automated unit tests, run the following command in the root directory:
`python -m unittest`
Specific modules can be specified by appending the file path of the test. See unittest documentation for more information e.g.
`python -m unittest tests/unit/util/test_dice_decider.py`

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Acknowledgements

- [Beer Pouring Animation - Original MP4 Video source](https://pixabay.com/videos/beer-glass-pouring-drink-bar-pub-67395/)
- [Attribution Credit - Breakdown Pictures](https://pixabay.com/users/breakdownpictures-12141240/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=67395)

## Authors

- [@chloehooper](https://github.com/chloeh98)
- [@louannloizou](https://github.com/louannl)
- [@nuranozan](https://github.com/nuran-o)
- [@zoethomas](https://github.com/zoerthomas)
- [@sunithawebster](https://github.com/SunithaWebster)