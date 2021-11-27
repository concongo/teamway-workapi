from rest_framework import serializers
from rest_framework.reverse import reverse
from django.core.exceptions import ValidationError
from .models import Worker, Shift, WorkPlanner


class WorkerSerializer(serializers.ModelSerializer):

    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = ['personal_id', 'name', 'last_name', 'absolute_url', ]

    def get_absolute_url(self, obj):
        return reverse('worker_detail', args=(obj.pk, ))


class WorkerDetailSerializer(serializers.ModelSerializer):

    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = ['personal_id', 'name', 'last_name',
                  'email', 'phone_number', 'update', 'delete', ]

    def get_update(self, obj):
        return reverse('worker_update', args=(obj.pk, ))

    def get_delete(self, obj):
        return reverse('worker_delete', args=(obj.pk, ))


class ShiftSerializer(serializers.ModelSerializer):

    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Shift
        fields = ['id', 'start_hour', 'end_hour', 'absolute_url', ]

    def get_absolute_url(self, obj):
        return reverse('shift_detail', args=(obj.pk, ))


class ShiftDetailSerializer(serializers.ModelSerializer):

    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()

    class Meta:
        model = Shift
        fields = ['id', 'start_hour', 'end_hour', 'update', 'delete']

    def get_update(self, obj):
        return reverse('shift_update', args=(obj.pk, ))

    def get_delete(self, obj):
        return reverse('shift_delete', args=(obj.pk, ))


class WorkPlannerSerializer(serializers.ModelSerializer):

    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = WorkPlanner
        fields = ['id', 'date', 'shift', 'worker', 'absolute_url']

    def get_absolute_url(self, obj):
        return reverse('workplan_detail', args=(obj.pk, ))


class WorkPlannerDetailSerializer(serializers.ModelSerializer):

    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()

    class Meta:
        model = WorkPlanner
        fields = ['id', 'date', 'shift', 'worker', 'update', 'delete']

    def get_update(self, obj):
        return reverse('workplan_update', args=(obj.pk, ))

    def get_delete(self, obj):
        return reverse('workplan_delete', args=(obj.pk, ))


class WorkPlannerDetailCreateSerializer(serializers.ModelSerializer):

    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()

    class Meta:
        model = WorkPlanner
        fields = ['id', 'date', 'shift', 'worker', 'update', 'delete']

    def get_update(self, obj):
        return reverse('workplan_update', args=(obj.pk, ))

    def get_delete(self, obj):
        return reverse('workplan_delete', args=(obj.pk, ))

    def validate(self, data):
        '''
        Custom Validator to check if a worker has already a shift in a day
        '''
        current_obj = dict(data)
        worker_shifts = WorkPlanner.objects.filter(date=current_obj['date'],
                                                   worker=current_obj['worker'])

        if worker_shifts.count():
            raise ValidationError({'worker': "The worker is already working a shift on the selected date."})

        return data
