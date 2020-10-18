
import requests
from io import BytesIO
from PIL import Image, ImageDraw
import cognitive_face as CF
import argparse


def handleArgs():
	parser = argparse.ArgumentParser(description='Generate face group')
	parser.add_argument('-g', '--group', help='generate group', default=',')
	parser.add_argument('-n', '--name', help='generate name', default=',')
	parser.add_argument('-u', '--user', help='add user data', default=',')
        parser.add_argument('-i', '--image', help='add user face image', default='./face_api_train_cp.jpg')

	args = vars(parser.parse_args())
        return args

KEY = 'dcf0f1dd4ffb45f880b9ae8c16f9e568'
CF.Key.set(KEY)

BASE_URL = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0'  
CF.BaseUrl.set(BASE_URL)



if __name__ == '__main__':
    
    args = handleArgs()
    if args['group'] == ',' or args['name'] == ',' or args['user'] == ',':
        print("argument error!!")
    else:   
        if args['group']:
            PERSON_GROUP_ID = args['group']
            CF.person_group.create(PERSON_GROUP_ID, args['group'])
 
        if args['name']:
            name = args['name']
    
        if args['user']:
            user_data = args['user']
    
        response = CF.person.create(PERSON_GROUP_ID, name, user_data)

        # Get person_id from response
        person_id = response['personId']

        if args['image']:
            CF.person.add_face(args['image'], PERSON_GROUP_ID, person_id, user_data=None, target_face=None)

        print CF.person.lists(PERSON_GROUP_ID)


        CF.person_group.train(PERSON_GROUP_ID)

        response = CF.person_group.get_status(PERSON_GROUP_ID)
        status = response['status']









