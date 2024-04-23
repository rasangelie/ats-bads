# from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from authentication.models import User
from tickets.models import Ticket, JobPosition, TechStack

class TicketModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.job_position = JobPosition.objects.create(position='Developer')
        self.tech_stack = TechStack.objects.create(tech_stack='Python')
        self.ticket = Ticket.objects.create(
            first_name='Test',
            middle_initial='T',
            last_name='User',
            email_address='testuser@example.com',
            job_position=self.job_position,
            resume_url='http://example.com/resume.pdf',
            tech_stacks=self.tech_stack,
            assignees=self.user
        )

    def test_ticket_has_assignee(self):
        self.assertEqual(self.ticket.assignees, self.user)