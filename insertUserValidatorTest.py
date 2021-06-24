import unittest
from validators.insertUserValidator import firstNameValidator

# why does test not run when in tests folder?
class InsertUserValidatorTestCase(unittest.TestCase):
   def test_first_name_validator_return_empty_string_if_not_empty_and_only_letters(self):
       result = firstNameValidator("validFirstName")
       self.assertEqual(result, "")


if __name__=="__main__":
    unittest.main()