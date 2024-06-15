

class FileLoader:
    @staticmethod
    def define_source_of_file(path: str) -> bool:
        return True if path[1] is '\\' else False
