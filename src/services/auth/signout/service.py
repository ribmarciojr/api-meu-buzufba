from fastapi import Response


class SignoutService:

    @staticmethod
    def signout(response: Response) -> dict:
        response.delete_cookie(key="access_token")

        return {"message": "User logged out"}
        