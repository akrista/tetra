"""Base Database Seeder Module."""

from masoniteorm.seeds import Seeder

from .tenant_table_seeder import TenantTableSeeder
from .user_table_seeder import UserTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(TenantTableSeeder)
        self.call(UserTableSeeder)
