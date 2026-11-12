from .DataAccess import DataAccess as DA
'''
Purpose: This class should handle verification of guesses and should
Created: 11/9 cthompson
'''
class GuessChecker:

    @staticmethod
    def checkGuess(guess):
        if not guess or not guess.strip():
            return False

        challenge = DA.getChallengeBySong(guess)

        return challenge is not None




