import unittest
from validators.insertUserValidator import firstNameValidator

# why does test not run when in tests folder?
class InsertUserValidatorTestCase(unittest.TestCase):
    def test_first_name_validator_return_empty_string_if_not_empty_and_only_letters(self):
        result = firstNameValidator("validFirstName")
        self.assertEqual(result, "")
    def test_first_name_validator_return_cant_be_empty_message_if_first_name_is_blank(self):
       result = firstNameValidator("")
       self.assertEqual(result, "First name can't be empty!")
    def test_first_name_validator_return_invalid_message_if_first_name_is_invalid(self):
        result = firstNameValidator("invalid name")
        self.assertEqual(result, "First name must only contain letters!")


if __name__=="__main__":
    unittest.main()