
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import standard
import extended
class vxlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vxlan-visibility - based on the path /overlay/access-list/type/vxlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__standard','__extended',)

  _yang_name = 'vxlan'
  _rest_name = 'vxlan'

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
    self.__extended = YANGDynClass(base=YANGListType("ext_user_acl_name",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-user-acl-name', extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)
    self.__standard = YANGDynClass(base=YANGListType("user_acl_name",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='user-acl-name', extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)

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
      return [u'overlay', u'access-list', u'type', u'vxlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay', u'access-list', u'type', u'vxlan']

  def _get_standard(self):
    """
    Getter method for standard, mapped from YANG variable /overlay/access_list/type/vxlan/standard (list)
    """
    return self.__standard
      
  def _set_standard(self, v, load=False):
    """
    Setter method for standard, mapped from YANG variable /overlay/access_list/type/vxlan/standard (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_standard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_standard() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("user_acl_name",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='user-acl-name', extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """standard must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("user_acl_name",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='user-acl-name', extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)""",
        })

    self.__standard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_standard(self):
    self.__standard = YANGDynClass(base=YANGListType("user_acl_name",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='user-acl-name', extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityStandardCallpoint', u'cli-mode-name': u'config-overlay-vxlan-std-$(user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)


  def _get_extended(self):
    """
    Getter method for extended, mapped from YANG variable /overlay/access_list/type/vxlan/extended (list)
    """
    return self.__extended
      
  def _set_extended(self, v, load=False):
    """
    Setter method for extended, mapped from YANG variable /overlay/access_list/type/vxlan/extended (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ext_user_acl_name",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-user-acl-name', extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ext_user_acl_name",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-user-acl-name', extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)""",
        })

    self.__extended = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended(self):
    self.__extended = YANGDynClass(base=YANGListType("ext_user_acl_name",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ext-user-acl-name', extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'extended <user-acl-name>', u'cli-sequence-commands': None, u'callpoint': u'VxlanVisibilityExtendedCallpoint', u'cli-mode-name': u'config-overlay-vxlan-ext-$(ext-user-acl-name)'}}, namespace='urn:brocade.com:mgmt:brocade-vxlan-visibility', defining_module='brocade-vxlan-visibility', yang_type='list', is_config=True)

  standard = __builtin__.property(_get_standard, _set_standard)
  extended = __builtin__.property(_get_extended, _set_extended)


  _pyangbind_elements = {'standard': standard, 'extended': extended, }


