
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import prefix
import key
class ldp_fec_prefixes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/fec/ldp-fec-prefixes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tot_no_of_prefix_fec','__tot_no_of_prefix_fec_installed','__tot_no_of_prefix_fec_filtered','__tot_no_of_prefix_fec_lwd','__filtered','__prefix_filtered','__prefix','__key',)

  _yang_name = 'ldp-fec-prefixes'
  _rest_name = 'ldp-fec-prefixes'

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
    self.__prefix_filtered = YANGDynClass(base=unicode, is_leaf=True, yang_name="prefix-filtered", rest_name="prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__tot_no_of_prefix_fec_installed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-installed", rest_name="tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__tot_no_of_prefix_fec = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec", rest_name="tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__prefix = YANGDynClass(base=YANGListType("destination",prefix.prefix, yang_name="prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}), is_container='list', yang_name="prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__tot_no_of_prefix_fec_lwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-lwd", rest_name="tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__key = YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__filtered = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filtered': {'value': 1}, u'filtered-in': {'value': 2}, u'filtered-out': {'value': 3}},), is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='fec-filter-type', is_config=False)
    self.__tot_no_of_prefix_fec_filtered = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-filtered", rest_name="tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefixes']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefixes']

  def _get_tot_no_of_prefix_fec(self):
    """
    Getter method for tot_no_of_prefix_fec, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec (uint32)

    YANG Description: tot_no_of_prefix_fec
    """
    return self.__tot_no_of_prefix_fec
      
  def _set_tot_no_of_prefix_fec(self, v, load=False):
    """
    Setter method for tot_no_of_prefix_fec, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tot_no_of_prefix_fec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tot_no_of_prefix_fec() directly.

    YANG Description: tot_no_of_prefix_fec
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec", rest_name="tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tot_no_of_prefix_fec must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec", rest_name="tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tot_no_of_prefix_fec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tot_no_of_prefix_fec(self):
    self.__tot_no_of_prefix_fec = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec", rest_name="tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_tot_no_of_prefix_fec_installed(self):
    """
    Getter method for tot_no_of_prefix_fec_installed, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec_installed (uint32)

    YANG Description: tot_no_of_prefix_fec_installed
    """
    return self.__tot_no_of_prefix_fec_installed
      
  def _set_tot_no_of_prefix_fec_installed(self, v, load=False):
    """
    Setter method for tot_no_of_prefix_fec_installed, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec_installed (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tot_no_of_prefix_fec_installed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tot_no_of_prefix_fec_installed() directly.

    YANG Description: tot_no_of_prefix_fec_installed
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-installed", rest_name="tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tot_no_of_prefix_fec_installed must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-installed", rest_name="tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tot_no_of_prefix_fec_installed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tot_no_of_prefix_fec_installed(self):
    self.__tot_no_of_prefix_fec_installed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-installed", rest_name="tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_tot_no_of_prefix_fec_filtered(self):
    """
    Getter method for tot_no_of_prefix_fec_filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec_filtered (uint32)

    YANG Description: tot_no_of_prefix_fec_filtered
    """
    return self.__tot_no_of_prefix_fec_filtered
      
  def _set_tot_no_of_prefix_fec_filtered(self, v, load=False):
    """
    Setter method for tot_no_of_prefix_fec_filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec_filtered (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tot_no_of_prefix_fec_filtered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tot_no_of_prefix_fec_filtered() directly.

    YANG Description: tot_no_of_prefix_fec_filtered
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-filtered", rest_name="tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tot_no_of_prefix_fec_filtered must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-filtered", rest_name="tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tot_no_of_prefix_fec_filtered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tot_no_of_prefix_fec_filtered(self):
    self.__tot_no_of_prefix_fec_filtered = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-filtered", rest_name="tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_tot_no_of_prefix_fec_lwd(self):
    """
    Getter method for tot_no_of_prefix_fec_lwd, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec_lwd (uint32)

    YANG Description: tot_no_of_prefix_fec_lwd
    """
    return self.__tot_no_of_prefix_fec_lwd
      
  def _set_tot_no_of_prefix_fec_lwd(self, v, load=False):
    """
    Setter method for tot_no_of_prefix_fec_lwd, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/tot_no_of_prefix_fec_lwd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tot_no_of_prefix_fec_lwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tot_no_of_prefix_fec_lwd() directly.

    YANG Description: tot_no_of_prefix_fec_lwd
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-lwd", rest_name="tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tot_no_of_prefix_fec_lwd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-lwd", rest_name="tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tot_no_of_prefix_fec_lwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tot_no_of_prefix_fec_lwd(self):
    self.__tot_no_of_prefix_fec_lwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tot-no-of-prefix-fec-lwd", rest_name="tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_filtered(self):
    """
    Getter method for filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/filtered (fec-filter-type)

    YANG Description: Filter Type
    """
    return self.__filtered
      
  def _set_filtered(self, v, load=False):
    """
    Setter method for filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/filtered (fec-filter-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filtered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filtered() directly.

    YANG Description: Filter Type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filtered': {'value': 1}, u'filtered-in': {'value': 2}, u'filtered-out': {'value': 3}},), is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='fec-filter-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filtered must be of a type compatible with fec-filter-type""",
          'defined-type': "brocade-mpls-operational:fec-filter-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filtered': {'value': 1}, u'filtered-in': {'value': 2}, u'filtered-out': {'value': 3}},), is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='fec-filter-type', is_config=False)""",
        })

    self.__filtered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filtered(self):
    self.__filtered = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'filtered': {'value': 1}, u'filtered-in': {'value': 2}, u'filtered-out': {'value': 3}},), is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='fec-filter-type', is_config=False)


  def _get_prefix_filtered(self):
    """
    Getter method for prefix_filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix_filtered (string)

    YANG Description: filter name
    """
    return self.__prefix_filtered
      
  def _set_prefix_filtered(self, v, load=False):
    """
    Setter method for prefix_filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix_filtered (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_filtered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_filtered() directly.

    YANG Description: filter name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="prefix-filtered", rest_name="prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_filtered must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="prefix-filtered", rest_name="prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__prefix_filtered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_filtered(self):
    self.__prefix_filtered = YANGDynClass(base=unicode, is_leaf=True, yang_name="prefix-filtered", rest_name="prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix (list)
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("destination",prefix.prefix, yang_name="prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}), is_container='list', yang_name="prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("destination",prefix.prefix, yang_name="prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}), is_container='list', yang_name="prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(base=YANGListType("destination",prefix.prefix, yang_name="prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='destination', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}), is_container='list', yang_name="prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_key(self):
    """
    Getter method for key, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/key (container)
    """
    return self.__key
      
  def _set_key(self, v, load=False):
    """
    Setter method for key, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/key (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key(self):
    self.__key = YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-key-key-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

  tot_no_of_prefix_fec = __builtin__.property(_get_tot_no_of_prefix_fec)
  tot_no_of_prefix_fec_installed = __builtin__.property(_get_tot_no_of_prefix_fec_installed)
  tot_no_of_prefix_fec_filtered = __builtin__.property(_get_tot_no_of_prefix_fec_filtered)
  tot_no_of_prefix_fec_lwd = __builtin__.property(_get_tot_no_of_prefix_fec_lwd)
  filtered = __builtin__.property(_get_filtered)
  prefix_filtered = __builtin__.property(_get_prefix_filtered)
  prefix = __builtin__.property(_get_prefix)
  key = __builtin__.property(_get_key)


  _pyangbind_elements = {'tot_no_of_prefix_fec': tot_no_of_prefix_fec, 'tot_no_of_prefix_fec_installed': tot_no_of_prefix_fec_installed, 'tot_no_of_prefix_fec_filtered': tot_no_of_prefix_fec_filtered, 'tot_no_of_prefix_fec_lwd': tot_no_of_prefix_fec_lwd, 'filtered': filtered, 'prefix_filtered': prefix_filtered, 'prefix': prefix, 'key': key, }


