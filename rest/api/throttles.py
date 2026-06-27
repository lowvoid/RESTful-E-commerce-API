from rest_framework.throttling import UserRateThrottle


class BurstUserThrottle(UserRateThrottle):
    rate = 'burst'


class SustainedUserThrottle(UserRateThrottle):
    rate = 'sustained'
