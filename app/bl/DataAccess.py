'''
Purpose: this class should be used to pass data to business logic
Created: cthompson, 11/9/2026
'''
from app.models import Challenge

class DataAccess:

    # CHALLENGE INFO
    @staticmethod
    def getChallengeBySong(song):
        return Challenge.objects.filter(
                song__iexact=song.strip()
            ).first()

    @staticmethod
    def getChallengeByID(challenge_id):
        try:
            return Challenge.objects.get(id=challenge_id)
        except Challenge.DoesNotExist:
            return None

    @staticmethod
    def getRandomChallenge():
        return Challenge.objects.order_by("?").first()

    # SONG INFO
    @staticmethod
    def getSongByChallenge(challenge):
        if challenge is None:
            return None
        return challenge.song

    @staticmethod
    def getClipsByChallenge(challenge):
        if challenge is None:
            return None
        return [
            challenge.clip_1,
            challenge.clip_2,
            challenge.clip_3
        ]

