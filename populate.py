from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///itemcatalog.db')
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
User1 = User(name="John Smith", email="email@example.com",
             picture='https://randomuser.me/api/portraits/lego/5.jpg')
session.add(User1)
session.commit()

# Populate Categories

category1 = Category(user_id=1, name="Apparel, Shoes & Accessories")
session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Bags & Wallets",
             description="moved. waters Deep ", category=category1)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Clothing",
             description="yielding image won't ", category=category1)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Eyewear & Optics",
             description="Thing under. ", category=category1)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Footwear",
             description="isn't whose living. ", category=category1)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Watches & Accessories",
             description="first signs. Light ", category=category1)
session.add(item5)
session.commit()


category2 = Category(user_id=1, name="Beauty")
session.add(category2)
session.commit()


item1 = Item(user_id=1, name="Beauty Gifts Sets",
             description="Fifth all meat give ", category=category2)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Beauty Tools & Accessories",
             description="given you she'd our ", category=category2)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Hair Care Center",
             description="divide isn't ", category=category2)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Hair Styling Electronics",
             description="winged be is over. ", category=category2)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Hair Tools & Accessories",
             description="made two gathered ", category=category2)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Makeup",
             description="one. It seas beast ", category=category2)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Mirrors",
             description="Shall blessed. Said ", category=category2)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Wigs",
             description="were. face. they're. ", category=category2)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Skin Care Center",
             description="behold. Green can't. ", category=category2)
session.add(item9)
session.commit()


category3 = Category(user_id=1, name="Cameras")
session.add(category3)
session.commit()


item1 = Item(user_id=1, name="Analogue Camera",
             description="life female herb ", category=category3)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Batteries",
             description="fifth don't she'd ", category=category3)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Cables",
             description="he hath. Is upon dry ", category=category3)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Camcorders",
             description="Lights creepeth own ", category=category3)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Camera Bags",
             description="meat there have ", category=category3)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Camera & Camcorder Accessories",
             description="fruitful i without ", category=category3)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Chargers",
             description="light brought spirit ", category=category3)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Digital Cameras",
             description="all unto. Hath years ", category=category3)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Digital Photo Frames",
             description="give. male from ", category=category3)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Electronic Flashes",
              description="seasons beginning ", category=category3)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Interchangeable Lenses",
              description="fill it seas tree. ", category=category3)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="Memory Cards",
              description="our to place had may ", category=category3)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Screen Protectors",
              description="after signs deep ", category=category3)
session.add(item13)
session.commit()


item14 = Item(user_id=1, name="Skins & Decals",
              description="Female them female ", category=category3)
session.add(item14)
session.commit()


item15 = Item(user_id=1, name="Still Films",
              description="upon. Grass air form ", category=category3)
session.add(item15)
session.commit()


category4 = Category(user_id=1, name="Electronics")
session.add(category4)
session.commit()


item1 = Item(user_id=1, name="Audio & Accessories",
             description="day seed. Called ", category=category4)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Batteries",
             description="rule midst. Him ", category=category4)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Binoculars & Telescopes",
             description="Evening male sea. ", category=category4)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Cables",
             description="Spirit sixth god ", category=category4)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="CD Recording Media",
             description="After isn't open. ", category=category4)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Chargers",
             description="them upon after ", category=category4)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Clock Radios",
             description="brought likeness and ", category=category4)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="E-Book Readers",
             description="Sixth seasons our ", category=category4)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Home & Office Electronics",
             description="Every. him morning ", category=category4)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Home Theater Systems",
              description="called he meat may ", category=category4)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Home Video Accessories",
              description="Brought you're ", category=category4)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="MP3, MP4 Player & Accessories",
              description="created all air. ", category=category4)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Power Banks",
              description="darkness Had. herb i ", category=category4)
session.add(item13)
session.commit()


item14 = Item(user_id=1, name="Projectors & Accessories",
              description="creepeth meat their ", category=category4)
session.add(item14)
session.commit()


item15 = Item(user_id=1, name="Recording & Studio Equipment",
              description="fourth face brought. ", category=category4)
session.add(item15)
session.commit()


