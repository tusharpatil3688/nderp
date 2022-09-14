from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data = get_result(filters)
	return columns, data

def get_columns(filters):
	columns = [
		{
			"label": _("Ticket Number"),
			"fieldname": "ticket_no",
			"fieldtype": "Data"
		},
		{
			"label": _("User"),
			"fieldname": "user",
			"fieldtype": "Link",
			"options": "User"
		},
		{
			"label": _("Project"),
			"fieldname": "project",
			"fieldtype": "Link",
			"options": "Ticket Project"
		},
		{
			"label": _("Issue Category"),
			"fieldname": "issue_category",
			"fieldtype": "Link",
			"options":"Issue Category"
		},
		{
			"label": _("Issue Type"),
			"fieldname": "issue_type",
			"fieldtype": "select",
			"options": ["Bug","New Feature"]
		},
		{
			"label": _("Reporting Date"),
			"fieldname": "reporting_date",
			"fieldtype": "Date"
		},
		{
			"label": _("Required by"),
			"fieldname": "required_by",
			"fieldtype": "Date"
		},
		{
			"label": _("Priority"),
			"fieldname": "priority",
			"fieldtype": "Data"
		},
		{
			"label": _("Current Status"),
			"fieldname": "cur_status",
			"fieldtype": "Data"
		}		
	]
	return columns

def get_result(filters):
	query = """
				SELECT name,user, project, issue_category, issue_type, reporting_date, required_by, priority,
				case when workflow_state!='Closed' AND CAST(CURRENT_DATE() AS DATE)>CAST(required_by AS DATE) THEN 'Overdue'
				ELSE  workflow_state end as workflow_state
				FROM `tabTicket System`
			"""

	query_data = frappe.db.sql(query, as_dict = True, debug = 1)

	data = []
	for q_data in query_data:
		row = {
			"ticket_no":q_data.name,
			"user" : q_data.user,
			"project" : q_data.project,
			"issue_category" : q_data.issue_category,
			"issue_type" : q_data.issue_type,
			"reporting_date" : q_data.reporting_date,
			"required_by" : q_data.required_by,
			"priority" : q_data.priority,
			"cur_status": q_data.workflow_state
		}
		data.append(row)
	return data