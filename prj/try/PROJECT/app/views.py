from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi,BaseView,expose

from . import appbuilder, db
from .models import Usertable



from flask_appbuilder.security.registerviews import RegisterUserDBView






class UsertableView(ModelView):
    datamodel = SQLAInterface(Usertable)

    show_fieldsets = [("Create Account",
    {"fields":['aadhaar','fname','lname','gender','dob','email','mobile','password']})]

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

class RegisterView(BaseView):
    route_base = "/registerview"

    @expose('/register/')
    def register(self):
        # do something with param1
        # and return it
        return render_template("register.html",base_template=appbuilder.base_template,appbuilder=appbuilder)

db.create_all()
appbuilder.add_view(
    UsertableView,
    "List Groups",
    icon="fa-folder-open-o",
    category="Create Account",
    category_icon="fa-envelope",
)