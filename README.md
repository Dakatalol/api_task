## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install pipenv
```
```bash
pipenv install
```
```bash
pipenv shell
```
Verify that C://Users/[YOUR_USER]/.virtualenvs is present with a folder inside with the following pattern: ​"api_task--.xxxxxxx"

Open your Pycharm -> File -> Settings ->
Project:[PROJECT_NAME]#->Settings_Button->Add->Virtual Environment->Existing Environnment and press the "..." button. Navigate to the  C://Users/[YOUR_USER]/.virtualenvs/api_task--.xxxxxxx/Scripts and select python.exe

## Running the tests

Run from inside project directory.

to run a specific test:
```
py.test tests/user_test.py
```

Pytest can autodiscover all tests:
````
py.test C:\automation\api_task\tests
````

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.txt)