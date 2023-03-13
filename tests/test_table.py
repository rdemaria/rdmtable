import numpy as np

from rdmtable import RDMTable

data = {
    "name": np.array(["ip1", "ip2", "ip3"]),
    "s": np.array([1.0, 2.0, 3.0]),
    "betx": np.array([4.0, 5.0, 6.0]),
    "bety": np.array([2.0, 3.0, 4.0]),
}


t = RDMTable(data)

# Column selection
t.betx  # return array
t["betx"]  # return array
t["betx", 0]  # return scalar
t["sqrt(betx)"]  # return array
t["betx bety"]  # return table
t[["betx", "bety"]]  # return table
t["sqrt(betx)>3 sqrt(bety)"]  # return table


# Row selection
t[:, 1]  # return a new table with row
t[:, [0, 2]]  # return a new table with 3 rows
t[:, t.s > 1]  # table with a selection of rows

t[:, "ip1"]  # table with rows fullmathcing name
t[:, "ip[23]"]  # table with rows mathcing name
t[:, "ip.*##1"]  # == t[:,'ip.*'][:,1]
t[:, "notthere"]  # empty table
t[:, ["ip1", "ip2"]]  # table with row selection

t[:, 1:4:3]  # return table slice
t[:, 1.5:2.5:"s"]  # return t.s>=1.5 & t.<=4
t[:, "ip1":"ip3"]  # return t from first 'ip1' to last 'ip3' in t.name
t[:, "ip.*##1":"ip.*##2"]  # return t from first 'ip2' to third 'ip3'
t[:, "ip2%%-1":"ip2%%+1"]  # return t from first 'ip1' to last 'ip3' in t.name
t[:, "ip1":"ip3":"name"]  # return t from first 'a' to last 'b' in t.name
t[:, None] # copy
t[:, :] # copy
