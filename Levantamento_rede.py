# coding: utf-8
import os
import pandas as pd
from subprocess import Popen
os.system(r'CSVDE -f "C:.csv" -r objectClass=user -l "givenName, sn, objectClass, cn, displayName, sAMAccountName, department, description, mail, logonCount, whenCreated, whenChanged"')
os.system(r'net group /domain > "C:.csv"')
usuarios_computadores_rede = pd.read_csv(r'C:.csv', encoding='iso-8859-13')
usuarios_computadores_rede = usuarios_computadores_rede.reindex(columns=(['sAMAccountName'] + list([a for a in usuarios_computadores_rede.columns if a != 'sAMAccountname']) ))
usuarios_rede = usuarios_computadores_rede.loc[usuarios_computadores_rede['objectClass'] == 'user']
usuarios_rede.to_csv(r"C:.txt", index=False)
q = Popen("S1.consulta_detalhada_usuarios_serv.bat", cwd=r"C:")
stdout, stderr = q.communicate()