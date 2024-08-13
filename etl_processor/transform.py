import pandas


class TransformExcelFileData:

    def transform_local_food_production_annual_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        return dataframe.set_index("Data Series").transpose()


    def transform_electricity_generation_monthly_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        return dataframe.rename(columns=lambda x: x.strip()).set_index("Data Series").transpose()
    

    def transform_licensed_local_food_farm_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        return dataframe.rename(columns=lambda x: x.strip()).set_index("Data Series")

    def transform_electricity_generation_and_consumption_monthly_data(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        dataframe = dataframe.rename(columns=lambda x: x.strip()).set_index("Data Series").transpose()
        # to clear the white space in another columns in dataframe after transpose
        dataframe = dataframe.rename(columns=lambda x: x.strip())
        dataframe = dataframe.replace('na', value=0)
        return dataframe.rename(columns={"Data Series": "Year"})

    
    def transform_electricity_generation_by_month(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:

        dataframe = dataframe.rename(columns={"Data Series": "Month"})

        dataframe = dataframe.set_index("Month").transpose()
 

        return dataframe
    #def transform_total_energy_consumption_by_energy_type_and_sector_for_petroleum_products(self):
       # total_final_energy_consumption_by_energy_type_and_sector_for_petroleum_products_dataframe.set_index("Data Series").transpose()

class TransformCSVFileData:

    pass