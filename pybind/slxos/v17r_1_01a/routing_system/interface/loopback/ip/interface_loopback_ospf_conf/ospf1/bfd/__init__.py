
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/loopback/ip/interface-loopback-ospf-conf/ospf1/bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Set Bidirectional Forwarding Detection operation mode on this interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__intf_bfd_enable',)

  _yang_name = 'bfd'
  _rest_name = 'bfd'

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
    self.__intf_bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="intf-bfd-enable", rest_name="intf-bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Enable bfd on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'interface', u'loopback', u'ip', u'interface-loopback-ospf-conf', u'ospf1', u'bfd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Loopback', u'ip', u'ospf', u'bfd']

  def _get_intf_bfd_enable(self):
    """
    Getter method for intf_bfd_enable, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf/ospf1/bfd/intf_bfd_enable (empty)

    YANG Description: Enable bfd on this interface
    """
    return self.__intf_bfd_enable
      
  def _set_intf_bfd_enable(self, v, load=False):
    """
    Setter method for intf_bfd_enable, mapped from YANG variable /routing_system/interface/loopback/ip/interface_loopback_ospf_conf/ospf1/bfd/intf_bfd_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_intf_bfd_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_intf_bfd_enable() directly.

    YANG Description: Enable bfd on this interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="intf-bfd-enable", rest_name="intf-bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Enable bfd on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """intf_bfd_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="intf-bfd-enable", rest_name="intf-bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Enable bfd on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__intf_bfd_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_intf_bfd_enable(self):
    self.__intf_bfd_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="intf-bfd-enable", rest_name="intf-bfd-enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'Enable bfd on this interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

  intf_bfd_enable = __builtin__.property(_get_intf_bfd_enable, _set_intf_bfd_enable)


  _pyangbind_elements = {'intf_bfd_enable': intf_bfd_enable, }


