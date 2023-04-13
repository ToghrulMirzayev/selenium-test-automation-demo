[![Code Checks](https://github.com/ToghrulMirzayev/selenium-test-automation-demo/actions/workflows/checks.yml/badge.svg)](https://github.com/ToghrulMirzayev/selenium-test-automation-demo/actions/workflows/checks.yml) [![Test Automation](https://github.com/ToghrulMirzayev/selenium-test-automation-demo/actions/workflows/pipelines.yml/badge.svg)](https://github.com/ToghrulMirzayev/selenium-test-automation-demo/actions/workflows/pipelines.yml) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ToghrulMirzayev_selenium-test-automation-demo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ToghrulMirzayev_selenium-test-automation-demo)

# selenium-test-automation-demo

UI automated test suite with Selenium using Page Elements pattern. 
The main purpose is to demonstrate Page Elements pattern in use

# Getting started

* Install dependencies
```
pip install -r requirements.txt
```

* Run tests

  * Run all tests
  ```
  pytest
  ```
  * Run specific test using predefined markers
  ```
  pytest -k <pytest mark>
  ```
  * Run tests in parallel, by using -n option followed by the number of CPUs
  ```
  pytest -n <CPU number>
  ```
