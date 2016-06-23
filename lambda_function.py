import pprint


def lambda_handler(event, context):
    pprint.pprint(event)
    pprint.pprint(dir(context))
    print('value1 = {}'.format(event['key1']))
    print('value1 = {}'.format(event['key1']))
