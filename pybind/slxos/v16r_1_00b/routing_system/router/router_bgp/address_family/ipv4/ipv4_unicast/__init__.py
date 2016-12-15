
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import default_vrf
import af_vrf
class ipv4_unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__default_vrf','__af_vrf',)

  _yang_name = 'ipv4-unicast'
  _rest_name = 'unicast'

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
    self.__af_vrf = YANGDynClass(base=YANGListType("af_vrf_name",af_vrf.af_vrf, yang_name="af-vrf", rest_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vrf-name', extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}), is_container='list', yang_name="af-vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__default_vrf = YANGDynClass(base=default_vrf.default_vrf, is_container='container', yang_name="default-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 unicast address Family', u'cli-suppress-no': None, u'cli-add-mode': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'callpoint': u'AfIpv4Ucast', u'cli-mode-name': u'config-bgp-ipv4u'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast']

  def _get_default_vrf(self):
    """
    Getter method for default_vrf, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf (container)
    """
    return self.__default_vrf
      
  def _set_default_vrf(self, v, load=False):
    """
    Setter method for default_vrf, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_vrf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=default_vrf.default_vrf, is_container='container', yang_name="default-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 unicast address Family', u'cli-suppress-no': None, u'cli-add-mode': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'callpoint': u'AfIpv4Ucast', u'cli-mode-name': u'config-bgp-ipv4u'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_vrf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_vrf.default_vrf, is_container='container', yang_name="default-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 unicast address Family', u'cli-suppress-no': None, u'cli-add-mode': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'callpoint': u'AfIpv4Ucast', u'cli-mode-name': u'config-bgp-ipv4u'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__default_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_vrf(self):
    self.__default_vrf = YANGDynClass(base=default_vrf.default_vrf, is_container='container', yang_name="default-vrf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 unicast address Family', u'cli-suppress-no': None, u'cli-add-mode': None, u'cli-drop-node-name': None, u'cli-full-command': None, u'callpoint': u'AfIpv4Ucast', u'cli-mode-name': u'config-bgp-ipv4u'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_af_vrf(self):
    """
    Getter method for af_vrf, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf (list)
    """
    return self.__af_vrf
      
  def _set_af_vrf(self, v, load=False):
    """
    Setter method for af_vrf, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_vrf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("af_vrf_name",af_vrf.af_vrf, yang_name="af-vrf", rest_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vrf-name', extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}), is_container='list', yang_name="af-vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_vrf must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("af_vrf_name",af_vrf.af_vrf, yang_name="af-vrf", rest_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vrf-name', extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}), is_container='list', yang_name="af-vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__af_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_vrf(self):
    self.__af_vrf = YANGDynClass(base=YANGListType("af_vrf_name",af_vrf.af_vrf, yang_name="af-vrf", rest_name="vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vrf-name', extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}), is_container='list', yang_name="af-vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF unicast', u'alt-name': u'vrf', u'cli-suppress-list-no': None, u'callpoint': u'AfIpv4UcastVrf', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-ipv4u-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

  default_vrf = __builtin__.property(_get_default_vrf, _set_default_vrf)
  af_vrf = __builtin__.property(_get_af_vrf, _set_af_vrf)


  _pyangbind_elements = {'default_vrf': default_vrf, 'af_vrf': af_vrf, }


