import unittest
from main import app

class init(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

class TestAPI(init):
    def test1Get(self):
        resp = self.client.get('/tasks')
        expectedResult = {'result': []}
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, expectedResult)

    def test2PostWithRightData(self):
        testData = {'name': '買晚餐'}
        resp = self.client.post('/task', json=testData)
        expectedResult = {'result': {'name': '買晚餐','status': 0, 'id': 1}}
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, expectedResult)

    def test3PostWithWorngData(self):
        testData = {'nam': '買晚餐'}
        resp = self.client.post('/task', json=testData)
        expectedResult = {'result': 'Field \'name\' is required.'}
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, expectedResult)
    
    def test4UpdateNotFound(self):
        testData = {'name': '買晚餐'}
        resp = self.client.put('/task/999', json=testData)
        expectedResult = {'result': 'Record 999 not found.'}
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json, expectedResult)

    def test5RecordUpdate(self):
        testData = {'name': '買晚餐2', 'status': 1}
        resp = self.client.put('/task/1', json=testData)
        expectedResult = {'result': {'name': '買晚餐2','status': 1, 'id': 1}}
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json, expectedResult)
    
    def test6RecordDelete(self):
        resp = self.client.delete('/task/1')
        self.assertEqual(resp.status_code, 200)
        respGet = self.client.get('/tasks')
        expectedResult = {'result': []}
        self.assertEqual(respGet.json, expectedResult)

if __name__ == "__main__":
    unittest.main()
