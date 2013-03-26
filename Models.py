import datetime
from google.appengine.ext import db
from google.appengine.api import users


class Site_User(db.Model):
    userid = db.StringProperty()
    name = db.StringProperty()
    email = db.StringProperty()
    company = db.StringProperty()
    account_type = db.StringProperty(choices=set(["employer", "employee", "admin"]))

class Payslip(db.Model):
    ownerid = db.StringProperty()
    upload_date = db.DateProperty(auto_now_add=True)
    beginning =  db.DateProperty()
    ending =  db.DateProperty()
    income = db.FloatProperty()
    tax = db.FloatProperty()
    net = db.FloatProperty()
    company = db.StringProperty()
    file = db.BlobProperty()
    
class File(db.Model):
    ownerid = db.StringProperty()
    title = db.StringProperty()
    description = db.StringProperty()
    upload_date = db.DateProperty(auto_now_add=True)
    file = db.BlobProperty()
        
def payslip_key(owner_id):
  return db.Key.from_path('Payslip', owner_id)

def file_key(owner_id):
  return db.Key.from_path('File', owner_id)

    

