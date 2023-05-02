from django.test import TestCase
from .models import ParkingFloor, ParkingSpot, Address, AccountStatus, ParkingTicketStatus, spotStatus, Floor_type, \
    Operators, DisplayBoard, PaymentCounter


class ModelTestCases(TestCase):
    """This class defines the test suite for the Address model."""

    def setUp(self):
        self.address = Address(street_name="test street", city="test city", state="test state", zip_code="test zip")

    def test_model_can_create_a_address(self):
        """Test the address model can create a address."""
        d = self.address
        self.assertTrue(isinstance(d, Address))

    def test_model_can_address_count(self):
        """Test the address model can create a address."""
        d = self.address
        d.save()
        self.assertEqual(Address.objects.count(), 1)



class OperatorTestCase(TestCase):
    def setUp(self):
        self.operator = Operators(name="test name", email="test email", phone_number="test phone",account_status=AccountStatus.ACTIVE)

    def test_model_can_create_a_operator(self):
        """Test the address model can create a address."""
        d = self.operator
        self.assertTrue(isinstance(d, Operators))
    def test_model_str_method(self):
        d = self.operator
        self.assertEqual(str(d), d.name)



class DisplayBoardTestCase(TestCase):
    def setUp(self):
        self.displayboard = DisplayBoard(name="test name", message="test message")

    def test_model_can_create_a_displayboard(self):
        """Test the address model can create a address."""
        d = self.displayboard
        self.assertTrue(isinstance(d, DisplayBoard))
    def test_model_str_method(self):
        d = self.displayboard
        self.assertEqual(str(d), d.name)

class PaymentCounterTestCase(TestCase):
    def setUp(self):

        self.paymentcounter = PaymentCounter(name="test name",counter_number=1,amount=100,parking_lot=1)

    def test_model_can_create_a_paymentcounter(self):
        """Test the address model can create a address."""
        d = self.paymentcounter
        self.assertTrue(isinstance(d, PaymentCounter))
    def test_model_str_method(self):
        d = self.paymentcounter
        self.assertEqual(str(d), d.name)

    def test_model_sum_method(self):
        d = self.paymentcounter
        self.assertEqual(d.amount, 100)