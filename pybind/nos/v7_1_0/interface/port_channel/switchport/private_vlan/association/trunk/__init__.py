
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class trunk(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/switchport/private-vlan/association/trunk. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trunk_pri_pvlan','__trunk_sec_pvlan',)

  _yang_name = 'trunk'
  _rest_name = 'trunk'

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
    self.__trunk_sec_pvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-sec-pvlan", rest_name="trunk-sec-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan id ', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    self.__trunk_pri_pvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-pri-pvlan", rest_name="trunk-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)

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
      return [u'interface', u'port-channel', u'switchport', u'private-vlan', u'association', u'trunk']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'switchport', u'private-vlan', u'association', u'trunk']

  def _get_trunk_pri_pvlan(self):
    """
    Getter method for trunk_pri_pvlan, mapped from YANG variable /interface/port_channel/switchport/private_vlan/association/trunk/trunk_pri_pvlan (vlan-type)
    """
    return self.__trunk_pri_pvlan
      
  def _set_trunk_pri_pvlan(self, v, load=False):
    """
    Setter method for trunk_pri_pvlan, mapped from YANG variable /interface/port_channel/switchport/private_vlan/association/trunk/trunk_pri_pvlan (vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_pri_pvlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_pri_pvlan() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-pri-pvlan", rest_name="trunk-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_pri_pvlan must be of a type compatible with vlan-type""",
          'defined-type': "brocade-interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-pri-pvlan", rest_name="trunk-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)""",
        })

    self.__trunk_pri_pvlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_pri_pvlan(self):
    self.__trunk_pri_pvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-pri-pvlan", rest_name="trunk-pri-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Primary vlan id', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)


  def _get_trunk_sec_pvlan(self):
    """
    Getter method for trunk_sec_pvlan, mapped from YANG variable /interface/port_channel/switchport/private_vlan/association/trunk/trunk_sec_pvlan (vlan-type)
    """
    return self.__trunk_sec_pvlan
      
  def _set_trunk_sec_pvlan(self, v, load=False):
    """
    Setter method for trunk_sec_pvlan, mapped from YANG variable /interface/port_channel/switchport/private_vlan/association/trunk/trunk_sec_pvlan (vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_sec_pvlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_sec_pvlan() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-sec-pvlan", rest_name="trunk-sec-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan id ', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_sec_pvlan must be of a type compatible with vlan-type""",
          'defined-type': "brocade-interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-sec-pvlan", rest_name="trunk-sec-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan id ', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)""",
        })

    self.__trunk_sec_pvlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_sec_pvlan(self):
    self.__trunk_sec_pvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="trunk-sec-pvlan", rest_name="trunk-sec-pvlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Secondary vlan id ', u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)

  trunk_pri_pvlan = __builtin__.property(_get_trunk_pri_pvlan, _set_trunk_pri_pvlan)
  trunk_sec_pvlan = __builtin__.property(_get_trunk_sec_pvlan, _set_trunk_sec_pvlan)


  _pyangbind_elements = {'trunk_pri_pvlan': trunk_pri_pvlan, 'trunk_sec_pvlan': trunk_sec_pvlan, }


