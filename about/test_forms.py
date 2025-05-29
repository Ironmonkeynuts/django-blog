from django.test import TestCase
from .forms import CollaborateForm


# Create your tests here.
class TestCollaborateForm(TestCase):
    def test_form_is_valid(self):
        """Test for all fields"""
        form = CollaborateForm({
            'name': 'name',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'XXXXXXXXXXXXX2',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name is required")

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm({
            'name': 'name2',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Email is required")

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm({
            'name': 'name3',
            'email': 'XXXXXXXXXXXXX3',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message is required")
