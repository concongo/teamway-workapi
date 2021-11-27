from .models import Worker, Shift, WorkPlanner
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json


# Create your tests here.
class WorkerTestCase(APITestCase):
    def setUp(self):

        worker1 = Worker.objects.create(personal_id="00000001T",
                                        name="John",
                                        last_name="Doe",
                                        email="john@doe.com",
                                        phone_number="5555555555")
        worker2 = Worker.objects.create(personal_id="00000034T",
                                        name="John",
                                        last_name="Doe",
                                        email="john@doe.com",
                                        phone_number="777777777")

        shift1 = Shift.objects.create(start_hour=0, end_hour=8)
        Shift.objects.create(start_hour=8, end_hour=16)

        WorkPlanner.objects.create(date='2021-11-27',
                                   shift=shift1, worker=worker1)
        WorkPlanner.objects.create(date='2021-11-27',
                                   shift=shift1, worker=worker2)

        return super().setUp()

    def test_worker_list_view(self):
        '''
        Testing GET list API View
        '''
        endpoint = reverse('worker_list')
        response = self.client.get(endpoint)
        content_dict = json.loads(response.content)

        assert len(content_dict) == 2
        assert response.status_code == 200

    def test_worker_detail_view(self):
        '''
        Testing GET Detail API View
        '''
        endpoint = reverse('worker_detail', args=('00000001T', ))
        response = self.client.get(endpoint)
        content_dict = json.loads(response.content)

        assert content_dict['personal_id'] == '00000001T'
        assert response.status_code == 200

    def test_worker_create_view(self):
        '''
        Testing CREATE Worker API View
        '''
        endpoint = reverse('worker_create')
        data = {'personal_id': 'Y77663434B',
                'name': 'Jane',
                'last_name': 'Doe',
                'email': 'jane.doe@gmail.com',
                'phone_number': '22222222'}
        response = self.client.post(endpoint, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Worker.objects.count() == 3
        assert Worker.objects.filter(personal_id=data['personal_id']).first().name == 'Jane'

    def test_worker_one_shift(self):
        '''
        Testing A worker never has two shifts on the same day on API
        '''
        endpoint = reverse('workplan_create')

        workplan = WorkPlanner.objects.first()
        worker = workplan.worker
        shift = workplan.shift

        new_shift = Shift.objects.exclude(id=shift.id).first()

        data = {'date': '2021-11-27',
                'shift': new_shift.id,
                'worker': worker.personal_id}

        response = self.client.post(endpoint, data, format='json')
        content_dict = json.loads(response.content)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert content_dict['worker'][0] == "The worker is already working a shift on the selected date."
