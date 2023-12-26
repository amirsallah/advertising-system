from model_baes import BaseAdvertising


class Advertiser(BaseAdvertising):
    advertisers = []

    def __init__(self, unique_id, name):
        super().__init__(unique_id)
        self._name = name
        self._check_unique_id()
        Advertiser.advertisers.append(self)

    def _check_unique_id(self):
        for user in Advertiser.advertisers:
            if self._id == user.get_id():
                raise ValueError("The identifier is duplicated!!!")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def describe_me(self):
        return "This is the Advertiser class. It is used to store information about advertisers."

    @staticmethod
    def get_total_clicks():
        total_clicks = 0
        for advertiser in Advertiser.advertisers:
            total_clicks += advertiser.get_clicks()
        return total_clicks

    @staticmethod
    def help():
        string = ""
        string += "id - The id of the advertiser.\n"
        string += "name - The name of the advertiser.\n"
        string += "clicks - The number of clicks the advertiser has.\n"
        string += "views - The number of views the advertiser has.\n"
        return string
