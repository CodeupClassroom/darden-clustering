import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# Remove any properties that are likely to be something other than a single unit properties (e.g. no duplexes, no land/lot, ...). There are multiple ways to estimate that a property is a single unit, and there is not a single "right" answer.

def get_zillow_data():
    query = '''
    SELECT p1.*
            , p2.transactiondate
            , p2.logerror 
            , ac.airconditioningdesc
            , arch.architecturalstyledesc
            , bldg.buildingclassdesc
            , heat.heatingorsystemdesc
            , land.propertylandusedesc
            , stories.storydesc
            , const.typeconstructiondesc
    FROM zillow.properties_2017 p1
    LEFT JOIN zillow.airconditioningtype ac USING(airconditioningtypeid)
    LEFT JOIN zillow.architecturalstyletype arch USING(architecturalstyletypeid)
    LEFT JOIN zillow.buildingclasstype bldg USING(buildingclasstypeid)
    LEFT JOIN zillow.heatingorsystemtype heat USING(heatingorsystemtypeid)
    LEFT JOIN zillow.propertylandusetype land USING(propertylandusetypeid)
    LEFT JOIN zillow.storytype stories USING(storytypeid)
    LEFT JOIN zillow.typeconstructiontype const USING(typeconstructiontypeid)
    INNER JOIN (
	    SELECT p2.parcelid, p1.logerror, p2.max_transactiondate AS transactiondate 
            FROM zillow.predictions_2017 p1
            INNER JOIN (SELECT parcelid, MAX(transactiondate) AS max_transactiondate 
                    FROM zillow.predictions_2017 
                    GROUP BY parcelid) p2
            ON p1.parcelid = p2.parcelid AND p1.transactiondate = p2.max_transactiondate
        ) p2 USING(parcelid)
    INNER JOIN (
	    SELECT parcelid, logerror, MAX(transactiondate) AS transactiondate FROM zillow.predictions_2017 GROUP BY parcelid, logerror
        ) t2 USING(parcelid, transactiondate)
    WHERE (p1.bedroomcnt > 0 AND p1.bathroomcnt > 0 
            AND calculatedfinishedsquarefeet > 500
            AND latitude IS NOT NULL AND longitude IS NOT NULL)
            AND (unitcnt = 1 OR unitcnt IS NULL)
    ;
    '''
    return pd.read_sql(query, get_connection('zillow'))

def get_iris_data():
    query = '''
    SELECT petal_length, petal_width, sepal_length, sepal_width, species_id, species_name
    FROM measurements m
    JOIN species s USING(species_id)
    '''
    return pd.read_sql(query, get_connection('iris_db'))

def get_mallcustomer_data():
    df = pd.read_sql('SELECT * FROM customers;', get_connection('mall_customers'))
    return df.set_index('customer_id')