import logging
import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/alert', methods = ['POST'])
def postAlertmanager():

    content = json.loads(request.get_data())
    with open("Output.txt", "w") as text_file:
        text_file.write("{0}".format(content))
    try:

        for alert in content['alerts']:

            if 'name' in alert['labels']:

                message = """
Status """+alert['status']+"""
Alertname: """+alert['labels']['alertname']+"""
Instance: """+alert['labels']['instance']+"""("""+alert['labels']['name']+""")
"""+alert['annotations']['description']+"""
"""
            else:
                message = """
Status """+alert['status']+"""
Alertname: """+alert['labels']['alertname']+"""
Instance: """+alert['labels']['instance']+"""
"""+alert['annotations']['description']+"""
"""
            print(message)
            return "Alert OK", 200
    except:
        print("Failed to send via Flask to Telegram!")
        return "Alert nOK", 200

if __name__ == '__main__':
    logging.basicConfig(filename='flaskAlert.log',level=logging.INFO)
    app.run(host='0.0.0.0', port=9119)
