from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

class TestCheckoutForms(TestCase):

    def test_order_form_is_valid_with_all_the_fields_filled(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'111111', 
            'country':'UK', 
            'postcode':'SE11', 
            'town_or_city':'London', 
            'street_address1':'street',
            'street_address2':'street2',  
            'county':'London'})
        self.assertTrue(order_form.is_valid())

    def test_order_form_is_valid_if_all_fields_are_filled_apart_from_postcode(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'111111', 
            'country':'UK', 
            'postcode':None, 
            'town_or_city':'London', 
            'street_address1':'street',
            'street_address2':'street2',  
            'county':'London'})
        self.assertTrue(order_form.is_valid())
    
    def test_order_form_is_not_valid_if_full_name_is_empty(self):
        order_form = OrderForm({
            'full_name':None,
            'phone_number':'111111', 
            'country':'UK', 
            'postcode':'SE11', 
            'town_or_city':'London', 
            'street_address1':'street',
            'street_address2':'street2',  
            'county':'London'})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['full_name'],[u'This field is required.'])
    
    def test_order_form_is_not_valid_if_phone_number_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':None, 
            'country':'UK', 
            'postcode':'SE11', 
            'town_or_city':'London', 
            'street_address1':'street',
            'street_address2':'street2',  
            'county':'London'})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['phone_number'],[u'This field is required.'])
    
    def test_order_form_is_not_valid_if_country_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'111111', 
            'country':None, 
            'postcode':'SE11', 
            'town_or_city':'London', 
            'street_address1':'street',
            'street_address2':'street2',  
            'county':'London'})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['country'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_town_or_city_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'111111', 
            'country':'UK', 
            'postcode':'SE11', 
            'town_or_city':None, 
            'street_address1':'street',
            'street_address2':'street2',  
            'county':'London'})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['town_or_city'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_street_address1_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'111111', 
            'country':'UK', 
            'postcode':'SE11', 
            'town_or_city':'London', 
            'street_address1':None,
            'street_address2':'street2',  
            'county':'London'})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['street_address1'],[u'This field is required.'])

    def test_order_form_is_not_valid_if_street_address2_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'111111', 
            'country':'UK', 
            'postcode':'SE11', 
            'town_or_city':'London', 
            'street_address1':'street',
            'street_address2':None,  
            'county':'London'})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['street_address2'],[u'This field is required.'])
    
    def test_order_form_is_not_valid_if_street_address2_is_empty(self):
        order_form = OrderForm({
            'full_name':'name',
            'phone_number':'111111', 
            'country':'UK', 
            'postcode':'SE11', 
            'town_or_city':'London', 
            'street_address1':'street',
            'street_address2':'street2',  
            'county':None})
        self.assertFalse(order_form.is_valid())
        self.assertEqual(order_form.errors['county'],[u'This field is required.'])
    






