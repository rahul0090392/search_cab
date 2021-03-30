class Utility:
    @staticmethod
    def flat_error_string(errors):
        try:
            error_list = list(errors.keys())
            flat_error = "{}".format(errors[error_list[0]][0])
            flat_error = flat_error.replace("This", "")
            flat_error = flat_error.replace("this field", error_list[0])
            if "blank" in flat_error:
                flat_error = error_list[0] + flat_error
            if "this value" in flat_error:
                flat_error = flat_error.replace("this value", error_list[0])
            if "required" in flat_error:
                flat_error = flat_error.replace("field", error_list[0])
            return flat_error.capitalize()
        except IndexError:
            return errors

    @staticmethod
    def get_integrity_error_field(error_tuple):
        try:
            return error_tuple[0].split(".")[1]
        except IndexError:
            return error_tuple[0]
