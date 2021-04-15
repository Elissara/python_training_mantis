from fixture.project import Project
import random


def test_del_project(app):
    if len(app.soap.get_projects_list()) == 0:
        app.project.create(Project(name="Test_project_007"))
    old_list_of_projects = app.soap.get_projects_list()
    project = random.choice(old_list_of_projects)
    app.project.delete(project.id)
    new_list_of_projects = app.soap.get_projects_list()
    old_list_of_projects.remove(project)
    assert sorted(old_list_of_projects, key=Project.max_id) == sorted(new_list_of_projects, key=Project.max_id)

