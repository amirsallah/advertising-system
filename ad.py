from advertiser import Advertiser
from model_baes import BaseAdvertising


class Ad(BaseAdvertising):
    def __init__(self, unique_id, title, img_url, link, advertiser):
        super().__init__(unique_id)
        self._title = title
        self._img_url = img_url
        self._link = link
        self._advertiser = advertiser

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_img_url(self):
        return self._img_url

    def set_img_url(self, img_url):
        self._img_url = img_url

    def get_link(self):
        return self._link

    def set_link(self, link):
        self._link = link

    def set_advertiser(self, advertiser: Advertiser):
        self._advertiser = advertiser

    def inc_clicks(self):
        super().inc_clicks()
        self._advertiser.inc_clicks()

    def inc_views(self):
        super().inc_views()
        self._advertiser.inc_views()

    def describe_me(self):
        return "This is the Ad class. It is used to store information about ads."

    @staticmethod
    def help():
        string = ""
        string += "id - The id of the ad.\n"
        string += "title - The title of the ad.\n"
        string += "img_url - The image url of the ad.\n"
        string += "link - The link of the ad.\n"
        string += "advertiser - The advertiser of the ad.\n"
        string += "clicks - The number of clicks the ad has.\n"
        string += "views - The number of views the ad has.\n"
        return string
