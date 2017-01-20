
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vni_add
import evpn_vni
class vni(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/evpn-instance/vni. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vni_add','__evpn_vni',)

  _yang_name = 'vni'
  _rest_name = 'vni'

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
    self.__evpn_vni = YANGDynClass(base=YANGListType("vni_number",evpn_vni.evpn_vni, yang_name="evpn-vni", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni-number', extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}), is_container='list', yang_name="evpn-vni", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    self.__vni_add = YANGDynClass(base=vni_add.vni_add, is_container='container', presence=False, yang_name="vni-add", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Remove VNIs from EVPN Instance', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'evpn-instance', u'vni']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'evpn-instance', u'vni']

  def _get_vni_add(self):
    """
    Getter method for vni_add, mapped from YANG variable /rbridge_id/evpn_instance/vni/vni_add (container)
    """
    return self.__vni_add
      
  def _set_vni_add(self, v, load=False):
    """
    Setter method for vni_add, mapped from YANG variable /rbridge_id/evpn_instance/vni/vni_add (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vni_add is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vni_add() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vni_add.vni_add, is_container='container', presence=False, yang_name="vni-add", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Remove VNIs from EVPN Instance', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vni_add must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vni_add.vni_add, is_container='container', presence=False, yang_name="vni-add", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Remove VNIs from EVPN Instance', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__vni_add = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vni_add(self):
    self.__vni_add = YANGDynClass(base=vni_add.vni_add, is_container='container', presence=False, yang_name="vni-add", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Remove VNIs from EVPN Instance', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_evpn_vni(self):
    """
    Getter method for evpn_vni, mapped from YANG variable /rbridge_id/evpn_instance/vni/evpn_vni (list)

    YANG Description: EVPN instance config
    """
    return self.__evpn_vni
      
  def _set_evpn_vni(self, v, load=False):
    """
    Setter method for evpn_vni, mapped from YANG variable /rbridge_id/evpn_instance/vni/evpn_vni (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_vni is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_vni() directly.

    YANG Description: EVPN instance config
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vni_number",evpn_vni.evpn_vni, yang_name="evpn-vni", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni-number', extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}), is_container='list', yang_name="evpn-vni", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_vni must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vni_number",evpn_vni.evpn_vni, yang_name="evpn-vni", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni-number', extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}), is_container='list', yang_name="evpn-vni", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__evpn_vni = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_vni(self):
    self.__evpn_vni = YANGDynClass(base=YANGListType("vni_number",evpn_vni.evpn_vni, yang_name="evpn-vni", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vni-number', extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}), is_container='list', yang_name="evpn-vni", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VNI configuration', u'cli-no-key-completion': None, u'callpoint': u'EvpnVniConfig', u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'evpn-vni-$(vni-number)'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

  vni_add = __builtin__.property(_get_vni_add, _set_vni_add)
  evpn_vni = __builtin__.property(_get_evpn_vni, _set_evpn_vni)


  _pyangbind_elements = {'vni_add': vni_add, 'evpn_vni': evpn_vni, }


