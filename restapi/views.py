# -*- coding: utf-8 -*-
import logging
import sys
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapi.repositories.crud import DriverService
from restapi.utils import Utility
from restapi.dtos import ValidateDriverAddParams, ValidateDriverLocationParams
from restapi.serializers import DriverSerializer, NearByDriverSerializer
from restapi.exceptions import DriverNotFound, NoNearByCabsFound
from restapi.errors.constants import INTERNAL_SERVER, NO_CABS

# Create your views here.

# Get an instance of a logger
logger = logging.getLogger(__name__)


class DriverRegisterAPI(APIView):
    def post(self, request):
        try:
            params = ValidateDriverAddParams(data=request.data)

            if not params.is_valid():
                logger.info("invalid parameters passed")
                return Response(
                    data={
                        "status": "failure",
                        "details": Utility.flat_error_string(params.errors),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            driver_obj = DriverService.add_new_driver(request.data)
            driver_data = DriverSerializer(driver_obj)
            return Response(driver_data.data, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            logger.error("driver with given details already exists")
            return Response(
                data={
                    "status": "failure",
                    "reason": f"{Utility.get_integrity_error_field(e.args)} already exists",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception:
            logger.error(sys.exc_info()[1])
            return Response(
                data={"status": "failure", "reason": INTERNAL_SERVER},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class DriverUpdateLocationAPI(APIView):
    def post(self, request, driver_id):
        try:
            params = ValidateDriverLocationParams(data=request.data)

            if not params.is_valid():
                logger.info("invalid parameters passed for location update")
                return Response(
                    data={
                        "status": "failure",
                        "details": Utility.flat_error_string(params.errors),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            DriverService.update_or_set_location(request.data, driver_id)

            return Response({"status": "success"}, status=status.HTTP_202_ACCEPTED)

        except DriverNotFound:
            logger.info("no driver found with given id")
            return Response(
                data={
                    "status": "failure",
                    "reason": f"No driver exists with {driver_id}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception:
            logger.error(sys.exc_info()[1])
            return Response(
                data={"status": "failure", "reason": INTERNAL_SERVER},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetNearByDrivers(APIView):
    def post(self, request):
        try:
            params = ValidateDriverLocationParams(data=request.data)

            if not params.is_valid():
                logger.info("invalid parameters passed for get near by drivers")
                return Response(
                    data={
                        "status": "failure",
                        "details": Utility.flat_error_string(params.errors),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            near_by_drivers = DriverService.get_all_nearby_drivers(params.data)
            serialize_data = NearByDriverSerializer(near_by_drivers, many=True)
            result = {"available_cabs": serialize_data.data}

            return Response(result, status=status.HTTP_200_OK)

        except NoNearByCabsFound:
            logger.info("No near by cabs found")
            return Response({"message": NO_CABS}, status=status.HTTP_200_OK)
        except Exception:
            logger.error(sys.exc_info()[1])
            return Response(
                data={"status": "failure", "reason": INTERNAL_SERVER},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
