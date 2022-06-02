from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
import base64

token_decoded = base64.b64decode(inputs['token'].encode('ascii'))
ca_decoded = base64.b64decode(inputs['ca'].encode('ascii'))

ctx.instance.runtime_properties['sa_token_decoded'] = token_decoded.decode()
ctx.instance.runtime_properties['ca_certificate_decoded'] = ca_decoded.decode()
