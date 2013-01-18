# -*- coding: utf-8 -*-

## SqlAlchemy Connection:

# 'mysql://user:password@localhost/dbname'
# 'postgres://user:password@localhost/dbname'
# 'oracle://user:password@localhost/dbname'
# 'mssql://user:password@mydsn'

# 'sqlite:///relative_path_to_dbname.db'
# 'sqlite:////absolute/path/to/dbname.db'

sqla_uri = 'sqlite:///memory'
sqla_params = {
    'echo': False,
    'encoding': 'utf-8'
}