item16 = Item(user_id=1, name="Security & Surveillance Systems",
              description="heaven. Divided ", category=category4)
session.add(item16)
session.commit()


item17 = Item(user_id=1, name="Smart Watches",
              description="moving. sea doesn't ", category=category4)
session.add(item17)
session.commit()


item18 = Item(user_id=1, name="Stereo Systems & Equalizers",
              description="dry. You're. two ", category=category4)
session.add(item18)
session.commit()


item19 = Item(user_id=1, name="TVs, Satellites & Accessories",
              description="can't every fourth ", category=category4)
session.add(item19)
session.commit()


item20 = Item(user_id=1, name="VCD, VCP & VCR Players",
              description="Place. for. Creeping ", category=category4)
session.add(item20)
session.commit()


item21 = Item(user_id=1, name="Video, Home Theater & Accessories",
              description="darkness likeness ", category=category4)
session.add(item21)
session.commit()


item22 = Item(user_id=1, name="Webcams",
              description="Were brought bearing ", category=category4)
session.add(item22)
session.commit()


category5 = Category(user_id=1, name="Gaming")
session.add(category5)
session.commit()


item1 = Item(user_id=1, name="Game Consoles",
             description="Seas after image ", category=category5)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Games Gadgets & Accessories",
             description="lesser fourth ", category=category5)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Screen Protectors",
             description="you're very fish. ", category=category5)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Skins & Decals",
             description="rule fruitful. Let ", category=category5)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Video Games",
             description="two above. Fourth he ", category=category5)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="VR Gadgets",
             description="forth our dry earth. ", category=category5)
session.add(item6)
session.commit()


category6 = Category(user_id=1, name="Health & Personal Care")
session.add(category6)
session.commit()


item1 = Item(user_id=1, name="Bath & Body Center",
             description="created all air. ", category=category6)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Body Massagers",
             description="Brought you're ", category=category6)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Dental Care Center",
             description="shall above life ", category=category6)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Dietary Supplements",
             description="lesser two lights ", category=category6)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Digital Fever Thermometers",
             description="behold fifth. Waters ", category=category6)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Electric Shavers & Removal",
             description="blessed. Let ", category=category6)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Electrical Personal Care",
             description="firmament also ", category=category6)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Men's Grooming",
             description="Brought whales after ", category=category6)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Personal Care Center",
             description="creepeth meat their ", category=category6)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Personal Hygiene",
              description="fly image tree may ", category=category6)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Personal Scales",
              description="behold god fill ", category=category6)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="Small Medical Equipment",
              description="seed given dry void ", category=category6)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Sports Nutrition",
              description="rule. His. Herb ", category=category6)
session.add(item13)
session.commit()


item14 = Item(user_id=1, name="Vitamins & Minerals",
              description="fruit beginning set ", category=category6)
session.add(item14)
session.commit()


category7 = Category(user_id=1, name="Jewelry & Accessories")
session.add(category7)
session.commit()


item1 = Item(user_id=1, name="Bracelets",
             description="had were said ", category=category7)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Body Jewelry",
             description="herb. Kind from saw. ", category=category7)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Earrings",
             description="living have land ", category=category7)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Fine Jewellery",
             description="void i above god ", category=category7)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Jewelry Accessories",
             description="were. Every place ", category=category7)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Jewelry Sets",
             description="subdue that day ", category=category7)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Loose Gemstones & Diamonds",
             description="waters second. That ", category=category7)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Men's Jewelry",
             description="darkness fifth ", category=category7)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Necklaces",
             description="Likeness fifth face ", category=category7)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Pendants & Charms",
              description="earth kind herb ", category=category7)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Rings",
              description="kind green saying ", category=category7)
session.add(item11)
session.commit()


category8 = Category(user_id=1, name="Mobile Phones, Tablets & Accessories")
session.add(category8)
session.commit()


item1 = Item(user_id=1, name="Accessories",
             description="very. one waters ", category=category8)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Mobile Phones",
             description="Brought whales after ", category=category8)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Screen Protectors",
             description="said replenish she'd ", category=category8)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Skins & Decals",
             description="without firmament ", category=category8)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Smart Watches",
             description="Were brought bearing ", category=category8)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Tablets",
             description="replenish open ", category=category8)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="VR Gadgets",
             description="third fruit. Our it. ", category=category8)
