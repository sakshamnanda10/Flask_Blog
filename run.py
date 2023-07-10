

from flaskblog import create_app


app = create_app()

if __name__=='__main__':
    app.secret_key = '4aa7ec421f7a8cdaceffec0693fd58c3'
    app.run(debug=True)