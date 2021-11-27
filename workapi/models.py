from django.db import models


# Create your models here.
class Shift(models.Model):
    '''
    Model Class for storing Shifts definitions
    '''
    start_hour = models.IntegerField(blank=False, default=0)
    end_hour = models.IntegerField(blank=False, default=8)

    def __str__(self):
        return f'{self.start_hour}-{self.end_hour}'

    @property
    def length(self):
        '''
        Returns the length in hours of a shift
        '''
        return self.end_hour - self.start_hour

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'
        unique_together = ('start_hour', 'end_hour',)
        ordering = ('start_hour',)


class Worker(models.Model):
    '''
    Model Class for storing Workers data
    '''
    personal_id = models.CharField(primary_key=True, max_length=50,
                                   blank=False, unique=True, help_text="")
    name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=245, blank=False)
    phone_number = models.CharField(max_length=10,
                                    blank=False)

    def __str__(self):
        return f'[{self.personal_id}] {self.last_name.capitalize()}, \
                 {self.name.capitalize()}'

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
        ordering = ('personal_id', )


class WorkPlanner(models.Model):
    '''
    Model Class for storing Weekly Calendar Schedules.
    '''

    date = models.DateField(blank=False)
    shift = models.ForeignKey(Shift, related_name='assigned_work_plan',
                              on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='assigned_work_plan',
                               on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.date.strftime('%Y-%m-%d')}) {self.shift} {self.worker}"

    class Meta:
        unique_together = ('date', 'shift', 'worker')
        verbose_name = 'Work Planner'
        verbose_name_plural = 'Work Planner'
        ordering = ('date', 'shift', 'worker',)
