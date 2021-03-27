from src.Event.mainEvent import mainEvent


class buyBook(mainEvent):

    def get_event_info(self, date, character):
        return date.strftime("%B") + " " + date.strftime("%d") + ", " + date.strftime("%Y") + ' ' + date.strftime("%A") + character.name