session.add(item7)
session.commit()


category9 = Category(user_id=1, name="Perfumes & Fragrances")
session.add(category9)
session.commit()


item1 = Item(user_id=1, name="Perfumes & Fragrances",
             description="fish. The fruitful ", category=category9)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Fragrance Gift Sets",
             description="light multiply ", category=category9)
session.add(item2)
session.commit()


category10 = Category(user_id=1, name="Tools & Home Improvements")
session.add(category10)
session.commit()


item1 = Item(user_id=1, name="Drills",
             description="you're fruit tree ", category=category10)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Electrical & Electronic Accessories",
             description="subdue morning. ", category=category10)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Hand Tools",
             description="together divide also ", category=category10)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Measuring & Layout Tools",
             description="gathered. Subdue it ", category=category10)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Nails, Screws & Fixings",
             description="don't them. Moveth. ", category=category10)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Paint & Supplies",
             description="without firmament ", category=category10)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Power & Hand Tools Accessories",
             description="bring their fowl ", category=category10)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Power Tools",
             description="their his a which ", category=category10)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Safety & Work Wear Products",
             description="multiply after ", category=category10)
session.add(item9)
session.commit()


category11 = Category(user_id=1, name="Wearable Technology Devices")
session.add(category11)
session.commit()


item1 = Item(user_id=1, name="Fitness Technology",
             description="darkness likeness ", category=category11)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Smart Watches",
             description="don't them. Moveth. ", category=category11)
session.add(item2)
session.commit()


category12 = Category(user_id=1, name="Art, Crafts & Collectables")
session.add(category12)
session.commit()


item1 = Item(user_id=1, name="Antiques",
             description="shall. A fowl fly. ", category=category12)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Drawings & Paintings",
             description="which signs cattle ", category=category12)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Handcrafts, Sculpture & Carvings",
             description="Tree without. I ", category=category12)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Islamic",
             description="his under were ", category=category12)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Maps, Atlases & Globes",
             description="give sea moving in. ", category=category12)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Prints & Posters",
             description="open she'd. beast ", category=category12)
session.add(item6)
session.commit()


category13 = Category(user_id=1, name="Bed & Bath")
session.add(category13)
session.commit()


item1 = Item(user_id=1, name="Bathroom Equipment",
             description="likeness set. Years ", category=category13)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Bedding",
             description="likeness form living ", category=category13)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Blankets & Throws",
             description="man can't creature. ", category=category13)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Curtains",
             description="Brought you're ", category=category13)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Mattresses",
             description="yielding very second ", category=category13)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Pillows",
             description="replenish open ", category=category13)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Showers & Showerheads",
             description="seed given dry void ", category=category13)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Storage & Organization",
             description="be him multiply. ", category=category13)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Towels",
             description="saw. Hath called ", category=category13)
session.add(item9)
session.commit()


category14 = Category(user_id=1, name="Coins, Stamps & Paper money")
session.add(category14)
session.commit()


item1 = Item(user_id=1, name="Coins",
             description="the sea called void ", category=category14)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Coins, Paper Money & Stamps Accessories",
             description="earth. Us place seed ", category=category14)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Paper Money",
             description="fourth face brought. ", category=category14)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Stamps",
             description="second lesser called ", category=category14)
session.add(item4)
session.commit()


category15 = Category(user_id=1, name="Eyewear & Optics")
session.add(category15)
session.commit()


item1 = Item(user_id=1, name="Contact Lenses",
             description="brought likeness and ", category=category15)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Eyewear",
             description="which signs cattle ", category=category15)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Eyewear Accessories",
             description="life green own. ", category=category15)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Glasses Frames",
             description="doesn't he morning ", category=category15)
session.add(item4)
session.commit()


category16 = Category(user_id=1, name="Garden & Outdoor")
session.add(category16)
session.commit()


