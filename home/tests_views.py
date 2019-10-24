from django.test import TestCase, Client

c=Client()

# Create your tests here.
class TestHomeViews(TestCase):
  
    def test_index_page(self):
        page = c.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_about_page(self):
        page = c.get("/home/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_adonate_page(self):
        page = c.get("/home/donate/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "donate.html")    
    
    def test_projects_page(self):
        page = c.get("/home/projects/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "projects.html")    

    def test_contact_page(self):
        page = c.get("/home/contact/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact.html")    
    