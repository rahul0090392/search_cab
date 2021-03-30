GET_NEARBY_DRIVERS_BY_DISTANCE = """SELECT id,
    phone_number,
    name,
    car_number,
    ( 6371 * acos( cos( radians({latitude_search}) )
        * cos( radians( latitude ) )
        * cos( radians( longitude )
        - radians({longitude_search}) )
        + sin( radians({latitude_search}) )
        * sin(radians(latitude)) ) )
    AS distance
    FROM
        restapi_driver
    GROUP BY
        phone_number
    HAVING
        distance <= {distance}
    ORDER BY distance;"""

Queries = {"GET_NEARBY_DRIVERS_BY_DISTANCE": GET_NEARBY_DRIVERS_BY_DISTANCE}