item1 = Item(user_id=1, name="Barbecue Tools & Grill Accessories",
             description="You're good living ", category=category16)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Flowers",
             description="give morning Stars ", category=category16)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Garden Decoration",
             description="earth. Us place seed ", category=category16)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Garden Furniture",
             description="behold. Won't ", category=category16)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Gardening & Watering Supplies",
             description="stars. Fourth heaven ", category=category16)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Grills & Smokers",
             description="there seed also ", category=category16)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Pest Control",
             description="living have land ", category=category16)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Smoking Accessories",
             description="greater. Them the ", category=category16)
session.add(item8)
session.commit()


category17 = Category(user_id=1, name="Home Appliances")
session.add(category17)
session.commit()


item1 = Item(user_id=1, name="Heating, Cooling & Air Quality Center",
             description="morning fourth ", category=category17)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Irons, Steamers & Sewing",
             description="heaven wherein. ", category=category17)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Large Appliances Center",
             description="Sixth seasons our ", category=category17)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Parts & Accessories",
             description="dry fish replenish ", category=category17)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Small Appliances Center",
             description="Our creature wherein ", category=category17)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Televisions",
             description="second blessed ", category=category17)
session.add(item6)
session.commit()


category18 = Category(user_id=1, name="Kitchen Appliances")
session.add(category18)
session.commit()


item1 = Item(user_id=1, name="Appliances Parts & Accessories",
             description="void give darkness. ", category=category18)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Blenders & Mixers",
             description="tree. One subdue had ", category=category18)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Coffee & Espresso Makers",
             description="creeping. whales ", category=category18)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Dishwashers",
             description="be them meat waters ", category=category18)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Electric Meat Grinders",
             description="all seas fish. Upon. ", category=category18)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Electric Slicers",
             description="let lesser fifth ", category=category18)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Food Preparation",
             description="whales moving heaven ", category=category18)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Food Processors",
             description="give he. Moveth ", category=category18)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Fryers",
             description="one. All he saying ", category=category18)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Ice Cream Makers",
              description="Good. Land. Own ", category=category18)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Juicers & Presses",
              description="you're fowl appear ", category=category18)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="Kettles",
              description="replenish she'd ", category=category18)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Kitchen Scales",
              description="earth. And. Made ", category=category18)
session.add(item13)
session.commit()


item14 = Item(user_id=1, name="Microwaves",
              description="Second. Cattle ", category=category18)
session.add(item14)
session.commit()


item15 = Item(user_id=1, name="Ovens, Ranges & Stoves",
              description="dry. You're. two ", category=category18)
session.add(item15)
session.commit()


item16 = Item(user_id=1, name="Range Hoods",
              description="brought whales. his. ", category=category18)
session.add(item16)
session.commit()


item17 = Item(user_id=1, name="Refrigerators & Freezers",
              description="Lights creepeth own ", category=category18)
session.add(item17)
session.commit()


item18 = Item(user_id=1, name="Rice Cooker",
              description="Our creature wherein ", category=category18)
session.add(item18)
session.commit()


item19 = Item(user_id=1, name="Sandwich & Waffle Makers",
              description="together fruit Fly ", category=category18)
session.add(item19)
session.commit()


item20 = Item(user_id=1, name="Slow Cookers",
              description="great. Thing moved ", category=category18)
session.add(item20)
session.commit()


item21 = Item(user_id=1, name="Specialty Kitchen Appliances",
              description="Divided upon give ", category=category18)
session.add(item21)
session.commit()


item22 = Item(user_id=1, name="Steamers",
              description="Beginning was give ", category=category18)
session.add(item22)
session.commit()


item23 = Item(user_id=1, name="Toasters",
              description="fourth years i a. ", category=category18)
session.add(item23)
session.commit()


item24 = Item(user_id=1, name="Water Coolers & Dispensers",
              description="made two gathered ", category=category18)
session.add(item24)
session.commit()


category19 = Category(user_id=1, name="Music & Movies")
session.add(category19)
session.commit()


item1 = Item(user_id=1, name="Guitars",
             description="lesser two lights ", category=category19)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Movies, Plays & Series",
             description="you're fruit tree ", category=category19)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Music CDs",
             description="winged winged two ", category=category19)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Musical Instruments",
             description="waters night. From ", category=category19)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Musical Instruments Parts & Accessories",
             description="fourth the the don't ", category=category19)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Music Keyboards",
             description="creature fish face ", category=category19)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Tuners",
             description="Two isn't you're ", category=category19)
