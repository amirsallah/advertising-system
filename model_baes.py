class BaseAdvertising:
    def __init__(self, unique_id=0):
        self._id = unique_id
        self._clicks = 0
        self._views = 0

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1

    def get_clicks(self):
        return self._clicks

    def get_views(self):
        return self._views

    def describe_me(self):
        return "This is the BaseAdvertising class. It is used to store information about ads and advertisers."

    @staticmethod
    def help():
        string = ""
        string += "id - The id of the ad or advertiser.\n"
        string += "clicks - The number of clicks the ad or advertiser has.\n"
        string += "views - The number of views the ad or advertiser has.\n"
        return string
