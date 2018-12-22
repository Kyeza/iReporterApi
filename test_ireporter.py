"""docstring for testing module"""
from time import time
from datetime import datetime
import unittest
import json
import app


class TestIReporterApi(unittest.TestCase):
    """This class is a Test case for testing the ireporter endpoints"""

    def setUp(self):
        """Define test variables"""

        # initialize test app
        self.client = app.APP.test_client()
        self.incident = {
            'createdOn': datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'),
            'createdBy': 0,
            'type': 'red-flag',
            'location': 'Andela',
            'status': 'draft',
            'Images': ["image_1.jpg", "image_2.png"],
            'Videos': ["video_1.mp4", "video_2.mp4"],
            'comment': 'This is a sample comment'
        }

        # bind the app to the current context
        with app.APP.app_context():
            # setup test data
            self.database = app.DATABASE

    def test_empty_database(self):
        """test for empty database"""
        response = self.client.get('/ireporter.com/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json['data'], self.database)

    def test_create_red_flag(self):
        """test for creation of a red-flag"""
        response = self.client.post('/ireporter.com/api/v1/red-flags',
                                    data=json.dumps(self.incident),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['data'][0]['id'], 1)
        self.assertEqual(response.json['data'][0]['message'], 'Created red-flag record')
        response = self.client.post('/ireporter.com/api/v1/red-flags',
                                    data=json.dumps(self.incident),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['data'][0]['id'], 2)
        self.assertEqual(response.json['data'][0]['message'], 'Created red-flag record')
        self.assertEqual(len(self.database), 2)

    def test_get_all_red_flags(self):
        """test for getting all created red-flags"""
        response = self.client.get('/ireporter.com/api/v1/red-flags')
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.json['data'], self.database)

    def test_get_a_red_flag(self):
        """test for getting a specific red-flags"""
        response = self.client.get('/ireporter.com/api/v1/red-flags/1')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json['data'][0], self.database[0])

    def test_update_red_flag(self):
        """test for updattng location of a red-flag"""
        response = self.client.patch('/ireporter.com/api/v1/red-flags/1',
                                     data=json.dumps({'location': 'New location'}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'][0]['id'], 1)
        self.assertEqual(response.json['data'][0]['message'], 'Updated red-flag record’s location')
        self.assertEqual(self.database[0]['location'], 'New location')
        
    def test_update_red_flag(self):
        """test for updattng comment of a red-flag"""
        response = self.client.patch('/ireporter.com/api/v1/red-flags/1',
                                     data=json.dumps({'comment': 'This is a new sample comment'}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'][0]['id'], 1)
        self.assertEqual(response.json['data'][0]['message'], 'Updated red-flag record’s comment')
        self.assertEqual(self.database[0]['comment'], 'This is a new sample comment')

    def test_delete_red_flag(self):
        """test for deletion of a red-flag"""
        response = self.client.delete('/ireporter.com/api/v1/red-flags/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['data'][0]['id'], 2)
        self.assertEqual(response.json['data'][0]['message'], 'red-flag record has been deleted')
        self.assertEqual(len(self.database), 1)

    def test_error_not_valid_incident(self):
        """test error for not valid incident"""
        response = self.client.post('/ireporter.com/api/v1/red-flags',
                                    data=json.dumps({}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Not a valid red-flag')

    def test_error_non_existent_red_flag(self):
        """test error for red-flag that doesnt exist"""
        response = self.client.get('/ireporter.com/api/v1/red-flags/3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'],
                         f"resource not found, red-flag with id=3 doesn't exist")

    def test_error_patch_non_existent_record(self):
        """test error for patch on non existent red-falg"""
        response = self.client.patch('/ireporter.com/api/v1/red-flags/3',
                                     data=json.dumps({'comment': 'This is a new sample comment'}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'],
                         f"resource not found, red-flag with id=3 doesn't exist")

    def test_error_patch_with_non_json_object(self):
        """test error if request to patch is not json"""
        response = self.client.patch('/ireporter.com/api/v1/red-flags/1',
                                     data=json.dumps({'comment': 'This is a new sample comment'}),
                                     content_type='application/text')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'bad request, not a valid red-flag')

    def test_error_patch_not_location_or_comment(self):
        """test error when patch request is not on eith comment or location"""
        response = self.client.patch('/ireporter.com/api/v1/red-flags/1',
                                     data=json.dumps({'type': 'This is a new sample comment'}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'bad request, must pass a comment/location')

    def test_error_delete_non_existent_record(self):
        """test error when trying to delete record that doesn't exist """
        response = self.client.delete('/ireporter.com/api/v1/red-flags/3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'],
                         f"resource not found, red-flag with id=3 doesn't exist")


if __name__ == '__main__':
    unittest.main()
