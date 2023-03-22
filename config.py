from dataclasses import dataclass, field
import os
import json


@dataclass
class Setup:
    FULL_PATH: str = os.path.dirname(os.path.realpath(__file__))
    CREDS_PATH: str = os.path.join(FULL_PATH, "ui", "data", "login_data.json")


@dataclass
class DataLogin:
    CORRECT_USERNAME: str = field(init=False)
    EMPTY_USERNAME: str = field(init=False)
    LOCKED_USERNAME: str = field(init=False)
    CORRECT_PASSWORD: str = field(init=False)
    INCORRECT_PASSWORD: str = field(init=False)
    MAIN_TITLE: str = field(init=False)
    ERR_MSG_WRONG_CREDS: str = field(init=False)
    ERR_MSG_EMPTY_CREDS: str = field(init=False)
    ERR_MSG_LOCKED_USER: str = field(init=False)

    def __post_init__(self):
        self.DATA_SET = json.load(open(Setup.CREDS_PATH)) if Setup.CREDS_PATH else {}
        self.CORRECT_USERNAME: str = self.DATA_SET["correct_username"]
        self.EMPTY_USERNAME: str = self.DATA_SET["empty_username"]
        self.LOCKED_USERNAME: str = self.DATA_SET["locked_username"]
        self.CORRECT_PASSWORD: str = self.DATA_SET["correct_password"]
        self.INCORRECT_PASSWORD: str = self.DATA_SET["incorrect_password"]
        self.MAIN_TITLE: str = self.DATA_SET["main_title"]
        self.ERR_MSG_WRONG_CREDS: str = self.DATA_SET["err_msg_wrong_creds"]
        self.ERR_MSG_EMPTY_CREDS: str = self.DATA_SET["err_msg_empty_creds"]
        self.ERR_MSG_LOCKED_USER: str = self.DATA_SET["err_msg_locked_user"]


data = DataLogin()

login_incorrect_password = [data.CORRECT_PASSWORD, data.INCORRECT_PASSWORD, data.ERR_MSG_WRONG_CREDS]
login_empty_username = [data.EMPTY_USERNAME, data.CORRECT_PASSWORD, data.ERR_MSG_EMPTY_CREDS]
login_locked_username = [data.LOCKED_USERNAME, data.CORRECT_PASSWORD, data.ERR_MSG_LOCKED_USER]
