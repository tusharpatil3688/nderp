// Copyright (c) 2022, nderp and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket System', {
	setup: function(frm){
		if (frm.doc.user == "" || frm.doc.user == null) {
			frm.doc.user = frappe.session.user;
		}

		frappe.db.get_value("User and Project Mapping", { user : frm.doc.user }, "project", (r) => {
			//console.log(r);
			frm.set_value("project", r.project);
		})
	},
	required_by : function(frm){
		validate_dates(frm);
	},
	validate: function(frm){
		validate_dates(frm);
	},
	reporting_date: function(frm){
		validate_dates(frm);
	}
});

function validate_dates(frm){
	if(frm.doc.reporting_date > frm.doc.required_by){
		frappe.throw("Required By date can not be less than reporting date.")
	}
}

