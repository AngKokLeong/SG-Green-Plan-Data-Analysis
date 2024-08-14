
from mongoengine import Document, StringField, IntField, DecimalField, GenericReferenceField
import database.database_connection


class ElectricityGenerationAndConsumptionByMonth(Document):
    meta = {"db_alias": database.database_connection.MongoDBTestCluster.connection_alias}

    year: IntField = IntField(required=True, unique=True)
    electricity_generation = DecimalField(min_value=0)
    electricity_consumption = DecimalField(min_value=0)
    industrial_related = DecimalField(min_value=0)
    manufacturing = DecimalField(min_value=0)
    construction = DecimalField(min_value=0)
    utilities = DecimalField(min_value=0)
    other_industrial_related = DecimalField(min_value=0)
    commerce_and_service_related = DecimalField(min_value=0)
    wholesale_and_retail_trade = DecimalField(min_value=0)
    accommodation_and_food_services = DecimalField(min_value=0)
    information_and_communications = DecimalField(min_value=0)
    financial_and_insurance_activities = DecimalField(min_value=0)
    real_estate_activities = DecimalField(min_value=0)
    professional_scientific_and_technical_administration_and_support_activities = DecimalField(min_value=0)
    other_commerce_and_service_related = DecimalField(min_value=0)
    transport_related = DecimalField(min_value=0)
    households = DecimalField(min_value=0)
    others = DecimalField(min_value=0)


class ElectricityGenerationMonthlyData(Document):
    meta = {"db_alias": database.database_connection.MongoDBTestCluster.connection_alias}

    month = StringField(required=True, unique=True)
    electricity_generation = DecimalField(min_value=0)


class LicensedLocalFoodFarm(Document):
    meta = {"db_alias": database.database_connection.MongoDBTestCluster.connection_alias}

    year = StringField( required=True, unique=True)
    number_of_licensed_local_food_farms = IntField(min_value=0)
    sea_based_seafood = IntField(min_value=0)
    land_based_seafood = IntField(min_value=0)
    vegetables = IntField(min_value=0)
    hen_shell_eggs = IntField(min_value=0)
    others = IntField(min_value=0)

 
class LocalFoodProduction(Document):
    meta = {"db_alias": database.database_connection.MongoDBTestCluster.connection_alias}

    year = StringField(required=True, unique=True)
    total_value_of_local_production_million_dollars = IntField(min_value=0)
    seafood_million_dollars = IntField(min_value=0)
    vegetable_million_dollars = IntField(min_value=0)
    hen_shell_eggs_million_dollars = IntField(min_value=0)
    local_production_of_seafood_tonnes = IntField(min_value=0)
    local_production_of_vegetables_tonnes = IntField(min_value=0)
    local_production_of_hen_shell_eggs_million_tonnes = IntField(min_value=0)
    local_production_of_aquarium_fish_million_pieces = IntField(min_value=0)
    local_production_of_aquatic_plants_and_tissue_culture_plantlets_million_plants = IntField(min_value=0)
    local_production_of_orchids_million_stalks = IntField(min_value=0)
    local_production_of_ornamental_plants_million_plants = IntField(min_value=0)

