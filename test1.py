from main import *

test = Cookie()

cc_cookie = Cookie(cookie_name='chocolate chip',
                   cookie_recipe_url="http://some.aweso.me/cookies/recipe.html",
                   cookie_sku='CC01',
                   quantity=12,
                   unit_cost=0.50)

c1 = Cookie(cookie_name='peanut buttter',
            cookie_recipe_url="http://some.aweso.me/cookies/peanut.html",
            cookie_sku='PB01',
            quantity=24,
            unit_cost=0.25)

c2 = Cookie(cookie_name='oatmeal raisin',
            cookie_recipe_url="http://some.aweso.me/cookies/raisin.html",
            cookie_sku='EWW01',
            quantity=100,
            unit_cost=1.00
            )


c3 = Cookie(cookie_name='dark chocolate',
            cookie_recipe_url="http://some.aweso.me/cookies/recipe_dark.html",
            cookie_sku='CC02',
            quantity=1,
            unit_cost=0.75
            )

c4 = Cookie(cookie_name='molasses',
            cookie_recipe_url="http://some.aweso.me/cookies/recipe_molasses.html",
            cookie_sku='MOL01',
            quantity=1,
            unit_cost=0.80
            )


session.bulk_save_objects([cc_cookie,c1,c2,c3,c4])
session.commit()
