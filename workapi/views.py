from rest_framework import generics
from .serializers import WorkerSerializer, WorkerDetailSerializer
from .serializers import ShiftSerializer, ShiftDetailSerializer
from .serializers import WorkPlannerSerializer, WorkPlannerDetailSerializer
from .serializers import WorkPlannerDetailCreateSerializer
from .models import Worker, Shift, WorkPlanner


# Create your views here.
class WorkerListAPIView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'personal_id'
    queryset = Worker.objects.all()
    serializer_class = WorkerDetailSerializer


class WorkerCreateAPIView(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerDetailSerializer


class WorkerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'personal_id'
    queryset = Worker.objects.all()
    serializer_class = WorkerDetailSerializer


class WorkerDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'personal_id'
    queryset = Worker.objects.all()


class ShiftListAPIView(generics.ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Shift.objects.all()
    serializer_class = ShiftDetailSerializer


class ShiftCreateAPIView(generics.CreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftDetailSerializer


class ShiftRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Shift.objects.all()
    serializer_class = ShiftDetailSerializer


class ShiftDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Shift.objects.all()


class WorkPlanneListAPIView(generics.ListAPIView):
    queryset = WorkPlanner.objects.all()
    serializer_class = WorkPlannerSerializer


class WorkPlannerRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = WorkPlanner.objects.all()
    serializer_class = WorkPlannerDetailSerializer


class WorkPlannerCreateAPIView(generics.CreateAPIView):
    queryset = WorkPlanner.objects.all()
    serializer_class = WorkPlannerDetailCreateSerializer


class WorkPlannerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = WorkPlanner.objects.all()
    serializer_class = WorkPlannerDetailSerializer


class WorkPlannerDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = WorkPlanner.objects.all()
