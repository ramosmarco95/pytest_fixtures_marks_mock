import pytest
from unittest.mock import MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.task_service import TaskService

# Test fixture
@pytest.fixture
def task_service():
    service = TaskService()
    service.task_model = MagicMock()  # Mock the database interactions
    return service

# Test add_task method
def test_add_task(task_service):
    task_service.task_model.add_task.return_value = True
    assert task_service.add_task("Buy milk", "Get from store", "Errands", "medium", "2025-02-20") is True

    with pytest.raises(ValueError):
        task_service.add_task("", "Get from store", "Errands", "medium", "2025-02-20")

    with pytest.raises(ValueError):
        task_service.add_task("Buy milk", "Get from store", "Errands", "urgent", "2025-02-20")

# Test get_tasks_by_priority
@pytest.mark.priority
def test_get_tasks_by_priority(task_service):
    task_service.task_model.get_all_tasks.return_value = [
        {
            "id": 1,
            "title": "Task A",
            "description": "Task A description",  # Added missing keys
            "category": "Work",
            "priority": "high",
            "due_date": "2025-12-31",
            "status": "Incomplete",
        },
        {
            "id": 2,
            "title": "Task B",
            "description": "Task B description",
            "category": "Personal",
            "priority": "medium",
            "due_date": "2025-12-31",
            "status": "Incomplete",
        },
    ]

    tasks = task_service.get_tasks_by_priority("high")
    
    assert len(tasks) == 1
    assert tasks[0]["Priority"] == "high"


# MonkeyPatch example
import random

class RandomNumberGenerator:
    def get_random(self):
        return random.randint(1, 100)

def test_random_generator(monkeypatch):
    def mock_random(self):
        return 42  # Fixed return value

    monkeypatch.setattr(RandomNumberGenerator, "get_random", mock_random)

    rng = RandomNumberGenerator()
    assert rng.get_random() == 42  # Should return the mocked value
