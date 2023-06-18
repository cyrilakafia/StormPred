from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    molecule_id = IntegerField(label='Molecule ID', validators=[DataRequired(message="Please enter a valid integer for the molecule ID.")])
    smiles = StringField(label='SMILES', validators=[DataRequired(message="Please enter a SMILES string.")])
    model_type = SelectField(label='Algorithm', choices=[('XGBoost', 'XGBoost'), ('AdaBoost', 'AdaBoost'), ('Random Forest', 'Random Forest')], validators=[DataRequired()])
    submit = SubmitField(label='Predict')
