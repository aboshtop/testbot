import os

API_TOKEN = os.environ.get('5567635792:AAELqu_F24oO-3ZQLCghzMRSI2nsrCogzJM')
SENTRY_DSN = os.getenv('SENTRY_DSN')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'Local')
USER_AGENT = os.getenv('USER_AGENT')
