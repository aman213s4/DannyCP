from flask import Flask
app = Flask(__name__)

@app.router('/')
def hello_world():
  return 'SirAdmin'

if __name__ == "__main__":
  app.run()