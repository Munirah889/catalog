from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///dummyrestaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Monirah", email="mun889@hotmail.com",
             picture='https://www.kwsme.com/wp-content/uploads/2016/06/login-user-icon.png')
session.add(User1)
session.commit()


# Menu for Monirah's resturant
restaurant1 = Restaurant(user_id=1, name="Monirah's Restaurant")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Green Salad", description="Green Salad with lime",
                     price="$3", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Onion Rings", description="Fries with parmesan",
                     price="$3", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Pasta", description="Pasta with pink sauce",
                     price="$5", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Cake", description="Cake with ice cream",
                     price="$4", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

# Menu for Herfy
restaurant2 = Restaurant(user_id=1, name="Herfy")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Chicken Burger", description="With cheese and vegetables",
                     price="$9", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Pasta",
                     description=" A famous Pasta wwith white sauce", price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Tuna Sandwich", description="with avocado, tomatoes and cheese sauce ",
                     price="10", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()


# Menu for Nourah's resturant
restaurant1 = Restaurant(user_id=1, name="Nourah's Restaurant")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Pasta", description="with pink souce",
                     price="$9", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Sandwich", description="with vegetables, onions and soy souce",
                     price="$6.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Tuna Sandwich", description="with vegetables, onions and soy souce",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

print "added dummy menu items!"