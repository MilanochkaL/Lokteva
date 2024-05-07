import unittest
import myform

class Test_test_email(unittest.TestCase):
    def test_invalid_emails(self):
        list_mail_uncor = ["", "1", "m1@", "@mail", "m@m@mail.ru", "?23@mail.ru", "12123@mail..r",
                           "abc@deffg.uoop", "abc@f.g", "abc@def@ghi.com", "abc@def,com", "abc@def;com", "abc@123.com", "abc@.com"]
        for email in list_mail_uncor:
            self.assertFalse(myform.check_email_d(email))

    def test_valid_emails(self):
        list_mail_cor = ["mm@mail.ru", "m1@gmail.com", "test@example.com", "johnDoe@domain.co.uk",
                         "jane_doe@sub.example.org", "aa@bd.cc"]
        for email in list_mail_cor:
            self.assertTrue(myform.check_email_d(email))

if __name__ == '__main__':
    unittest.main()
