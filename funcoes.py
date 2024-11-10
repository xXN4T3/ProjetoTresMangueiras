from fastapi.exceptions import HTTPException

def errorFunction(self, E):
        if isinstance(E, HTTPException):
                raise E
        else:
            print(str(E))
            raise HTTPException(400, str(E))