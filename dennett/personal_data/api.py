from dennett.api import simple_endpoint
from dennett.personal_data.models import PersonalDataCollection
from . import personal_data


@personal_data.route('v2/personal-data', methods=['GET', 'POST'])
def personal_data_endpoint():
    collection = PersonalDataCollection(PersonalDataCollection.V2_COLLECTION_NAME)
    return simple_endpoint(collection)
