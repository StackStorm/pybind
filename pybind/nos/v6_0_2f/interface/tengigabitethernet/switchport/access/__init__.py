
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rspan_access
class access(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/switchport/access. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The access layer characteristics of this 
interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__accessvlan','__rspan_access',)

  _yang_name = 'access'
  _rest_name = 'access'

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
    self.__rspan_access = YANGDynClass(base=rspan_access.rspan_access, is_container='container', presence=False, yang_name="rspan-access", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__accessvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="accessvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the default VLAN for the interface', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'switchport', u'access']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'switchport', u'access']

  def _get_accessvlan(self):
    """
    Getter method for accessvlan, mapped from YANG variable /interface/tengigabitethernet/switchport/access/accessvlan (vlan-type)

    YANG Description: This specifies the access vlan for this 
interface.
    """
    return self.__accessvlan
      
  def _set_accessvlan(self, v, load=False):
    """
    Setter method for accessvlan, mapped from YANG variable /interface/tengigabitethernet/switchport/access/accessvlan (vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accessvlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accessvlan() directly.

    YANG Description: This specifies the access vlan for this 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="accessvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the default VLAN for the interface', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accessvlan must be of a type compatible with vlan-type""",
          'defined-type': "brocade-interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="accessvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the default VLAN for the interface', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)""",
        })

    self.__accessvlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accessvlan(self):
    self.__accessvlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="accessvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the default VLAN for the interface', u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='vlan-type', is_config=True)


  def _get_rspan_access(self):
    """
    Getter method for rspan_access, mapped from YANG variable /interface/tengigabitethernet/switchport/access/rspan_access (container)

    YANG Description: The access layer characteristics of this 
interface.
    """
    return self.__rspan_access
      
  def _set_rspan_access(self, v, load=False):
    """
    Setter method for rspan_access, mapped from YANG variable /interface/tengigabitethernet/switchport/access/rspan_access (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rspan_access is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rspan_access() directly.

    YANG Description: The access layer characteristics of this 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rspan_access.rspan_access, is_container='container', presence=False, yang_name="rspan-access", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rspan_access must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rspan_access.rspan_access, is_container='container', presence=False, yang_name="rspan-access", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__rspan_access = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rspan_access(self):
    self.__rspan_access = YANGDynClass(base=rspan_access.rspan_access, is_container='container', presence=False, yang_name="rspan-access", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-drop-node-name': None, u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  accessvlan = __builtin__.property(_get_accessvlan, _set_accessvlan)
  rspan_access = __builtin__.property(_get_rspan_access, _set_rspan_access)


  _pyangbind_elements = {'accessvlan': accessvlan, 'rspan_access': rspan_access, }