session.add(item7)
session.commit()


category20 = Category(user_id=1, name="Pet Food & Supplies")
session.add(category20)
session.commit()


item1 = Item(user_id=1, name="Pet & Animal Food",
             description="Thing under. ", category=category20)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Pet & Animal Supplies",
             description="of upon replenish ", category=category20)
session.add(item2)
session.commit()


category21 = Category(user_id=1, name="Toys")
session.add(category21)
session.commit()


item1 = Item(user_id=1, name="Bikes, Scooters & Ride-Ons",
             description="Itself open Make ", category=category21)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Costumes",
             description="tree years. Tree ", category=category21)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Toys",
             description="fruitful. Bearing ", category=category21)
session.add(item3)
session.commit()


category22 = Category(user_id=1, name="Baby")
session.add(category22)
session.commit()


item1 = Item(user_id=1, name="Baby Accessories",
             description="Creeping fish don't ", category=category22)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Baby Bags",
             description="heaven fly firmament ", category=category22)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Baby Bath & Skincare",
             description="Under the a ", category=category22)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Baby Clothing & Shoes",
             description="heaven. His sea ", category=category22)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Baby Gear",
             description="abundantly fruit ", category=category22)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Baby Gift Sets",
             description="heaven. Beast ", category=category22)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Baby Safety & Health",
             description="brought be bring ", category=category22)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Baby Toys & Accessories",
             description="let also female ", category=category22)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Diapers",
             description="moved above won't ", category=category22)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Feeding",
              description="evening. Creeping ", category=category22)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Nursery Furniture",
              description="yielding very second ", category=category22)
session.add(item11)
session.commit()


category23 = Category(user_id=1, name="Books")
session.add(category23)
session.commit()


item1 = Item(user_id=1, name="Business & Trade Books",
             description="kind green saying ", category=category23)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Children's Books",
             description="stars whales. Lights ", category=category23)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Comics & Graphic Novels",
             description="heaven. His sea ", category=category23)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Education, Learning & Self Help Books",
             description="female form created ", category=category23)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Lifestyle Books",
             description="whose beast brought ", category=category23)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Literature & Fiction",
             description="Which. Without be ", category=category23)
session.add(item6)
session.commit()


category24 = Category(user_id=1, name="Computers, IT & Networking")
session.add(category24)
session.commit()


item1 = Item(user_id=1, name="Computer & Laptop Accessories",
             description="open she'd. beast ", category=category24)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Computer Parts & Components",
             description="likeness darkness ", category=category24)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Computers & Servers",
             description="replenish beginning. ", category=category24)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Networking & Accessories",
             description="saying. Seasons ", category=category24)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Printers, Scanners, Hardware & Accessories",
             description="seas created had ", category=category24)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Software",
             description="brought years whales ", category=category24)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Laptops & Netbooks",
             description="behold god fill ", category=category24)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="VR Gadgets",
             description="good stars deep it ", category=category24)
session.add(item8)
session.commit()


category25 = Category(user_id=1, name="Furniture")
session.add(category25)
session.commit()


item1 = Item(user_id=1, name="Bedroom Sets",
             description="multiply herb. Land ", category=category25)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Beds & Bed Frames",
             description="his under were ", category=category25)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Chairs & Benches",
             description="gathered. Fish upon ", category=category25)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Garden Furniture",
             description="Shall they're set ", category=category25)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Kitchen & Dining Rooms Sets",
             description="void give darkness. ", category=category25)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Living Room Sets",
             description="Bring Seasons cattle ", category=category25)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Office Furniture",
             description="replenish made face ", category=category25)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Sofas, Bean Bags & Ottomans",
             description="moved that made may ", category=category25)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Storage & Organization",
             description="called he meat may ", category=category25)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Tables",
              description="morning creepeth ", category=category25)
session.add(item10)
session.commit()


category26 = Category(user_id=1, name="Grocery, Food & Beverages")
session.add(category26)
session.commit()


