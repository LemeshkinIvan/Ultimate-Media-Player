from datetime import datetime


class MediaFile:
    format: str = None
    duration: str | int = None          # not sure about type
    date_of_creation: datetime = None
    file: bytearray = None

    def __init__(self):
        pass


class AudioFile(MediaFile):
    pass


class VideoFile(MediaFile):
    pass
