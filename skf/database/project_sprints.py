
from skf.database import db

'''
--
-- Table structure for table `project_sprints`
--
drop table if exists `project_sprints`;
CREATE TABLE `project_sprints` (
`sprint_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`project_id` int(11) NOT NULL,
`group_id` int(11) NOT NULL,
`sprint_name` varchar(250) NOT NULL,
`sprint_description` varchar(250) NOT NULL
);
'''

class ProjectSprint(db.Model):
    
    __tablename__ = "project_sprints"

    sprint_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    description = db.Column(db.Text)

    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship('Group', backref=db.backref("sprints"))

    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    project = db.relationship('Project', backref=db.backref("sprints"))

    checklist_type_id = db.Column(db.Integer, db.ForeignKey("checklist_types.id"))
    checklist_type = db.relationship('ChecklistType', backref=db.backref("sprints"))

    def __init__(self, name, description):
        self.name = name
        self.description = description
 