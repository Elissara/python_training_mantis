from model.project import Project


def test_add_project(app, json_projects):
    app.session.login("administrator", "root")
    old_list_of_projects = app.soap.get_projects_list()
    project_data = json_projects
    app.project.create(project_data)
    new_list_of_projects = app.soap.get_projects_list()
    old_list_of_projects.append(project_data)
    assert sorted(old_list_of_projects, key=Project.max_id) == sorted(new_list_of_projects, key=Project.max_id)
