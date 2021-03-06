# dummy_data.py
# Loads dummy data from json files to populate the webpage while there is no backend established.

# Use os to navigate path and json to load json files
import os
import json


class DummyData:
    """Generate a set of dummy data to populate the site's webpages."""

    def __init__(self):
        """Load all dummy files on initialization."""

        self.special_components = self.load_data("special_components")
        self.regular_components = self.load_data("regular_components")
        self.work_orders = self.load_data("work_orders")
        self.employees = self.load_data("employees")
        self.sites = self.load_data("sites")
        self.locations = self.load_data("locations")
        self.products = self.load_data("products")
        self.states = self.load_data("states")

        #Ali
        self.products_catalog=self.load_data("products_catalog")
        self.regular_components_catalog=self.load_data("regular_components_catalog")
        self.special_components_catalog=self.load_data("special_components_catalog")
        self.workorderproducts=self.load_data("workorderproducts")
        self.product_components=self.load_data("product_components")
        self.assembly=self.load_data("assembly")
        self.qc=self.load_data("qc")
        self.wo_status=self.load_data("workorder_status_catalog")

    @staticmethod
    def load_data(filename):
        """Load json files containing dummy data."""

        # Create a link to the `data` directory inside the `cim` directory
        data_path = os.path.join("cim", "data")

        # Load the json filename proviced
        with open(f"{data_path}/{filename}.json") as json_file:
            return json.load(json_file)

    # methods to return dummy data
    def get_sc(self):
        return self.special_components
    def get_rc(self):
        return self.regular_components
    def get_emp(self):
        return self.employees
    def get_sites(self):
        return self.sites
    def get_wo(self):
        return self.work_orders
    def get_loc(self):
        return self.locations
    def get_products(self):
        return self.products
    def get_states(self):
        return self.states

    #Ali
    def get_products_catalog(self):
        # print(f'products key: {self.products_catalog.keys()}')
        return self.products_catalog
    def get_rc_catalog(self):
        return self.regular_components_catalog
    def get_sp_catalog(self):
        return self.special_components_catalog
    def get_workorderproducts(self):
        return self.workorderproducts
    def get_product_components(self):
        return self.product_components
    def get_assembly(self):
        return self.assembly
    def get_qc(self):
        return self.qc
    def get_wo_status(self):
        return self.wo_status


