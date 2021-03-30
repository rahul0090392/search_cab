import logging
from restapi.models import Driver
from restapi.exceptions import DriverNotFound, NoNearByCabsFound
from restapi.queries import Queries

# Get an instance of a logger
logger = logging.getLogger(__name__)

DISTANCE = 4


class DriverService:
    @staticmethod
    def get_driver(driver_id):
        try:
            driver = Driver.objects.get(id=driver_id)
            logger.info("driver found")
            return driver
        except Driver.DoesNotExist:
            raise DriverNotFound

    @staticmethod
    def add_new_driver(data):
        driver_obj = Driver()
        driver_obj.name = data["name"]
        driver_obj.email = data["email"]
        driver_obj.phone_number = data["phone_number"]
        driver_obj.license_number = data["license_number"]
        driver_obj.car_number = data["car_number"]
        driver_obj.save()
        logger.info("driver object registered")
        return driver_obj

    @staticmethod
    def update_or_set_location(data, driver_id):
        driver = DriverService.get_driver(driver_id)
        driver.latitude = data["latitude"]
        driver.longitude = data["longitude"]
        driver.save()
        logger.info("driver current location updated")
        return driver

    @staticmethod
    def get_all_nearby_drivers(data):
        query = Queries["GET_NEARBY_DRIVERS_BY_DISTANCE"].format(
            latitude_search=data["latitude"],
            longitude_search=data["longitude"],
            distance=DISTANCE,
        )
        result = Driver.objects.raw(query)

        result = list(result)
        if len(result) == 0:
            logger.info("nocabs found")
            raise NoNearByCabsFound
        logger.info(f"{len(result)} cabs found")
        return result
