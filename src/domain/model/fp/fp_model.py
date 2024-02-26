from fp_model_id import FpModelId


class FpModel:
    def __init__(self, extension: str):
        if len(extension) > 10:
            raise ValueError("Invalid extension")
        self.id = FpModelId()
        self.extension = extension
