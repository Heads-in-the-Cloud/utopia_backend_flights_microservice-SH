import requests
import json
import unittest


class ApiTests(unittest.TestCase):

    # ------------------------------------------------
    #                   Create Tests
    # ------------------------------------------------

    def create_response_probe(self, url, payload):
        base_url = "http://flights:5000/api"
        headers = {'Content-Type': 'application/json'}

        # convert dict to json string by json.dumps() for body data.
        resp = requests.post(
            url=base_url + url,
            headers=headers,
            data=json.dumps(payload)
        )

        # Validate response headers and body contents, e.g. status code.
        self.assertEqual(
            resp.status_code,
            201,
            "Bad status code")

        resp_body = resp.json()
        self.assertEqual(
            resp_body['url'],
            base_url + url,
            "Bad return URL")

        # print response full body as text
        print(resp.text)

        return resp_body

    def test_airplane_type_create(self):
        url = '/airplane_type/create'

        # Body
        payload = {
            'id': 999,
            'max_capacity': 100
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_airplane_create(self):
        url = '/airplane/create'

        # Body
        payload = {
            'type_id': 999
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_airport_create(self):
        url = '/airport/create'

        # Body
        payload = {
            'iata_id': 'ZZZ',
            'city': 'Zamzabeea, ZZ',
            'name': 'Zamzara Internaional',
            'longitude': 0.00,
            'latitude': 0.00,
            'elevation': 0
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_flight_create(self):
        url = '/flight/create'

        # Body
        payload = {
            'flight_id': 999,
            'route_id': 999,
            'airplane_id': 999,
            'departure_time': '2021-09-29T14:46:14Z',
            'reserved_seats': 99,
            'seat_price': 123.45
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_route_create(self):
        url = '/route/create'

        # Body
        payload = {
            'origin_id': 'ZZZ',
            'destination_id': 'ZZZ',
            'duration': 1
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    # ------------------------------------------------
    #                   Retrieval Tests
    # ------------------------------------------------

    def retrieval_response_probe(self, url, expected):
        base_url = "http://flights:5000/api"
        headers = {'Content-Type': 'application/json'}

        # convert dict to json string by json.dumps() for body data.
        resp = requests.post(
            url=base_url + url,
            headers=headers
        )

        # Validate response headers and body contents, e.g. status code.
        self.assertEqual(
            resp.status_code,
            200,
            "Bad status code")

        resp_body = resp.json()
        self.assertEqual(
            resp.json(),
            expected.json(),
            "Bad return URL")

        # print response full body as text
        print(resp.text)

        return resp_body

    def test_airplane_type_retrieval(self):
        url = '/airplane_type/999'

        expected = {
            "id": "999",
            "max_cap": "100"
        }

        resp_json = ApiTests.retrieval_response_probe(url, expected)

    def test_airplane_retrieval(self):
        url = '/airplane/<id>'

        expected = {

        }

        resp_json = ApiTests.retrieval_response_probe(url, expected)

    def test_airport_retrieval(self):
        url = '/airport/ZZZ'

        expected = {
            'iata_id': 'ZZZ',
            'city': 'Zamzabeea, ZZ',
            'name': 'Zamzara Internaional',
            'longitude': 0.00,
            'latitude': 0.00,
            'elevation': 0
        }

        resp_json = ApiTests.retrieval_response_probe(url, expected)

    def test_flight_retrieval(self):
        url = '/flight/999'

        expected = {
            'flight_id': 999,
            'route_id': 999,
            'airplane_id': 999,
            'departure_time': '2021-09-29T14:46:14Z',
            'reserved_seats': 99,
            'seat_price': 123.45
        }

        resp_json = ApiTests.retrieval_response_probe(url, expected)

    def test_route_retrieval(self):
        url = '/route/<route_id>'

        expected = {
            'origin_id': 'ZZZ',
            'destination_id': 'ZZZ',
            'duration': 1
        }

        resp_json = ApiTests.retrieval_response_probe(url, expected)

    # ------------------------------------------------
    #                   Update Tests
    # ------------------------------------------------

    def update_response_probe(self, url, payload):
        base_url = "http://flights:5000/api"
        headers = {'Content-Type': 'application/json'}

        # convert dict to json string by json.dumps() for body data.
        resp = requests.post(
            url=base_url + url,
            headers=headers,
            data=json.dumps(payload)
        )

        # Validate response headers and body contents, e.g. status code.
        self.assertEqual(
            resp.status_code,
            200,
            "Bad status code")

        resp_body = resp.json()
        self.assertEqual(
            resp_body['url'],
            base_url + url,
            "Bad return URL")

        # print response full body as text
        print(resp.text)

        return resp_body

    # ------------------------------------------------
    #                   Delete Tests
    # ------------------------------------------------

    def delete_response_probe(self, url, payload):
        base_url = "http://flights:5000/api"
        headers = {'Content-Type': 'application/json'}

        # convert dict to json string by json.dumps() for body data.
        resp = requests.post(
            url=base_url + url,
            headers=headers,
            data=json.dumps(payload)
        )

        # Validate response headers and body contents, e.g. status code.
        self.assertEqual(
            resp.status_code,
            201,
            "Bad status code")

        resp_body = resp.json()
        self.assertEqual(
            resp_body['url'],
            base_url + url,
            "Bad return URL")

        # print response full body as text
        print(resp.text)

        return resp_body

    def test_airplane_type_update(self):
        url = '/airplane_type/create'

        # Body
        payload = {
            'id': 999,
            'max_capacity': 100
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_airplane_update(self):
        url = '/airplane/create'

        # Body
        payload = {
            'type_id': 999
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_airport_update(self):
        url = '/airport/create'

        # Body
        payload = {
            'iata_id': 'ZZZ',
            'city': 'Zamzabeea, ZZ',
            'name': 'Zamzara Internaional',
            'longitude': 0.00,
            'latitude': 0.00,
            'elevation': 0
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_flight_update(self):
        url = '/flight/create'

        # Body
        payload = {
            'flight_id': 999,
            'route_id': 999,
            'airplane_id': 999,
            'departure_time': '2021-09-29T14:46:14Z',
            'reserved_seats': 99,
            'seat_price': 123.45
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)

    def test_route_update(self):
        url = '/route/create'

        # Body
        payload = {
            'origin_id': 'ZZZ',
            'destination_id': 'ZZZ',
            'duration': 1
        }

        resp_json = ApiTests.create_response_probe(self, url=url, payload=payload)

        print(resp_json)


if __name__ == "__main__":
    unittest.main()
