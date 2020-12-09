import unittest
from datetime import datetime

import Bank.cards.card as card_base 

class TestBaseCard(unittest.TestCase):         # test class
    def setUp(self):
        # Nothing much to do here.
        print('TestBaseCard: Set up')

    def tearDown(self):
        # Nothing much to do here.
        print('TestBaseCard: Tear down')

    @classmethod
    def setUpClass(cls):
        print("TestBaseCard: Creating 'base cards' class objects")
        cls.base_card1 = card_base.card(1214, 'Base Customer 1', 12141214, 1234, 1000)
        cls.base_card2 = card_base.card(1215, 'Base Customer 2', 12151215, 4321, 0)

    @classmethod
    def tearDownClass(cls):
        # Nothing much to do here.
        print('TestBaseCard: tearDownClass')

    # Verify check pincode function
    def test_checkCode(self):
        c1 = self.base_card1._card__card_pin
        c2 = self.base_card2._card__card_pin
        
        self.assertIsInstance(c1, int)
        self.assertIsInstance(c2, int)
        self.assertTrue(self.base_card1.checkCode(c1))
        self.assertTrue(self.base_card2.checkCode(c2))
        
        print("TestBaseCard: Function checkCode testing ... Successful")

    # Verify pincode change function
    def test_changePIN(self):
        self.base_card1.changePIN(1234, 2345)
        self.base_card2.changePIN(4321, 2345)
        
        self.assertIsInstance(self.base_card1.checkCode(2345), bool)
        self.assertIsInstance(self.base_card2.checkCode(2345), bool)
        self.assertTrue(self.base_card1.checkCode(2345))
        self.assertTrue(self.base_card2.checkCode(2345))
        
        print("TestBaseCard: Function changePIN testing ... Successful")

    # Verify initial balance
    def test_balance_init(self):
        # Base class can't alter balance, so we can test initial credit.
        
        self.assertIsInstance(self.base_card1.bal_curr, int)
        self.assertIsInstance(self.base_card2.bal_curr, int)
        self.assertEqual(self.base_card1.bal_curr, 1000)
        self.assertEqual(self.base_card2.bal_curr, 0)
        
        print("TestBaseCard: Initial balance testing ... Successful")

