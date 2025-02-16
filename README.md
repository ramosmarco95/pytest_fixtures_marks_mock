# pytest_fixtures_marks_mock
This assignment focuses on writing and organizing tests using pytest with fixtures, custom marks, and monkeypatching techniques. 
Test Fixtures:

Implement a Python class with at least two methods.
Create a pytest fixture that returns a new instance of the class.
Write test functions that utilize the fixture.

Registering Marks:

Configure a pytest.ini file to register custom marks.
Apply custom marks to test functions.
Run and verify that marked tests execute without warnings.

MonkeyPatching:

Create a class with a method returning a random value.
Use monkeypatch to override the method with a mock function.
Ensure the mocked method returns a static value in tests.