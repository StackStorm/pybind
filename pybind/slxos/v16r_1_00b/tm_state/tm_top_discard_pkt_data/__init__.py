
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tm_top_discard_pkt_data(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysdiag-operational - based on the path /tm-state/tm-top-discard-pkt-data. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: TM voq stats to get list of top discarded destination ports
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__slot','__tower','__id','__dest_port','__priority','__queue','__discardpkt',)

  _yang_name = 'tm-top-discard-pkt-data'
  _rest_name = 'tm-top-discard-pkt-data'

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
    self.__slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__queue = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)
    self.__discardpkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__dest_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-port", rest_name="dest-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)

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
      return [u'tm-state', u'tm-top-discard-pkt-data']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'tm-state', u'tm-top-discard-pkt-data']

  def _get_slot(self):
    """
    Getter method for slot, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/slot (uint16)

    YANG Description: slot id to get top discarded destination ports
    """
    return self.__slot
      
  def _set_slot(self, v, load=False):
    """
    Setter method for slot, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/slot (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot() directly.

    YANG Description: slot id to get top discarded destination ports
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__slot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot(self):
    self.__slot = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot", rest_name="slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_tower(self):
    """
    Getter method for tower, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/tower (uint16)

    YANG Description: tower id to get top discarded destination ports
    """
    return self.__tower
      
  def _set_tower(self, v, load=False):
    """
    Setter method for tower, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/tower (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tower is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tower() directly.

    YANG Description: tower id to get top discarded destination ports
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tower must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__tower = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tower(self):
    self.__tower = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="tower", rest_name="tower", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/id (uint16)

    YANG Description: unique id to get top discarded destination ports
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: unique id to get top discarded destination ports
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_dest_port(self):
    """
    Getter method for dest_port, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/dest_port (string)

    YANG Description: destination port having one of the highest discarded packets
    """
    return self.__dest_port
      
  def _set_dest_port(self, v, load=False):
    """
    Setter method for dest_port, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/dest_port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dest_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dest_port() directly.

    YANG Description: destination port having one of the highest discarded packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="dest-port", rest_name="dest-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dest_port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-port", rest_name="dest-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)""",
        })

    self.__dest_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dest_port(self):
    self.__dest_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="dest-port", rest_name="dest-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='string', is_config=False)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/priority (uint16)

    YANG Description: priority of the highest discarded packets
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/priority (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: priority of the highest discarded packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_queue(self):
    """
    Getter method for queue, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/queue (uint32)

    YANG Description: Queue id that is having discarded packets
    """
    return self.__queue
      
  def _set_queue(self, v, load=False):
    """
    Setter method for queue, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/queue (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue() directly.

    YANG Description: Queue id that is having discarded packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue(self):
    self.__queue = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue", rest_name="queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint32', is_config=False)


  def _get_discardpkt(self):
    """
    Getter method for discardpkt, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/discardpkt (uint64)

    YANG Description: count of the number of packets that are discarded
    """
    return self.__discardpkt
      
  def _set_discardpkt(self, v, load=False):
    """
    Setter method for discardpkt, mapped from YANG variable /tm_state/tm_top_discard_pkt_data/discardpkt (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_discardpkt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_discardpkt() directly.

    YANG Description: count of the number of packets that are discarded
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """discardpkt must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__discardpkt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_discardpkt(self):
    self.__discardpkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)

  slot = __builtin__.property(_get_slot)
  tower = __builtin__.property(_get_tower)
  id = __builtin__.property(_get_id)
  dest_port = __builtin__.property(_get_dest_port)
  priority = __builtin__.property(_get_priority)
  queue = __builtin__.property(_get_queue)
  discardpkt = __builtin__.property(_get_discardpkt)


  _pyangbind_elements = {'slot': slot, 'tower': tower, 'id': id, 'dest_port': dest_port, 'priority': priority, 'queue': queue, 'discardpkt': discardpkt, }


