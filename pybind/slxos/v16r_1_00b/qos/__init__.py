
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import map_
import red_profile
import tx_queue
import rx_queue
import cpu
class qos(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_','__red_profile','__tx_queue','__rx_queue','__cpu',)

  _yang_name = 'qos'
  _rest_name = 'qos'

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
    self.__tx_queue = YANGDynClass(base=tx_queue.tx_queue, is_container='container', yang_name="tx-queue", rest_name="tx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Eegress Queue', u'callpoint': u'qos_transmit_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    self.__rx_queue = YANGDynClass(base=rx_queue.rx_queue, is_container='container', yang_name="rx-queue", rest_name="rx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Ingress Queue', u'callpoint': u'qos_receive_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    self.__red_profile = YANGDynClass(base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    self.__cpu = YANGDynClass(base=cpu.cpu, is_container='container', yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU QoS'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)

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
      return [u'qos']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos']

  def _get_map_(self):
    """
    Getter method for map_, mapped from YANG variable /qos/map (container)
    """
    return self.__map_
      
  def _set_map_(self, v, load=False):
    """
    Setter method for map_, mapped from YANG variable /qos/map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)""",
        })

    self.__map_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_(self):
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)


  def _get_red_profile(self):
    """
    Getter method for red_profile, mapped from YANG variable /qos/red_profile (list)
    """
    return self.__red_profile
      
  def _set_red_profile(self, v, load=False):
    """
    Setter method for red_profile, mapped from YANG variable /qos/red_profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_red_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_red_profile() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """red_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)""",
        })

    self.__red_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_red_profile(self):
    self.__red_profile = YANGDynClass(base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'RUNNCFG_LEVEL_SYSTEM_QOS', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='list', is_config=True)


  def _get_tx_queue(self):
    """
    Getter method for tx_queue, mapped from YANG variable /qos/tx_queue (container)
    """
    return self.__tx_queue
      
  def _set_tx_queue(self, v, load=False):
    """
    Setter method for tx_queue, mapped from YANG variable /qos/tx_queue (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_queue() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tx_queue.tx_queue, is_container='container', yang_name="tx-queue", rest_name="tx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Eegress Queue', u'callpoint': u'qos_transmit_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_queue must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tx_queue.tx_queue, is_container='container', yang_name="tx-queue", rest_name="tx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Eegress Queue', u'callpoint': u'qos_transmit_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)""",
        })

    self.__tx_queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_queue(self):
    self.__tx_queue = YANGDynClass(base=tx_queue.tx_queue, is_container='container', yang_name="tx-queue", rest_name="tx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Eegress Queue', u'callpoint': u'qos_transmit_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)


  def _get_rx_queue(self):
    """
    Getter method for rx_queue, mapped from YANG variable /qos/rx_queue (container)
    """
    return self.__rx_queue
      
  def _set_rx_queue(self, v, load=False):
    """
    Setter method for rx_queue, mapped from YANG variable /qos/rx_queue (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rx_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rx_queue() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rx_queue.rx_queue, is_container='container', yang_name="rx-queue", rest_name="rx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Ingress Queue', u'callpoint': u'qos_receive_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rx_queue must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rx_queue.rx_queue, is_container='container', yang_name="rx-queue", rest_name="rx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Ingress Queue', u'callpoint': u'qos_receive_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)""",
        })

    self.__rx_queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rx_queue(self):
    self.__rx_queue = YANGDynClass(base=rx_queue.rx_queue, is_container='container', yang_name="rx-queue", rest_name="rx-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Ingress Queue', u'callpoint': u'qos_receive_queue', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='container', is_config=True)


  def _get_cpu(self):
    """
    Getter method for cpu, mapped from YANG variable /qos/cpu (container)
    """
    return self.__cpu
      
  def _set_cpu(self, v, load=False):
    """
    Setter method for cpu, mapped from YANG variable /qos/cpu (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=cpu.cpu, is_container='container', yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU QoS'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=cpu.cpu, is_container='container', yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU QoS'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)""",
        })

    self.__cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu(self):
    self.__cpu = YANGDynClass(base=cpu.cpu, is_container='container', yang_name="cpu", rest_name="cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure CPU QoS'}}, namespace='urn:brocade.com:mgmt:brocade-qos-cpu', defining_module='brocade-qos-cpu', yang_type='container', is_config=True)

  map_ = __builtin__.property(_get_map_, _set_map_)
  red_profile = __builtin__.property(_get_red_profile, _set_red_profile)
  tx_queue = __builtin__.property(_get_tx_queue, _set_tx_queue)
  rx_queue = __builtin__.property(_get_rx_queue, _set_rx_queue)
  cpu = __builtin__.property(_get_cpu, _set_cpu)


  _pyangbind_elements = {'map_': map_, 'red_profile': red_profile, 'tx_queue': tx_queue, 'rx_queue': rx_queue, 'cpu': cpu, }


