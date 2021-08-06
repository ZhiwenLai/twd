import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twd.settings')

import django
django.setup()
from rango.models import *

# For an explanation of what is going on here, please refer to the TwD book.

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 114,},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views': 53},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views': 20} ]
    
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 32},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 12},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 1258} ]
    
    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 54},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views': 64} ]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    dog = {

        'Corgi': {
            'breedname': 'Corgi', 'description': "Corgi is a small type of herding dog that originated in Wales. There are two breeds of Welsh Corgis, the Cardigan and the Pembroke, each named for the county in Wales where it originated. The dogs share several similar traits, such as their coats, which are water-resistant and shed on average twice a year. The body of the Cardigan is slightly longer than that of the Pembroke; both breeds have short legs, placing their bodies close to the ground. But they are not as square in outline as a typical Terrier, or have an elongated body as great as that of a Dachshund. There are only minor differences in the shape of the head, both appear fox-like. The head of a Cardigan Welsh Corgi is typically larger than that of an equivalent Pembroke, and has a larger nose. It can take a few days following birth for the true colour of a Corgi's coat to appear, and this is particularly evident in those with tricolour or black and tan markings.Corgis in the modern era often compete in dog agility trials, obedience, showmanship, flyball, tracking, and herding events. Herding instincts and trainability can be measured at non-competitive herding tests. Cardigan and Pembroke Corgis exhibiting basic herding instincts can be trained to compete in herding trials – known colloquially as a 'mad run'. Welsh Corgis were once used to guard children."
, 'image': 'dog_images\corgi3.jpeg',
            'status': 3,'views': 9,
        },
        'Schnauzer': {
            'breedname': 'Schnauzer', 'description': "Schnauzer is a dog breed type that originated in Germany from the 14th to 16th centuries. The term comes from the German word for 'snout' and means colloquially 'moustache', or 'whiskered snout', because of the dog's distinctively bearded snout. There are three breeds: the Standard, the Giant, and the Miniature. The breed is of above average intelligence and can be independent minded, so early training and diverse daily exercise are recommended. They are protective and energetic, and will alert members of the household to any potential danger, although its watchful nature can lead to persistent barking. To avoid annoying the neighbors, dog owners should make every effort to curb excessive barking through training. Schnauzers have distinctive beards and long, feathery eyebrows. They are generally either a salt and pepper colour, black, or white, but they can be brown also. It was traditional to have the tails docked and the ears cropped to give an alert appearance but in many countries it is now illegal. For working dogs that are ratters, these procedures don't give the rat anything to grab on to when being attacked and therefore cannot fight back. Cropping and docking are now illegal in the European Union, Australia, and New Zealand, and are becoming less common elsewhere. The Schnauzer's beard and leg hair should be brushed often to prevent mats from forming."
, 'image': 'dog_images\Schnauzer3.jpg',
            'status': 1,'views': 11,
        },
        'Dachshund': {
            'breedname': 'Dachshund', 'description': "The dachshund, also known as the wiener dog, badger dog, sausage dog, is a short-legged, long-bodied, hound-type dog breed. They may be smooth, wire, or long-haired. A typical dachshund is long-bodied and muscular with short stubby legs. Its front paws are disproportionately large, being paddle-shaped and particularly suitable for digging. Its skin is loose enough not to tear while tunneling in tight burrows to chase prey. The dachshund has a deep chest which provides plenty of space for heart development and lung capacity. Its snout is long. The dominant color in the breed is red, followed by black and tan. Tan pointed dogs have tan (or cream) markings over the eyes, ears, paws, and tail. Dachshunds come in three sizes: standard, miniature, and kaninchen (German for 'rabbit'). A full-grown standard dachshund averages 7.5 kg (16 lb) to 14.5 kg (32 lb), while the miniature variety normally weighs less than 5.5 kg (12 lb). The kaninchen weighs 3.5 kg (8 lb) to 5 kg (11 lb). Dachshunds are playful, but as hunting dogs can be quite stubborn, and are known for their propensity for chasing small animals, birds, and tennis balls with great determination and ferocity. Dachshunds are often stubborn, making them a challenge to train."
, 'image': 'dog_images\Dachshund3.jpg',
            'status': 1,'views': 100,
        },
        'Pug': {
            'breedname': 'Pug', 'description': "The pug is a breed of dog with physically distinctive features of a wrinkly, short-muzzled face, and curled tail. The breed has a fine, glossy coat that comes in a variety of colors, most often light brown (fawn) or black, and a compact, square body with well-developed muscles. Pugs are known for being sociable and gentle companion dogs. The American Kennel Club describes the breed's personality as 'even-tempered and charming'. Pugs remain popular into the twenty-first century, with some famous celebrity owners. Modern breed preferences are for a square cobby body, a compact form, a deep chest, and well-developed muscle. Their smooth and glossy coats can be fawn, apricot fawn, silver fawn, or black. The markings are clearly defined and there is a trace of a black line extending from the occiput to the tail. The tail normally curls tightly over the hip. Pugs have two distinct shapes for their ears, 'rose' and 'button'. 'Rose' ears are smaller than the standard style of 'button' ears, and are folded with the front edge against the side of the head. Breeding preference goes to 'button' style ears. Pugs' legs are strong, straight, of moderate length and are set well under. Their shoulders are moderately laid back. Their ankles are strong, their feet are small, their toes are well split-up, and their nails are black. The lower teeth normally protrude further than their upper, resulting in an under-bite."
, 'image': 'dog_images\Pug3.jpg',
            'status': 1,'views': 999,
        },
        'Border Collie': {
            'breedname': 'Border Collie', 'description': "The Border Collie is a working and herding dog breed. They come from the Anglo-Scottish border region and are used to herd livestock, specifically sheep. The Border Collie is considered a highly intelligent, extremely energetic, acrobatic and athletic dog. They frequently compete with great success in sheepdog trials and a range of dog sports like dog obedience, disc dog, herding and dog agility. They are one of the most intelligent dogs of all domestic dog breeds. Border Collies continue to be employed in their traditional work of herding livestock throughout the world and are kept as pets. In general, Border Collies are medium-sized dogs with a moderate amount of coat, which is more often thick and prone to shedding. They have a double coat that varies from smooth to rough and is occasionally curled. While black and white is the most commonly seen color pattern of the Border Collie, the breed appears in just about any color and pattern known to occur in dogs. Some of these include black tricolor (black/tan/white), liver and white, and red tricolor (red/tan/white) which have also been seen regularly, and other colours such as blue, lilac, red merle, blue merle, brindle, and Australian red (also known as ee red, blonde, recessive red, or gold) which is seen less frequently. Some border collies may also have single-color coats."
, 'image': 'dog_images\Border_collie3.jpeg',
            'status': 3,'views': 300,
        },
         'Husky': {
            'breedname': 'Husky', 'description': "A husky is a sled dog used in the polar regions. One can differentiate huskies from other dog types by their fast pulling-style. When used as a sled dog, they represent an ever-changing crossbreed of the fastest dogs (the Alaskan Malamute, by contrast, pulled heavier loads at a slower speed). Huskies are energetic and athletic. They usually have a thick double coat that can be gray, black, copper red, or white. The double coat generally protects huskies against harsh winters and, contrary to what most believe, they can survive in hotter climates. During the hotter climates, huskies tend to shed their undercoat regularly to cool their bodies. In addition to shedding, huskies control their eating habits based on the season; in cooler climates, they tend to eat generous amounts, causing their digestion to generate heat, whilst in warmer climates, they eat less. Their eyes are typically pale blue, although they may also be brown, green, blue, yellow, or heterochromic. Huskies are more prone to some degree of uveitis than most other breeds. Hunting instincts can still be found in some of this breed today."
, 'image': 'dog_images\Husky3.jpeg',
            'status': 3,'views': 1,
        },
         'Labrador Retriever': {
            'breedname': 'Labrador Retriever', 'description': "The Labrador Retriever, often abbreviated to Labrador or Lab, is a breed of retriever-gun dog from the United Kingdom that was developed from imported Canadian fishing dogs. The Labrador is one of the most popular dog breeds in a number of countries in the world, particularly in the Western world. A popular disability assistance breed in many countries, Labradors are frequently trained to aid those with blindness or autism, act as a therapy dog, or perform screening and detection work for law enforcement and other official agencies. The breed is best known for their obedience, loyalty, and playful composure. Additionally, they are prized as sporting and hunting dogs. Ancestors include a breed used in Newfoundland as fishing dogs, that would help in bringing in the fishing nets and recapture escaped fish. The AKC describes the Labrador's temperament as a kind, pleasant, outgoing and tractable nature. Labradors' sense of smell allows them to home in on almost any scent and follow the path of its origin. They generally stay on the scent until they find it. Navies, military forces and police forces use them as detection dogs to track down smugglers, thieves, terrorists and black marketers. They are known to have a very soft feel to the mouth as a result of being bred to retrieve game such as waterfowl. They are prone to chewing objects (though they can be trained to abandon this behaviour). Labradors have a reputation as a very even-tempered breed and an excellent family dog."
, 'image': 'dog_images\labrador3.jpg',
            'status': 2,'views': 1,
        },
        'German Shepherd': {
            'breedname': 'German Shepherd', 'description': "The German Shepherd is a breed of medium to large-sized working dog that originated in Germany. According to the FCI, the breed's English language name is German Shepherd Dog. The breed was officially known as the 'Alsatian Wolf Dog' in the UK from after the First World War until 1977 when its name was changed back to German Shepherd. Despite its wolf-like appearance, the German Shepherd is a relatively modern breed of dog, with its origin dating to 1899. As a herding dog, German Shepherds are working dogs developed originally for herding sheep. Since that time, however, because of their strength, intelligence, trainability, and obedience, German Shepherds around the world are often the preferred breed for many types of work, including disability assistance, search-and-rescue, police and military roles and acting. The German Shepherd is the second-most registered breed by the American Kennel Club and seventh-most registered breed by The Kennel Club in the United Kingdom. German Shepherds are medium to large-sized dogs. The breed standard height at the withers is 60–65 cm (24–26 in) for males, and 55–60 cm (22–24 in) for females. They have a domed forehead, a long square-cut muzzle with strong jaws and a black nose. The eyes are medium-sized and brown. The ears are large and stand erect, open at the front and parallel, but they often are pulled back during movement."
, 'image': 'dog_images\German_Shepherd3.jpeg',
            'status': 2,'views': 1,
        },
            

    }

    info_1= {'images': 'sales_images\corgi4.jpeg',  'descriptions': '3 years old and 14kg. Good health. Pedigree.',
     'color': 'yellow and white', 'gender': 'male', 'price': 980, 'contactnumber': 1368555135,}

    info_2= {'images': 'sales_images\Schnauzer4.jpg',  'descriptions': '3 months old and 2kg. Good health. Pedigree. Vaccinated',
             'color': 'black and white', 'gender': 'female', 'price': 750, 'contactnumber': 1763225645,}

    info_3= {'images': 'sales_images\Dachshund4.jpg',  'descriptions': '2 years old and 7kg. Good health.',
             'color': 'tan', 'gender': 'male', 'price': 680, 'contactnumber': 1676512985,}

    info_4= {'images': 'sales_images\pug4.jpg',  'descriptions': '3 years old and 8kg. Good health. Pedigree.',
             'color': 'black', 'gender': 'male', 'price': 800, 'contactnumber': 1496625462,}            

    add_info(images=info_1['images'],descriptions=info_1['descriptions'],color=info_1['color'],gender=info_1['gender'],
                 price=info_1['price'],contactnumber=info_1['contactnumber']),
    add_info( images=info_2['images'], descriptions=info_2['descriptions'],
             color=info_2['color'], gender=info_2['gender'],
             price=info_2['price'], contactnumber=info_2['contactnumber']),
    add_info(images=info_3['images'],descriptions=info_3['descriptions'],color=info_3['color'],gender=info_3['gender'],
                 price=info_3['price'],contactnumber=info_3['contactnumber']),
    add_info( images=info_4['images'], descriptions=info_4['descriptions'],
             color=info_4['color'], gender=info_4['gender'],
             price=info_4['price'], contactnumber=info_4['contactnumber']),


    for dog, dog_data in dog.items():
        add_dog(breedname=dog_data['breedname'], description=dog_data['description'],image=dog_data['image'],status=dog_data['status'],views=dog_data['views'])


    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
def add_dog(breedname, description,image,status,views=0):
    d = Dog.objects.get_or_create(breedname=breedname)[0]
    d.description = description
    d.image= image
    d.status = status
    d.views = views
    d.save()
    return d


def add_info(images, descriptions,color,gender,price,contactnumber):
    e = salesinfo.objects.get_or_create(color=color)[0]
    e.image = images
    e.description= descriptions
    e.color = color
    e.gender =gender
    e.price = price
    e.contactnumber = contactnumber
    e.save()
    return e



# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()