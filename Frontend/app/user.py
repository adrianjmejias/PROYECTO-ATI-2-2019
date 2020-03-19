from flask_mongoengine.wtf import model_form
from wtforms import SubmitField

from wtforms.validators import DataRequired, NumberRange
from app import mongo
from flask_babel import _
from mongoengine.fields import DateTimeField, IntField, StringField, URLField, ListField, ReferenceField, EmailField, BooleanField
import datetime
class Media(mongo.Document):
    __name__ = "media"
    mtype = StringField()
    content = StringField()
    pass

class Question(mongo.Document):
    __name__ = "question"
    question = StringField()
    qtype =  StringField()
    pass

class Certificate(mongo.Document):
    __name__ = "certificate"
    imgUrl = URLField()
    title = StringField(verbose_name= "Title", validators=[DataRequired()])
    description = StringField(verbose_name= "Description", validators=[DataRequired()])
    scoreForTrueFalse = IntField(verbose_name= "Score For True False", validators=[DataRequired(), NumberRange(min=0)] )   
    scoreForSimpleSelection = IntField(verbose_name= "Score For Simple Selection", validators=[DataRequired(), NumberRange(min=0)] )  
    numQuestions = IntField(verbose_name= "numQuestions", validators=[DataRequired(), NumberRange(min=0)] )  
    timeForTest = StringField(verbose_name= "timeForTest", validators=[DataRequired(), NumberRange(min=0)] )  
    submit = SubmitField(verbose_name= 'Save Changes')
    dateCreated = DateTimeField(default= datetime.datetime.utcnow)
    listQuestion = ListField(ReferenceField(Question))
    listQuestionActive = ListField(ReferenceField(Question))



    # users = []
    # pdf url / firm
    pass


class Admin(mongo.Document):
    __name__ = "admin"
    pass

class User(mongo.Document):
    __name__ = "user"
    username = StringField(validators=[DataRequired(),], verbose_name=_("Username"))
    password = StringField(validators=[DataRequired(),])
    listTest = ListField(ReferenceField(Certificate))

    listCert = ListField(ReferenceField(Certificate))

    name = StringField(verbose_name='Name', validators=[DataRequired()])

    lastName = StringField(verbose_name='Last name', validators=[DataRequired()])

    email = EmailField(verbose_name="Email", validators=[DataRequired()])

    profileImageUrl = URLField()

    # birthDate = DateTimeField(verbose_name='Birth Date', validators=[DataRequired()], )

    gender = StringField(verbose_name='Gender', choices=[('Male','Male'),('Female','Female')])

    university = StringField(verbose_name='University/Institution')

    location = StringField(verbose_name='location')    

    remember_me = BooleanField()

    admin = ReferenceField(Admin)

    # submit = SubmitField('Sign Up')

    birthDate = DateTimeField()

    pass

class Test(mongo.Document):
    __name__ = "test"
    idUser = ReferenceField(User)
    idCertificate = ReferenceField(Certificate)
    pass


UserFormSignUp = model_form(User, field_args={'password':{'password': True}, "gender":{"radio" : True}})
UserFormSignIn = model_form(User, field_args={'password':{'password': True}})

CertificateForm = model_form(Certificate)

def GetSignUpForm(form):
    return UserFormSignUp(form)

def GetSignInForm(form):
    return UserFormSignIn(form)

def GetCertificateForm(form):
    return CertificateForm(form)
