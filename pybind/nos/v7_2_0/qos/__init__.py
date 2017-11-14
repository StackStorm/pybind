
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
import ecn
import queue
import rcv_queue
class qos(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /qos. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_','__red_profile','__ecn','__queue','__rcv_queue',)

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
    self.__queue = YANGDynClass(base=queue.queue, is_container='container', presence=False, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure egress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    self.__ecn = YANGDynClass(base=ecn.ecn, is_container='container', presence=False, yang_name="ecn", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'full', u'callpoint': u'qos_red_profile_ecn'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    self.__rcv_queue = YANGDynClass(base=rcv_queue.rcv_queue, is_container='container', presence=False, yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ingress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    self.__red_profile = YANGDynClass(base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)

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
      t = YANGDynClass(v,base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__map_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_(self):
    self.__map_ = YANGDynClass(base=map_.map_, is_container='container', presence=False, yang_name="map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure QoS map', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


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
      t = YANGDynClass(v,base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """red_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)""",
        })

    self.__red_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_red_profile(self):
    self.__red_profile = YANGDynClass(base=YANGListType("profile_id",red_profile.red_profile, yang_name="red-profile", rest_name="red-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-id', extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}), is_container='list', yang_name="red-profile", rest_name="red-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RED profiles', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'qos_red_profile'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)


  def _get_ecn(self):
    """
    Getter method for ecn, mapped from YANG variable /qos/ecn (container)
    """
    return self.__ecn
      
  def _set_ecn(self, v, load=False):
    """
    Setter method for ecn, mapped from YANG variable /qos/ecn (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ecn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ecn() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ecn.ecn, is_container='container', presence=False, yang_name="ecn", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'full', u'callpoint': u'qos_red_profile_ecn'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ecn must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ecn.ecn, is_container='container', presence=False, yang_name="ecn", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'full', u'callpoint': u'qos_red_profile_ecn'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__ecn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ecn(self):
    self.__ecn = YANGDynClass(base=ecn.ecn, is_container='container', presence=False, yang_name="ecn", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'47', u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'hidden': u'full', u'callpoint': u'qos_red_profile_ecn'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


  def _get_queue(self):
    """
    Getter method for queue, mapped from YANG variable /qos/queue (container)
    """
    return self.__queue
      
  def _set_queue(self, v, load=False):
    """
    Setter method for queue, mapped from YANG variable /qos/queue (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=queue.queue, is_container='container', presence=False, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure egress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=queue.queue, is_container='container', presence=False, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure egress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue(self):
    self.__queue = YANGDynClass(base=queue.queue, is_container='container', presence=False, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure egress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


  def _get_rcv_queue(self):
    """
    Getter method for rcv_queue, mapped from YANG variable /qos/rcv_queue (container)
    """
    return self.__rcv_queue
      
  def _set_rcv_queue(self, v, load=False):
    """
    Setter method for rcv_queue, mapped from YANG variable /qos/rcv_queue (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rcv_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rcv_queue() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rcv_queue.rcv_queue, is_container='container', presence=False, yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ingress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rcv_queue must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rcv_queue.rcv_queue, is_container='container', presence=False, yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ingress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__rcv_queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rcv_queue(self):
    self.__rcv_queue = YANGDynClass(base=rcv_queue.rcv_queue, is_container='container', presence=False, yang_name="rcv-queue", rest_name="rcv-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ingress queueing', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)

  map_ = __builtin__.property(_get_map_, _set_map_)
  red_profile = __builtin__.property(_get_red_profile, _set_red_profile)
  ecn = __builtin__.property(_get_ecn, _set_ecn)
  queue = __builtin__.property(_get_queue, _set_queue)
  rcv_queue = __builtin__.property(_get_rcv_queue, _set_rcv_queue)


  _pyangbind_elements = {'map_': map_, 'red_profile': red_profile, 'ecn': ecn, 'queue': queue, 'rcv_queue': rcv_queue, }


