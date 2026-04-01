from django.test import TestCase
from django.db import IntegrityError
from .models import Task, Status


class TaskTestCase(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            name="Test Task",
            status=Status.UNSTARTED
        )

    def test_create_task(self):
        self.assertEqual(self.task.name, "Test Task")
        self.assertEqual(self.task.status, Status.UNSTARTED)

    def test_update_task(self):
        self.task.name = "Updated Task"
        self.task.status = Status.ONGOING
        self.task.save()

        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.name, "Updated Task")
        self.assertEqual(updated_task.status, Status.ONGOING)

    def test_delete_task(self):
        self.task.delete()
        self.assertEqual(Task.objects.count(), 0)

    def test_duplicate_task(self):
        # setUp already created "Test Task"
        with self.assertRaises(IntegrityError):
            Task.objects.create(name="Test Task", status=Status.UNSTARTED)

    def test_status_choices(self):
        task = Task.objects.create(name="New Task", status=Status.FINISHED)
        self.assertIn(task.status, [choice[0] for choice in Status.choices])

    def test_str_method(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_task_count(self):
        self.assertEqual(Task.objects.count(), 1)