from flask import Flask 
from flask import render_template, request
from flask_bootstrap import Bootstrap
from wtforms import FloatField , SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kkbb'
Bootstrap(app)


class Info(FlaskForm):
	HoursPerWeek=FloatField("enter the hours per week: ",validators=[DataRequired()])
	APM=FloatField("enter the action per minute: ",validators=[DataRequired()])
	SelectByHotkeys=FloatField("enter the Number of unit or building selections made using hotkeys per timestamp: ",validators=[DataRequired()])
	AssignToHotkeys=FloatField("enter the Number of units or buildings assigned to hotkeys per timestamp: ",validators=[DataRequired()])
	UniqueHotkeys=FloatField("enter the  Number of unique hotkeys used per timestamp : ",validators=[DataRequired()])
	MinimapAttacks=FloatField("enter the Number of attack actions on minimap per timestamp: ",validators=[DataRequired()])
	MinimapRightClicks=FloatField("enter the number of right-clicks on minimap per timestamp: ",validators=[DataRequired()])
	NumberOfPACs=FloatField("enter the  Number of PACs per timestamp: ",validators=[DataRequired()])
	GapBetweenPACs=FloatField("enter the Mean duration in milliseconds between PACs: ",validators=[DataRequired()])
	ActionLatency=FloatField("enter the  Mean latency from the onset of a PACs to their first action in milliseconds",validators=[DataRequired()])
	TotalMapExplored=FloatField("enter the number of 24x24 game coordinate grids viewed by the player per timestamp: ",validators=[DataRequired()])
	WorkersMade=FloatField("enter the  Number of SCVs, drones, and probes trained per timestamp: ",validators=[DataRequired()])
	submit=SubmitField("predict")


@app.route('/',methods=["GET" , "POST"])
def show_form():
	formi=Info()	
	if request.method =="POST" and formi.validate_on_submit():
		model=joblib.load("model_randomf")
		pred=str(model.predict([[formi.HoursPerWeek.data ,formi.APM.data,formi.SelectByHotkeys.data,formi.AssignToHotkeys.data,formi.UniqueHotkeys.data,formi.MinimapAttacks.data, formi.MinimapRightClicks.data , formi.NumberOfPACs.data , formi.GapBetweenPACs.data ,formi.ActionLatency.data , formi.TotalMapExplored.data , formi.WorkersMade.data]]))
		return render_template('result.html',pred=pred[1:len(pred)-1])
	return render_template('form.html' , form=formi)


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000 , debug=True)