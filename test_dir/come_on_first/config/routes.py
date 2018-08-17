
from app.views.v2 import *
# from app.views.v1 import *
from config import config

# register blueprints
# routes = {
#     # url_prefix: blueprint_instance
#     # "/url": inst
#     "/login": auth,
#     "/register": register,
#     "/article": article,
#     "/comment": comment,
#     "/g_test": g_test
# }
# register blueprints, include template
routes = {
    # url_prefix: blueprint_instance
    # "/url": inst
    "/login": auth,
    "/register": register,
    "/article": article,
    "/comment": comment,
    "/": index,
    "/404": not_found,
    "/publish": publish,
    "/user": user,
    "/show_article": show_articles
}


def register_routes(app):
    """register blueprints from route map"""
    v = config.get('APP_API_VERSION') or ""
    for url, bp in routes.items():
        app.register_blueprint(bp, url_prefix=v+url)


# end
