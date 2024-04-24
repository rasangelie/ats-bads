# from django.test import TestCase

# Create your tests here.
# from django.test import TestCase
# from authentication.models import User
# from tickets.models import Ticket, JobPosition, TechStack

# class TicketModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.job_position = JobPosition.objects.create(position='Developer')
#         self.tech_stack = TechStack.objects.create(tech_stack='Python')
#         self.ticket = Ticket.objects.create(
#             first_name='Test',
#             middle_initial='T',
#             last_name='User',
#             email_address='testuser@example.com',
#             job_position=self.job_position,
#             resume_url='http://example.com/resume.pdf',
#             tech_stacks=self.tech_stack,
#             assignees=self.user
#         )

#     def test_ticket_has_assignee(self):
#         self.assertEqual(self.ticket.assignees, self.user)

from django.test import TestCase
from .models import Ticket, JobPosition
from authentication.models import User
from auditlog.models import LogEntry

class TicketAuditLogTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com', password='test')
        self.job_position = JobPosition.objects.create(position='Developer')
        self.ticket = Ticket.objects.create(first_name='Test', last_name='User', email_address='test@example.com', assignees=self.user, job_position=self.job_position)

    def test_audit_log_on_update(self):
        self.ticket.progress = Ticket.TicketProgressChoices.APPLICATION  # Change this to a valid value for your progress field
        self.ticket.save()

        log_entry = LogEntry.objects.get(object_id=str(self.ticket.id))
        self.assertEqual(log_entry.action, LogEntry.Action.UPDATE)
        self.assertIn('progress', log_entry.changes)

    def test_audit_log_on_updated_at(self):
        self.ticket.first_name = 'Updated'  # Make a change to update the 'updated_at' field
        self.ticket.save()

        log_entry = LogEntry.objects.get(object_id=str(self.ticket.id))
        self.assertEqual(log_entry.action, LogEntry.Action.UPDATE)
        self.assertIn('updated_at', log_entry.changes)