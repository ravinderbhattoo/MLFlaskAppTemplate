from flask import request
from main import create_model_report, single_model_predict

def create_routes(app, models):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        str_ = "<b>Model hosted on this path are:</b> <br>"
        for ind, model in enumerate(models):
            str_ = str_ + "<div style='margin-top:40px'>"
            str_ = str_ + f"<a href='{model}'><i>{ind+1}. {model}</i></a>"
            str_ = str_ + f"<p></p>"
            str_ = str_ + f"<a href='{model}/test'><i>{ind+1}. {model} test</i></a><br>"
            str_ = str_ + "</div>"
        return str_

    @app.route('/<string:modelname>/', methods=['GET', 'POST'])
    def model_route(modelname):
        if request.method == "POST":
            data = request.json
            return single_model_predict(models[modelname], data['X'])
        else:
            return create_model_report(models[modelname], modelname)

    @app.route('/<string:modelname>/test')
    def model_route_test(modelname):
        return single_model_predict(models[modelname], models[modelname]['X_test'][:10])

    @app.route('/allmodels/', methods=['GET', 'POST'])
    def allmodel_route():
        if request.method == "POST":
            data = request.json
            return {modelname: single_model_predict(models[modelname], data['X']) for modelname in data['models']}
        else:
            return home()
