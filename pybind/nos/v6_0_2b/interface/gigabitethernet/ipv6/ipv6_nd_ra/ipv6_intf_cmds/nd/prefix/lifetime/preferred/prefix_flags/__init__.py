
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class prefix_flags(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/ipv6/ipv6-nd-ra/ipv6-intf-cmds/nd/prefix/lifetime/preferred/prefix-flags. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__no_autoconfig','__no_onlink','__off_link',)

  _yang_name = 'prefix-flags'
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
    self.__no_autoconfig = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-autoconfig", rest_name="no-autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for autoconfiguration', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__off_link = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="off-link", rest_name="off-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix is offlink', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__no_onlink = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-onlink", rest_name="no-onlink", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for onlink determination', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds', u'nd', u'prefix', u'lifetime', u'preferred', u'prefix-flags']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'ipv6', u'nd', u'prefix']

  def _get_no_autoconfig(self):
    """
    Getter method for no_autoconfig, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags/no_autoconfig (empty)
    """
    return self.__no_autoconfig
      
  def _set_no_autoconfig(self, v, load=False):
    """
    Setter method for no_autoconfig, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags/no_autoconfig (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_autoconfig is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_autoconfig() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="no-autoconfig", rest_name="no-autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for autoconfiguration', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_autoconfig must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-autoconfig", rest_name="no-autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for autoconfiguration', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__no_autoconfig = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_autoconfig(self):
    self.__no_autoconfig = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-autoconfig", rest_name="no-autoconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for autoconfiguration', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_no_onlink(self):
    """
    Getter method for no_onlink, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags/no_onlink (empty)
    """
    return self.__no_onlink
      
  def _set_no_onlink(self, v, load=False):
    """
    Setter method for no_onlink, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags/no_onlink (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_onlink is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_onlink() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="no-onlink", rest_name="no-onlink", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for onlink determination', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_onlink must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-onlink", rest_name="no-onlink", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for onlink determination', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__no_onlink = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_onlink(self):
    self.__no_onlink = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-onlink", rest_name="no-onlink", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not use prefix for onlink determination', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_off_link(self):
    """
    Getter method for off_link, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags/off_link (empty)
    """
    return self.__off_link
      
  def _set_off_link(self, v, load=False):
    """
    Setter method for off_link, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags/off_link (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_off_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_off_link() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="off-link", rest_name="off-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix is offlink', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """off_link must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="off-link", rest_name="off-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix is offlink', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__off_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_off_link(self):
    self.__off_link = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="off-link", rest_name="off-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Prefix is offlink', u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

  no_autoconfig = __builtin__.property(_get_no_autoconfig, _set_no_autoconfig)
  no_onlink = __builtin__.property(_get_no_onlink, _set_no_onlink)
  off_link = __builtin__.property(_get_off_link, _set_off_link)


  _pyangbind_elements = {'no_autoconfig': no_autoconfig, 'no_onlink': no_onlink, 'off_link': off_link, }


