from owslib.wfs import WebFeatureService
from owslib.util import Authentication
from pprint import pprint
import geopandas as gpd

wfs = WebFeatureService('https://geoservicos.cprm.gov.br/geoserver/geoquimica/wfs',
                        version='1.1.0', auth=Authentication(verify=False))

pprint([operation.name for operation in wfs.operations])

pprint(list(wfs.contents))

pprint(wfs.get_schema('geoquimica:novo-fcampo'))

response = wfs.getfeature(typename='geoquimica:novo-fcampo', bbox=(-41.26, -12.82, -40.88, -12.52), srsname='urn:x-ogc:def:crs:EPSG:4326')

#with open('/tmp/geoquimica.gml', 'wb') as output:
#    output.write(response.read())

df = gpd.read_file(response)

print(df.head())
