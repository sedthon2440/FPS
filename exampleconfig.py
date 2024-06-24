from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 9671629
    API_HASH = "be5c84e9dc1ca0e2b53d54b71e575124"
    # the name to display in your alive message
    ALIVE_NAME = "BiLaL"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:bilal2440@localhost:5432/BiLaL"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBuxX4wkNbwrdNGySP4sJkS-9XmZdYVNHk9Hymr5S7U4xau0267es4AyILubh0LrHyg5b01bYt9Sw5-6BoGY0yrPB8zGAiUnq3Dqd7yqBjNwv_0fBroh5Ka4YtoZ9CEKtDvCf6k91Cb_BlqzgCyXUPK58vFO0F6m4knXBZoA8KLswRhmujWc9N5vS_groYY6zLSq7V1UhuwazU4eeV8W0cn5T7MbyLVNFELrhyFvBOCLsfsWoRFjRmSqaTqyK40VuY84Bvvg81T5ButSMWbXLHNIvFowNbMYYfK_KrVIJOCBm0tEXmZy8jLJei0o6nd0NAkNFEJhpPmy4ySBVDcReTjsw="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "6056629549:AAET7XFiC_nGSU266d50gpy7rprmhTBhE-c"
    # command handler
    TZ = "Asia/Baghdad"
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
