class FlightData:
    # This class is responsible for structuring the flight data.

    def create_message(data):
        price = data['price']
        city_from = data['cityFrom']
        iata_from = data['flyFrom']
        city_to = data['cityTo']
        iata_to = data['flyTo']
        out_date = data["route"][0]["local_departure"].split("T")[0],
        return_date = data["route"][1]["local_departure"].split("T")[0]
        print(data["route"][0]["local_departure"])
        print(data["route"][1]["local_departure"])

        message = f'Low price alert! Only ${price} to fly from ' \
                  f'{city_from}-{iata_from} to {city_to}-{iata_to}, ' \
                  f' from {out_date} to {return_date} ' \

        return message