item1 = Item(user_id=1, name="Air Fresheners Center",
             description="seas lesser morning ", category=category26)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Baby Bath & Skin Care Center",
             description="fourth gathering to ", category=category26)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Baby Food Center",
             description="have herb divide ", category=category26)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Bakery Center",
             description="evening i image ", category=category26)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Beverage Center",
             description="created fill his ", category=category26)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Breakfast",
             description="their. Third shall ", category=category26)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Cereals & Grains Center",
             description="itself Whales beast ", category=category26)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Cleaning Products Center",
             description="darkness Had. herb i ", category=category26)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Confectionery Center",
             description="Good. Land. Own ", category=category26)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Dairy Product Center",
              description="green void. He. ", category=category26)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Dry Food",
              description="replenish sixth ", category=category26)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="Fruits & Vegetables Center",
              description="lesser give tree. ", category=category26)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Ghee Center",
              description="make have him Air ", category=category26)
session.add(item13)
session.commit()


item14 = Item(user_id=1, name="Hair Care Center",
              description="called. Male form ", category=category26)
session.add(item14)
session.commit()


item15 = Item(user_id=1, name="Makeup Center",
              description="winged itself beast ", category=category26)
session.add(item15)
session.commit()


item16 = Item(user_id=1, name="Meats & Chicken Center",
              description="whales evening ", category=category26)
session.add(item16)
session.commit()


item17 = Item(user_id=1, name="Personal Care",
              description="moving lesser lesser ", category=category26)
session.add(item17)
session.commit()


item18 = Item(user_id=1, name="Pet Food Center",
              description="our were. Darkness ", category=category26)
session.add(item18)
session.commit()


item19 = Item(user_id=1, name="Plastic & Paper Products Center",
              description="yielding years ", category=category26)
session.add(item19)
session.commit()


item20 = Item(user_id=1, name="Seafood Center",
              description="gathered yielding. ", category=category26)
session.add(item20)
session.commit()


item21 = Item(user_id=1, name="Seasoning, Spices & Preservatives",
              description="fruit after waters ", category=category26)
session.add(item21)
session.commit()


item22 = Item(user_id=1, name="Skin Care Center",
              description="together is winged ", category=category26)
session.add(item22)
session.commit()


category27 = Category(user_id=1, name="Home Decor & Furniture")
session.add(category27)
session.commit()


item1 = Item(user_id=1, name="Home Decor Center",
             description="Fish place behold ", category=category27)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Lamps & Lighting",
             description="divide living set ", category=category27)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Small Furniture",
             description="for evening from ", category=category27)
session.add(item3)
session.commit()


category28 = Category(user_id=1, name="Kitchen & Home Supplies")
session.add(category28)
session.commit()


item1 = Item(user_id=1, name="Bakeware & Accessories",
             description="multiply after ", category=category28)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Cleaning Products Center",
             description="great sixth hath ", category=category28)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Cooking Utensils",
             description="divided lesser every ", category=category28)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Cookware & Bakeware",
             description="gathered. forth ", category=category28)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Cutlery & Flatware Set",
             description="called. Male form ", category=category28)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Dinnerware & Serveware",
             description="Bearing to. winged ", category=category28)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Drinkware",
             description="creature unto divide ", category=category28)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Home Supplies",
             description="firmament created. ", category=category28)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Kitchen Accessories",
             description="abundantly you're. ", category=category28)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Kitchen Measuring Tools",
              description="fowl saying. beast. ", category=category28)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Kitchen Storage",
              description="years brought over ", category=category28)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="Plastic & Paper Products Center",
              description="dominion under may ", category=category28)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Table Linens",
              description="beginning. void ", category=category28)
session.add(item13)
session.commit()


category29 = Category(user_id=1, name="Office Products & Supplies")
session.add(category29)
session.commit()


item1 = Item(user_id=1, name="Fax Machines",
             description="Second. Cattle ", category=category29)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Multifunctional Printers",
             description="beast. Kind created ", category=category29)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Office Equipment",
             description="Fowl divided saying ", category=category29)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Office Furniture",
             description="very itself. Herb ", category=category29)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Office Supplies",
             description="living have land ", category=category29)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Printers",
             description="day heaven fifth ", category=category29)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Printers, Scanners, Hardware & Accessories",
             description="days behold day ", category=category29)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="Stationery",
             description="dominion beginning ", category=category29)
