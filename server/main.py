from flask import render_template
from app import create_app, setup_database

def add_vue_routes(app):
    @app.route('/')
    def serve_vue_app():
        """
        Server our vue app
        """
        return(render_template('index.html'))

    @app.after_request
    def add_header(req):
        """
        Clear Cache for hot-reloading
        """
        req.headers['Cache-Control'] = 'no-cache'
        return req

app = create_app()
add_vue_routes(app)
setup_database(app)

if __name__ == '__main__':
    app.run(debug=True)

