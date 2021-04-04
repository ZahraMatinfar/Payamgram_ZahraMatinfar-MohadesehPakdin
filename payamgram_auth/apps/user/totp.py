from django_otp.oath import TOTP
import time


class TOTPVerification:

    def __init__(self, key):
        """
        secret key that will be used to generate a token,
        User can provide a custom value to the key.

        counter with which last token was verified.
        Next token must be generated at a higher counter value.

        verified will return True, if a token has been successfully
        verified.
        """
        self.key = key
        self.last_verified_counter = -1
        self.verified = False
        self.number_of_digits = 6
        self.token_validity_period = 60

    def totp_obj(self):
        """
        create a TOTP object.
        the current time will be used to generate a counter
        """
        totp = TOTP(key=bytes(self.key.encode()),
                    step=self.token_validity_period,
                    digits=self.number_of_digits)
        totp.time = time.time()
        return totp

    def generate_token(self):
        """
        get the TOTP object and use that to create token.
        token can be obtained with `totp.token()`
        """
        totp = self.totp_obj()
        token = str(totp.token()).zfill(6)
        return token

    def verify_token(self, token, tolerance=0):
        try:
            # convert the input token to integer
            token = int(token)
        except ValueError:
            # return False, if token could not be converted to an integer
            self.verified = False
        else:
            totp = self.totp_obj()

            """check if the current counter value is higher than the value of
            last verified counter and check if entered token is correct by
            calling totp.verify_token()
            """
            if ((totp.t() > self.last_verified_counter) and
                    (totp.verify(token, tolerance=tolerance))):

                """if the condition is true, set the last verified counter value
                to current counter value, and return True"""

                self.last_verified_counter = totp.t()
                self.verified = True
            else:
                """if the token entered was invalid or if the counter value
                was less than last verified counter, then return False"""

                self.verified = False
        return self.verified
