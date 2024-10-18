import pathlib
import sys
import dotenv
import os


dotenv.load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_ENGINE_ID = os.getenv("GOOGLE_ENGINE_ID")


def EXPORT_LOCATION():
    location = pathlib.Path.home() / 'Documents/five'

    if not location.exists():
        try:
            location.mkdir(parents=True)
        except Exception as e:
            print(f"Error creating Documents folder: {e}")
            sys.exit()
    else:
        pass

    return str(location)


