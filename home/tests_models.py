from django.test import TestCase
from .models import ContactUs,Projects,TotalRaised

class TestHomeModels(TestCase):

    def test_can_create_project_with_all_the_fields(self):
        
        project = Projects(
            name = 'Project name',
            target = 1000,
            link_project = "www.test.com"
        )
        self.assertEqual(project.name, 'Project name')
        self.assertEqual("Project name - £1000", str(project))
    
    def test_can_create_contact_us_email_all_the_fields(self):
        
        contactus = ContactUs(
            email = 'email@email.com',
            content = 'random text',
            contact_date = '2018-10-23'
        )
        self.assertEqual(contactus.email, 'email@email.com')
        self.assertEqual("2018-10-23 - email@email.com", str(contactus))

    def test_total_money_raised(self):
        
        totalraised = TotalRaised(
            number_books = 10,
            money_raised = 50.5,
        )
        self.assertEqual(totalraised.number_books, 10)
        self.assertEqual(totalraised.money_raised, 50.5)
        self.assertEqual("£50.5 - 10 books", str(totalraised))

    
    

    
 