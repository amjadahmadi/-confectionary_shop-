import datetime

from django.test import TestCase
from .models import Discount_Code
import pytz


# Create your tests here.

class Discount_CodeTestCase(TestCase):
    def setUp(self) -> None:
        self.te = Discount_Code.objects.create(discount_name='sample',
                                               start_date=datetime.datetime(2009, 8, 19, tzinfo=pytz.UTC),
                                               end_date=datetime.datetime(2009, 8, 20, tzinfo=pytz.UTC),amount=20.,percent=True)

    def test_dis(self):
        self.assertEqual(self.te.percent, True)



# class ProfileTestCase(TestCase):
#     def setUp(self) -> None:
#         self.pf = Profile.objects.create(email='a@a.com', gender='MA',
#                                          birth_day=datetime.datetime(2009, 8, 19, tzinfo=pytz.UTC))
#
#     def test_profile(self):
#         self.assertEqual(self.pf.gender, "MA")
#         self.assertEqual(self.pf.birth_day, datetime.datetime(2009, 8, 19, tzinfo=pytz.UTC))
#
#
# class UserTestCase(TestCase):
#     def setUp(self) -> None:
#         self.ba = Bank_Account.objects.create(balance=250000, card_bank='6037701596552134')
#         self.pf = Profile.objects.create(email='a@a.com', gender='MA',
#                                          birth_day=datetime.datetime(2009, 8, 19, tzinfo=pytz.UTC))
#         self.us = User.objects.create(phone='09120793109', profile=self.pf, bank_account=self.ba)
#
#     def test_user(self):
#         self.assertEqual(self.us.profile.email, "a@a.com")
#         self.assertEqual(self.us.bank_account.card_bank, '6037701596552134')
#
#
# class AddressTestCase(TestCase):
#     def setUp(self) -> None:
#         self.ba = Bank_Account.objects.create(balance=250000, card_bank='6037701596552134')
#         self.pf = Profile.objects.create(email='a@a.com', gender='MA',
#                                          birth_day=datetime.datetime(2009, 8, 19, tzinfo=pytz.UTC))
#         self.us = User.objects.create(phone='09120793109', profile=self.pf, bank_account=self.ba)
#         self.ad = Addresses.objects.create(full_address='kerman', user=self.us)
#
#     def test_address(self):
#         self.assertEqual(self.ad.full_address, "kerman")
#         self.assertEqual(self.ad.user.phone, "09120793109")