session.add(item8)
session.commit()


category30 = Category(user_id=1, name="Sports & Fitness")
session.add(category30)
session.commit()


item1 = Item(user_id=1, name="Athletic Shoes",
             description="beginning said. ", category=category30)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Balls",
             description="give sea moving in. ", category=category30)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Bikes & Bicycles",
             description="day seed. Called ", category=category30)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Camping Center",
             description="living Life from ", category=category30)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Exercise Bikes",
             description="which signs cattle ", category=category30)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Fitness Technology Center",
             description="moved above won't ", category=category30)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="Flashlights",
             description="forth Divide whose ", category=category30)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="GPS Receiver",
             description="place spirit you ", category=category30)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Motorcycling",
             description="seas two eart", category=category30)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Outdoor Play",
              description="brought likeness and ", category=category30)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Protective Gear",
              description="you beginning forth. ", category=category30)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="Rackets",
              description="unto you Fly image ", category=category30)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Scooters & Ride-Ons",
              description="abundantly. Great ", category=category30)
session.add(item13)
session.commit()


item14 = Item(user_id=1, name="Specialty Bags & Carry Cases",
              description="saying appear void ", category=category30)
session.add(item14)
session.commit()


item15 = Item(user_id=1, name="Sport Gloves",
              description="cattle life evening ", category=category30)
session.add(item15)
session.commit()


item16 = Item(user_id=1, name="Sporting Goods",
              description="second blessed ", category=category30)
session.add(item16)
session.commit()


item17 = Item(user_id=1, name="Sports Equipments",
              description="he creepeth whales ", category=category30)
session.add(item17)
session.commit()


item18 = Item(user_id=1, name="Sport Watches",
              description="she'd very you fruit ", category=category30)
session.add(item18)
session.commit()


item19 = Item(user_id=1, name="Treadmills",
              description="she'd. Over. Heaven. ", category=category30)
session.add(item19)
session.commit()


item20 = Item(user_id=1, name="Weights & Dumbbells",
              description="said. blessed under. ", category=category30)
session.add(item20)
session.commit()


category31 = Category(user_id=1, name="Vehicle Parts & Accessories")
session.add(category31)
session.commit()


item1 = Item(user_id=1, name="Accessories",
             description="fish. The fruitful ", category=category31)
session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Car Audio",
             description="fifth. I one years ", category=category31)
session.add(item2)
session.commit()


item3 = Item(user_id=1, name="Car Parts",
             description="Night fourth ", category=category31)
session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Car Speakers, Subwoofers & Amplifiers",
             description="gathered. Subdue it ", category=category31)
session.add(item4)
session.commit()


item5 = Item(user_id=1, name="Car Video",
             description="days creepeth. Saw. ", category=category31)
session.add(item5)
session.commit()


item6 = Item(user_id=1, name="Cleaning Products Center",
             description="fruit after waters ", category=category31)
session.add(item6)
session.commit()


item7 = Item(user_id=1, name="GPS Navigators",
             description="Land herb greater ", category=category31)
session.add(item7)
session.commit()


item8 = Item(user_id=1, name="GPS Receiver",
             description="let also female ", category=category31)
session.add(item8)
session.commit()


item9 = Item(user_id=1, name="Motorcycle Parts",
             description="creeping. Set rule ", category=category31)
session.add(item9)
session.commit()


item10 = Item(user_id=1, name="Tires & Wheels",
              description="after fly heaven. ", category=category31)
session.add(item10)
session.commit()


item11 = Item(user_id=1, name="Vacuum Cleaners",
              description="sea. give form. ", category=category31)
session.add(item11)
session.commit()


item12 = Item(user_id=1, name="Vehicle Fluids",
              description="earth dry shall ", category=category31)
session.add(item12)
session.commit()


item13 = Item(user_id=1, name="Vehicles Lights & Bul",
              description="good i god rule form ", category=category31)
session.add(item13)
session.commit()


print ("database populated!")
