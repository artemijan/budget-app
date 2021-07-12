class PathExtractionException(Exception):
    def __init__(self, message):
        super().__init__(message)


class PathExtractor:
    PATH_SEPARATOR = '.'

    def __init__(self, subject):
        self.subject = subject

    def resolve(self, path):
        if not path:
            return self.subject

        parts = self._parse_path(path)

        last_element = self.subject
        for index, part in enumerate(parts):
            path_so_far = self.PATH_SEPARATOR.join(parts[:index])

            if isinstance(last_element, dict):
                if part in last_element:
                    last_element = last_element[part]
                else:
                    raise PathExtractionException(
                        f'Unable to extract path.\n\nA dict at "{path_so_far} does not contain a key "{part}"'
                    )
            elif isinstance(last_element, list):
                index = int(part)  # todo: how to handle non int values here?
                if len(last_element) > index:
                    last_element = last_element[index]
                else:
                    raise PathExtractionException(
                        f'Unable to extract path. \n\nA list at "{path_so_far} does element at index "{index}"'
                    )
            else:
                last_element = getattr(last_element, part)

        return last_element

    def _parse_path(self, path):
        """
        cleans and validates and parses path
        """
        path = path.replace('[', '.')
        path = path.replace('[', '.')
        path = path.replace('"', "")
        path = path.replace('\'', "")

        parts = path.split(self.PATH_SEPARATOR)
        if len(list(filter(None, parts))) != len(parts):
            raise ValueError('the path must not start or end with the dot, contain dots coming in sequence')

        return parts
