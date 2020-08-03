#! /usr/bin/env python

"""
This is a test script will print out the structure (seqences) of the
JPARC linac.
"""

import sys
import time

# import the XmlDataAdaptor XML parser
from orbit.utils.xml import XmlDataAdaptor

print "============================================="

#---- the XML file name with the structure
xml_file_name = "../jparc_linac_lattice_xml/jparc_linac.xml"
acc_da = XmlDataAdaptor.adaptorForFile(xml_file_name)

sequences_da = acc_da.childAdaptors()
for seq_da in sequences_da:
	print "seq=",seq_da.getName()," length[m]=",seq_da.doubleValue("length")," n_elemnts=",len(seq_da.childAdaptors())