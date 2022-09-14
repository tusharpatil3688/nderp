// Copyright (c) 2022, nderp and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Ticket System Analytics"] = {
	"filters": [
		{
			"fieldname":"reporting_date",
			"label": __("Reporting Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()	
		},
		{
			"fieldname":"required_by",
			"label": __("Required By"),
			"fieldtype": "Date"
			//"default": frappe.datetime.get_today()	
		},
		{
			"fieldname":"status",
			"label": __("Ticket Status"),
			"fieldtype": "Select",
			"options": ["Draft", "Ticket Raised", "Ticket Assigned", "Pending For Testing", "Tested", "Closed", "Cancelled"]	
		}
	]
};
