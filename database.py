import csv

import pandas as pd


class User:
    def __init__(self, username, password):
        """
        This function initializes a new user object
        :param username: The username value of the user
        :param password: The password value of the user
        """
        self.authentication_csv_file_location = 'database.csv'
        self.username = username
        self.password = password
        self.is_authenticated = False

    def check_if_user_is_already_saved(self):
        """
        This function check if a user is already saved in the database:
        If the user is already saved return first instance of the user
        else return None
        :return:
        """
        df_json = pd.read_csv(self.authentication_csv_file_location)
        user_dict_list = df_json.to_dict('records')
        for user_data in user_dict_list:
            if user_data.get('username') == self.username:
                return user_data
        return None

    def save(self):
        """
        This function saves a new user to the database
        :return:
        """
        user = self.check_if_user_is_already_saved()
        if not user:
            with open(self.authentication_csv_file_location, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['', self.username, self.password])
            return True, user
        else:
            return False, user

    def login(self):
        """
        This function logs in a user
        :return:
        """
        self.is_authenticated = True
