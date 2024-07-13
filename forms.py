from flask_wtf import FlaskForm
from wtforms import StringField, TelField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

phone_regex = r'^\d{3}-\d{3}-\d{4}$'

class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=80)])
    phone = StringField('Phone Number', validators=[DataRequired(), Regexp(phone_regex, message="Phone number must be in xxx-xxx-xxxx format")])
    
    heard_about = SelectField('How Did You Hear About Us?', 
                              choices=[('0', 'Google Search'), 
                                       ('1', 'Social Media'),
                                       ('2', 'Referral'), 
                                       ('3', 'Flyer Advertisement'), 
                                       ('4', 'Other')],
                              validators=[DataRequired()])
    property_type = SelectField('Property Type?', 
                                choices=[('0', 'House'), 
                                         ('1', 'Apartment'), 
                                         ('2', 'Office'), 
                                         ('3', 'Retail Space'), 
                                         ('4', 'Other')],
                                validators=[DataRequired()])
    special_attention = TextAreaField('Are There Any Specific Areas or Items That Require Special Attention?',
                                      validators=[Length(max=500)])  
    other_message = TextAreaField("Is There Anything Else You'd Like Us To Know?",
                                  validators=[Length(max=500)]) 
    
    def format_data(self):
        # Mapping for select fields
        heard_about_mapping = dict(self.heard_about.choices)
        property_type_mapping = dict(self.property_type.choices)
        
        formatted_data = []
        
        # Iterate through each field in the form
        for field in self:
            if field.name == 'csrf_token':
                continue
            if field.name == 'heard_about':
                value = heard_about_mapping.get(field.data, 'Unknown')
            elif field.name == 'property_type':
                value = property_type_mapping.get(field.data, 'Unknown')
            else:
                value = field.data
            
            formatted_data.append(f"{field.label.text}: {value}")
        
        return "\n".join(formatted_data)