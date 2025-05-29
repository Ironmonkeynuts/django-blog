from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title='About Me',
            content='This is the about me.'
        )
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Tests that the about page renders with a collaborate form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'],
            CollaborateForm
        )

    def test_successful_collaboration_request_submission(self):
        """Tests for a successful collaboration submission"""
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello, I would like to collaborate.'
        }
        response = self.client.post(reverse('about'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)
