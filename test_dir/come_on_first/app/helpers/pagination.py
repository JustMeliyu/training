# encoding:utf-8
from flask_sqlalchemy import Pagination
from flask import abort


def paginate(query, page, per_page, error_out=True):
    """
    这个函数是给使用db.session.query查询的数据，而不是用db.Model对象查询的数据，
    因为db.session.query返回的数据是没有paginate函数的 所以这里实现了个
    """
    if page < 1:
        if error_out:
            abort(404)
        else:
            page = 1
    if per_page < 1:
        if error_out:
            abort(404)
        else:
            per_page = 10

    items = query.limit(per_page).offset((page - 1) * per_page).all()
    if not items and page != 1 and error_out:
        abort(404)
    if page == 1 and len(items) < per_page:
        total = len(items)
    else:
        total = query.order_by(None).count()
    return Pagination(query, page, per_page, total, items)
