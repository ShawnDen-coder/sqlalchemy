from main import *

# cc_cookie = Cookie(cookie_name='chocolate chip',
#                    cookie_recipe_url="http://some.aweso.me/cookies/recipe.html",
#                    cookie_sku='CC01',
#                    quantity=12,
#                    unit_cost=0.50)
#
# c1 = Cookie(cookie_name='peanut buttter',
#             cookie_recipe_url="http://some.aweso.me/cookies/peanut.html",
#             cookie_sku='PB01',
#             quantity=24,
#             unit_cost=0.25)
#
# c2 = Cookie(cookie_name='oatmeal raisin',
#             cookie_recipe_url="http://some.aweso.me/cookies/raisin.html",
#             cookie_sku='EWW01',
#             quantity=100,
#             unit_cost=1.00
#             )
#
# c3 = Cookie(cookie_name='dark chocolate',
#             cookie_recipe_url="http://some.aweso.me/cookies/recipe_dark.html",
#             cookie_sku='CC02',
#             quantity=1,
#             unit_cost=0.75
#             )
#
# c4 = Cookie(cookie_name='molasses',
#             cookie_recipe_url="http://some.aweso.me/cookies/recipe_molasses.html",
#             cookie_sku='MOL01',
#             quantity=1,
#             unit_cost=0.80
#             )
#
# session.bulk_save_objects([cc_cookie, c1, c2, c3, c4])
# session.commit()


# t = session.query(Cookie)
# for x in t.order_by(desc(Cookie.cookie_id)).all():
#     print(x.cookie_id)
#


cookiemon = User(username='cookiemon',
                 email_address='mon@cookie.com',
                 phone='111-111-1111',
                 password='password')

cakeeater = User(username='cakeeater',
                 email_address='cakeeater@cake.com',
                 phone='222-222-2222',
                 password='password')

pieperson = User(username='pieperson',
                 email_address='pieperson@pie.com',
                 phone='222-222-2222',
                 password='password')





session.add(cookiemon)
# session.commit()
