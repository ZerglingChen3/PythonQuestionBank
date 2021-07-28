from model import person as ops
from model import list as ls
from manage import initdata as init
import pandas as pd
import pandas.io.formats.excel


def appendPerson(new_person):
    df = pd.read_excel(init.user_path)
    ls.user_list.append(new_person)
    ds = pd.DataFrame({"序号": [str(len(ls.user_list))],
                       "姓名": [new_person.getName()],
                       "密码": [new_person.getPassword()],
                       "权限": [new_person.getPermission()]})
    df = df.append(ds)
    df.to_excel(init.user_path, index=False, header=True)
