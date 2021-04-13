from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_create_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            self.open_manage_page()
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/mantisbt-1.2.20/"):
            wd.get("http://localhost/mantisbt-1.2.20/")

    def open_manage_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()


    def create(self, project):
        wd = self.app.wd
        self.open_manage_page()
        self.open_create_page()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def open_manage_section(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a i[class='fa fa-gears menu-icon']").click()
        wd.find_element_by_css_selector("ul[class='nav nav-tabs padding-18'] li:nth-child(3)").click()

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_value("name", project.name)
        self.change_value("description", project.description)

    def delete(self, id):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

