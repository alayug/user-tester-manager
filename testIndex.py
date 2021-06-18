import unittest
from index import insertTask, id, taskName, message

class TestInsertTask(unittest.TestCase):

    def testInsertTaskSuccessfully(self):
        # Set the variables for insertTask
        id.set("1")
        taskName.set("Test Task Name")

        # Expected message after insertTask is invoked
        expectedMessage = "Task inserted successfully!"

        # Invoke insertTask
        insertTask()

        # Expect the message to equal expectedMessage
        self.assertEqual(message, expectedMessage)