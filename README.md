# Get Served
<!-- TABLE OF CONTENTS -->
<details open="open">
    <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
    <ol>
        <li>
            <a href="#about-the-project">About The Project</a>
            <ul>
                <li><a href="#aims-and-objectives">Aims and Objectives</a></li>
            </ul>
        </li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li><a href="#prerequisites">Prerequisites</a></li>
                <li><a href="#installation">Installation</a></li>
            </ul>
        </li>
        <li>
            <a href="#usage">Usage</a>
            <ul>
                <li><a href="#how-to-use">How To Use</a></li>
                <li><a href="#rules-and-that">Rules And That</a></li>
            </ul>
        </li>
        <li><a href="#testing-and-evaluation">Testing and Evaluation</a></li>
    </ol>
</details>

<!-- ABOUT THE PROJECT -->
# About the project

## Aims and Objectives
Really fun game

<!-- GETTING STARTED -->
# Getting started

## Prerequisites
To run this program locally you need to have the following installed/setup:
- Python v3.9 or above
- API key for superheroAPI
- mySQL Database 
- A really swanky looking terminal to increase the viewing experience

## Installation
1. Clone the repo.
2. Setup a mySQL database, the information to create the DB is in an sql file under the 'save' directory.
3. Install dependencies by using requirements.txt, this can be done using the following command:

    *If using a virtual environment set it up first, then install the requirements.txt.

    ```
    pip install -r requirements.txt
    ```
4. Copy the .env.example file and rename it to .env within the same directory.
5. Fill in the .env information with your own API keys and db details.

<!-- USAGE -->
# Usage
## How to use
To run the game, run the following command from the root directory:

```

python -m main
=======
pip install -r requirements.txt

```

## Rules and that
:)

<!-- TESTING -->
# Testing
*To run all unit tests, the tests directory needs to have an empty `__init__.py` file.*

To run automated unit tests, run the following command in the root directory:
```
python -m unittest
```

Specific modules can be specified by appending the file path of the test. See unittest documentation for more information e.g.

```
python -m unittest tests/unit/utils/test_dice_decider.py
```