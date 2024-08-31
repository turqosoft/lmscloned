# your_custom_app/api.py
import frappe

@frappe.whitelist(allow_guest=True)
def submit_cart_endpoint(cart_items):
    try:
        for item in cart_items:
            doc = frappe.get_doc({
                'doctype': 'Material Requirement',
                'items': [{
                    'item_code': item['id'],
                    'qty': item['quantity'],
                    # Add other required fields
                }],
                # Add any additional fields required by Material Requirement
            })
            doc.insert()
        return {'status': 'success'}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), 'Material Requirement Submission Error')
        return {'status': 'error', 'message': str(e)}
import frappe

@frappe.whitelist(allow_guest=True)
def create_material_requirement(doc):
    """Create a new Material Requirement record."""
    try:
        # Parse the incoming doc
        new_doc = frappe.get_doc(doc)
        # Insert the new document
        new_doc.insert()
        # Return the name of the newly created document
        return new_doc.name
    except Exception as e:
        # Log the error
        frappe.log_error(frappe.get_traceback(), 'Create Material Requirement Failed')
        # Return the error message
        return str(e)

@frappe.whitelist(allow_guest=True)
def update_material_requirement(name, **kwargs):
    """Update an existing Material Requirement record."""
    try:
        # Fetch the existing document
        doc = frappe.get_doc('Material Requirement', name)
        # Update the fields
        for field, value in kwargs.items():
            setattr(doc, field, value)
        # Save the changes
        doc.save()
        # Return the name of the updated document
        return doc.name
    except Exception as e:
        # Log the error
        frappe.log_error(frappe.get_traceback(), 'Update Material Requirement Failed')
        # Return the error message
        return str(e)

@frappe.whitelist(allow_guest=True)
def get_material_requirement(name):
    """Fetch an existing Material Requirement record."""
    try:
        # Fetch the existing document
        doc = frappe.get_doc('Material Requirement', name)
        # Return the document data as a dictionary
        return doc.as_dict()
    except Exception as e:
        # Log the error
        frappe.log_error(frappe.get_traceback(), 'Get Material Requirement Failed')
        # Return the error message
        return str(e)
