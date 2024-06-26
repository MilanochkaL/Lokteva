import unittest
import myform

class Test_test_email(unittest.TestCase):
    def test_invalid_emails(self):
        list_mail_uncor = ["", "1", "m1@", "@mail", "m@m@mail.ru", "?23@mail.ru", "12123@mail..r",
                           "1abc@deffg.uoop", "abc@f.g", "abcdabadsgjhsjdhsjhsjdhsdkajskahdef@ghi.com", "ac@f.com", "abc@dm", "abc@123.com", "abc@.com"]
        for email in list_mail_uncor:
            self.assertFalse(myform.check_email_d(email), email)

    def test_valid_emails(self):
        list_mail_cor = ["mms@mail.ru", "md1@gmail.com", "test@example.com", "johnDoe@domain.co.uk",
                         "jane_doe@sub.example.org", "daa@bd.cc"]
        for email in list_mail_cor:
            self.assertTrue(myform.check_email_d(email), email)

if __name__ == '__main__':
    unittest.main()
