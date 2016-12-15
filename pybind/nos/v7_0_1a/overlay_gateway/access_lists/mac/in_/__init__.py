
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class in_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway/access-lists/mac/in. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_acl_in_name','__mac_acl_in_dir',)

  _yang_name = 'in'
  _rest_name = ''

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
    self.__mac_acl_in_dir = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-acl-in-dir", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group in ingress direction', u'alt-name': u'in', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    self.__mac_acl_in_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-acl-in-name", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group name', u'alt-name': u'access-group', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-acl-name', is_config=True)

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
      return [u'overlay-gateway', u'access-lists', u'mac', u'in']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-gateway', u'mac']

  def _get_mac_acl_in_name(self):
    """
    Getter method for mac_acl_in_name, mapped from YANG variable /overlay_gateway/access_lists/mac/in/mac_acl_in_name (mac-access-list:mac-acl-name)
    """
    return self.__mac_acl_in_name
      
  def _set_mac_acl_in_name(self, v, load=False):
    """
    Setter method for mac_acl_in_name, mapped from YANG variable /overlay_gateway/access_lists/mac/in/mac_acl_in_name (mac-access-list:mac-acl-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_acl_in_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_acl_in_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-acl-in-name", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group name', u'alt-name': u'access-group', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-acl-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_acl_in_name must be of a type compatible with mac-access-list:mac-acl-name""",
          'defined-type': "mac-access-list:mac-acl-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-acl-in-name", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group name', u'alt-name': u'access-group', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-acl-name', is_config=True)""",
        })

    self.__mac_acl_in_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_acl_in_name(self):
    self.__mac_acl_in_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="mac-acl-in-name", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group name', u'alt-name': u'access-group', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='mac-access-list:mac-acl-name', is_config=True)


  def _get_mac_acl_in_dir(self):
    """
    Getter method for mac_acl_in_dir, mapped from YANG variable /overlay_gateway/access_lists/mac/in/mac_acl_in_dir (empty)
    """
    return self.__mac_acl_in_dir
      
  def _set_mac_acl_in_dir(self, v, load=False):
    """
    Setter method for mac_acl_in_dir, mapped from YANG variable /overlay_gateway/access_lists/mac/in/mac_acl_in_dir (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_acl_in_dir is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_acl_in_dir() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mac-acl-in-dir", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group in ingress direction', u'alt-name': u'in', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_acl_in_dir must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-acl-in-dir", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group in ingress direction', u'alt-name': u'in', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)""",
        })

    self.__mac_acl_in_dir = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_acl_in_dir(self):
    self.__mac_acl_in_dir = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mac-acl-in-dir", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC access-group in ingress direction', u'alt-name': u'in', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)

  mac_acl_in_name = __builtin__.property(_get_mac_acl_in_name, _set_mac_acl_in_name)
  mac_acl_in_dir = __builtin__.property(_get_mac_acl_in_dir, _set_mac_acl_in_dir)


  _pyangbind_elements = {'mac_acl_in_name': mac_acl_in_name, 'mac_acl_in_dir': mac_acl_in_dir, }


