
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import lacp
import xstp
import rpvst
import udld
import bfd_vxlan
import bfd_l3
import fcoe
class kap_custom_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-hardware - based on the path /hardware/custom-profile/kap-custom-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__lacp','__xstp','__rpvst','__udld','__bfd_vxlan','__bfd_l3','__fcoe',)

  _yang_name = 'kap-custom-profile'
  _rest_name = 'kap'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='string', is_config=True)
    self.__bfd_l3 = YANGDynClass(base=bfd_l3.bfd_l3, is_container='container', presence=False, yang_name="bfd-l3", rest_name="bfd-l3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-L3 protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__rpvst = YANGDynClass(base=rpvst.rpvst, is_container='container', presence=False, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RPVST protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__bfd_vxlan = YANGDynClass(base=bfd_vxlan.bfd_vxlan, is_container='container', presence=False, yang_name="bfd-vxlan", rest_name="bfd-vxlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-VXLAN protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__lacp = YANGDynClass(base=lacp.lacp, is_container='container', presence=False, yang_name="lacp", rest_name="lacp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LACP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__fcoe = YANGDynClass(base=fcoe.fcoe, is_container='container', presence=False, yang_name="fcoe", rest_name="fcoe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FCOE protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__udld = YANGDynClass(base=udld.udld, is_container='container', presence=False, yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure UDLD protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    self.__xstp = YANGDynClass(base=xstp.xstp, is_container='container', presence=False, yang_name="xstp", rest_name="xstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'hardware', u'custom-profile', u'kap-custom-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'hardware', u'custom-profile', u'kap']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/name (string)
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='string', is_config=True)


  def _get_lacp(self):
    """
    Getter method for lacp, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/lacp (container)
    """
    return self.__lacp
      
  def _set_lacp(self, v, load=False):
    """
    Setter method for lacp, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/lacp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lacp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lacp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lacp.lacp, is_container='container', presence=False, yang_name="lacp", rest_name="lacp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LACP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lacp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lacp.lacp, is_container='container', presence=False, yang_name="lacp", rest_name="lacp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LACP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__lacp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lacp(self):
    self.__lacp = YANGDynClass(base=lacp.lacp, is_container='container', presence=False, yang_name="lacp", rest_name="lacp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure LACP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_xstp(self):
    """
    Getter method for xstp, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/xstp (container)
    """
    return self.__xstp
      
  def _set_xstp(self, v, load=False):
    """
    Setter method for xstp, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/xstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_xstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_xstp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=xstp.xstp, is_container='container', presence=False, yang_name="xstp", rest_name="xstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """xstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=xstp.xstp, is_container='container', presence=False, yang_name="xstp", rest_name="xstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__xstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_xstp(self):
    self.__xstp = YANGDynClass(base=xstp.xstp, is_container='container', presence=False, yang_name="xstp", rest_name="xstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure xSTP protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_rpvst(self):
    """
    Getter method for rpvst, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/rpvst (container)
    """
    return self.__rpvst
      
  def _set_rpvst(self, v, load=False):
    """
    Setter method for rpvst, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/rpvst (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rpvst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rpvst() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rpvst.rpvst, is_container='container', presence=False, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RPVST protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rpvst must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rpvst.rpvst, is_container='container', presence=False, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RPVST protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__rpvst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rpvst(self):
    self.__rpvst = YANGDynClass(base=rpvst.rpvst, is_container='container', presence=False, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RPVST protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_udld(self):
    """
    Getter method for udld, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/udld (container)
    """
    return self.__udld
      
  def _set_udld(self, v, load=False):
    """
    Setter method for udld, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/udld (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_udld is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_udld() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=udld.udld, is_container='container', presence=False, yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure UDLD protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """udld must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=udld.udld, is_container='container', presence=False, yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure UDLD protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__udld = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_udld(self):
    self.__udld = YANGDynClass(base=udld.udld, is_container='container', presence=False, yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure UDLD protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_bfd_vxlan(self):
    """
    Getter method for bfd_vxlan, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/bfd_vxlan (container)
    """
    return self.__bfd_vxlan
      
  def _set_bfd_vxlan(self, v, load=False):
    """
    Setter method for bfd_vxlan, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/bfd_vxlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_vxlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_vxlan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bfd_vxlan.bfd_vxlan, is_container='container', presence=False, yang_name="bfd-vxlan", rest_name="bfd-vxlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-VXLAN protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_vxlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bfd_vxlan.bfd_vxlan, is_container='container', presence=False, yang_name="bfd-vxlan", rest_name="bfd-vxlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-VXLAN protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__bfd_vxlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_vxlan(self):
    self.__bfd_vxlan = YANGDynClass(base=bfd_vxlan.bfd_vxlan, is_container='container', presence=False, yang_name="bfd-vxlan", rest_name="bfd-vxlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-VXLAN protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_bfd_l3(self):
    """
    Getter method for bfd_l3, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/bfd_l3 (container)
    """
    return self.__bfd_l3
      
  def _set_bfd_l3(self, v, load=False):
    """
    Setter method for bfd_l3, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/bfd_l3 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_l3 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_l3() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bfd_l3.bfd_l3, is_container='container', presence=False, yang_name="bfd-l3", rest_name="bfd-l3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-L3 protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_l3 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bfd_l3.bfd_l3, is_container='container', presence=False, yang_name="bfd-l3", rest_name="bfd-l3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-L3 protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__bfd_l3 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_l3(self):
    self.__bfd_l3 = YANGDynClass(base=bfd_l3.bfd_l3, is_container='container', presence=False, yang_name="bfd-l3", rest_name="bfd-l3", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD-L3 protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)


  def _get_fcoe(self):
    """
    Getter method for fcoe, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/fcoe (container)
    """
    return self.__fcoe
      
  def _set_fcoe(self, v, load=False):
    """
    Setter method for fcoe, mapped from YANG variable /hardware/custom_profile/kap_custom_profile/fcoe (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fcoe.fcoe, is_container='container', presence=False, yang_name="fcoe", rest_name="fcoe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FCOE protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fcoe.fcoe, is_container='container', presence=False, yang_name="fcoe", rest_name="fcoe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FCOE protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)""",
        })

    self.__fcoe = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe(self):
    self.__fcoe = YANGDynClass(base=fcoe.fcoe, is_container='container', presence=False, yang_name="fcoe", rest_name="fcoe", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure FCOE protocol KAP parameters', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  lacp = __builtin__.property(_get_lacp, _set_lacp)
  xstp = __builtin__.property(_get_xstp, _set_xstp)
  rpvst = __builtin__.property(_get_rpvst, _set_rpvst)
  udld = __builtin__.property(_get_udld, _set_udld)
  bfd_vxlan = __builtin__.property(_get_bfd_vxlan, _set_bfd_vxlan)
  bfd_l3 = __builtin__.property(_get_bfd_l3, _set_bfd_l3)
  fcoe = __builtin__.property(_get_fcoe, _set_fcoe)


  _pyangbind_elements = {'name': name, 'lacp': lacp, 'xstp': xstp, 'rpvst': rpvst, 'udld': udld, 'bfd_vxlan': bfd_vxlan, 'bfd_l3': bfd_l3, 'fcoe': fcoe, }


