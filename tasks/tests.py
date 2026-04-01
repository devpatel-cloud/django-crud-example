from django.test import TestCase
from django.db import IntegrityError
from .models import Task, Status


class TaskTestCase(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            name="Test Task",
            status=Status.UNSTARTED
        )

    # ✅ Create Test
    def test_create_task(self):
        self.assertEqual(self.task.name, "Test Task")
        self.assertEqual(self.task.status, Status.UNSTARTED)

    # ✅ Update Test
    def test_update_task(self):
        self.task.name = "Updated Task"
        self.task.status = Status.ONGOING
        self.task.save()

        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.name, "Updated Task")
        self.assertEqual(updated_task.status, Status.ONGOING)

    # ✅ Delete Test
    def test_delete_task(self):
        self.task.delete()
        self.assertEqual(Task.objects.count(), 0)

    # ✅ Duplicate Name Test (only works if unique=True in model)
    def test_duplicate_task(self):
        Task.objects.create(name="Duplicate Task", status=Status.UNSTARTED)
        with self.assertRaises(IntegrityError):
            Task.objects.create(name="Duplicate Task", status=Status.UNSTARTED)

    # ✅ Status Choices Test
    def test_status_choices(self):
        task = Task.objects.create(
            name="New Task",
            status=Status.FINISHED
        )
        valid_choices = [choice[0] for choice in Status.choices]
        self.assertIn(task.status, valid_choices)

    # ✅ String Method Test
    def test_str_method(self):
        self.assertEqual(str(self.task), "Test Task")

    # ✅ Count Test
    def test_task_count(self):
        self.assertEqual(Task.objects.count(), 1)

    # 🔥 Extra: Default Status Test (if you have default)
    def test_default_status(self):
        task = Task.objects.create(name="Default Status Task")
        self.assertEqual(task.status, Status.UNSTARTED)