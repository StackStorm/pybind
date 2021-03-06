
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import log_adjacency
import log_bad_packet
class log(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/router/ospf/log. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__log_adjacency','__log_all','__log_bad_packet','__log_database','__log_retransmit',)

  _yang_name = 'log'
  _rest_name = 'log'

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
    self.__log_retransmit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-retransmit", rest_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging retransmit activity', u'alt-name': u'retransmit'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__log_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging everything', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__log_database = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging LSA activity', u'alt-name': u'database'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__log_adjacency = YANGDynClass(base=log_adjacency.log_adjacency, is_container='container', presence=True, yang_name="log-adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging adjacency changes', u'alt-name': u'adjacency'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__log_bad_packet = YANGDynClass(base=log_bad_packet.log_bad_packet, is_container='container', presence=True, yang_name="log-bad-packet", rest_name="bad-packet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging Bad packets', u'alt-name': u'bad-packet'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'log']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'router', u'ospf', u'log']

  def _get_log_adjacency(self):
    """
    Getter method for log_adjacency, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_adjacency (container)

    YANG Description: Configure logging for adjacency changes
    """
    return self.__log_adjacency
      
  def _set_log_adjacency(self, v, load=False):
    """
    Setter method for log_adjacency, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_adjacency (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_adjacency is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_adjacency() directly.

    YANG Description: Configure logging for adjacency changes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=log_adjacency.log_adjacency, is_container='container', presence=True, yang_name="log-adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging adjacency changes', u'alt-name': u'adjacency'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_adjacency must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=log_adjacency.log_adjacency, is_container='container', presence=True, yang_name="log-adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging adjacency changes', u'alt-name': u'adjacency'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__log_adjacency = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_adjacency(self):
    self.__log_adjacency = YANGDynClass(base=log_adjacency.log_adjacency, is_container='container', presence=True, yang_name="log-adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging adjacency changes', u'alt-name': u'adjacency'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_log_all(self):
    """
    Getter method for log_all, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_all (empty)

    YANG Description: Configure logging for everything
    """
    return self.__log_all
      
  def _set_log_all(self, v, load=False):
    """
    Setter method for log_all, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_all() directly.

    YANG Description: Configure logging for everything
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging everything', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging everything', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__log_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_all(self):
    self.__log_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging everything', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)


  def _get_log_bad_packet(self):
    """
    Getter method for log_bad_packet, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_bad_packet (container)

    YANG Description: Configure logging for bad packets
    """
    return self.__log_bad_packet
      
  def _set_log_bad_packet(self, v, load=False):
    """
    Setter method for log_bad_packet, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_bad_packet (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_bad_packet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_bad_packet() directly.

    YANG Description: Configure logging for bad packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=log_bad_packet.log_bad_packet, is_container='container', presence=True, yang_name="log-bad-packet", rest_name="bad-packet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging Bad packets', u'alt-name': u'bad-packet'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_bad_packet must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=log_bad_packet.log_bad_packet, is_container='container', presence=True, yang_name="log-bad-packet", rest_name="bad-packet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging Bad packets', u'alt-name': u'bad-packet'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__log_bad_packet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_bad_packet(self):
    self.__log_bad_packet = YANGDynClass(base=log_bad_packet.log_bad_packet, is_container='container', presence=True, yang_name="log-bad-packet", rest_name="bad-packet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Logging Bad packets', u'alt-name': u'bad-packet'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_log_database(self):
    """
    Getter method for log_database, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_database (empty)

    YANG Description: Configure logging for LSA activity
    """
    return self.__log_database
      
  def _set_log_database(self, v, load=False):
    """
    Setter method for log_database, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_database (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_database is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_database() directly.

    YANG Description: Configure logging for LSA activity
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log-database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging LSA activity', u'alt-name': u'database'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_database must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging LSA activity', u'alt-name': u'database'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__log_database = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_database(self):
    self.__log_database = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-database", rest_name="database", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging LSA activity', u'alt-name': u'database'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)


  def _get_log_retransmit(self):
    """
    Getter method for log_retransmit, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_retransmit (empty)

    YANG Description: Configure logging for retransmit activity
    """
    return self.__log_retransmit
      
  def _set_log_retransmit(self, v, load=False):
    """
    Setter method for log_retransmit, mapped from YANG variable /rbridge_id/ipv6/router/ospf/log/log_retransmit (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_log_retransmit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_log_retransmit() directly.

    YANG Description: Configure logging for retransmit activity
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="log-retransmit", rest_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging retransmit activity', u'alt-name': u'retransmit'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """log_retransmit must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-retransmit", rest_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging retransmit activity', u'alt-name': u'retransmit'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__log_retransmit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_log_retransmit(self):
    self.__log_retransmit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="log-retransmit", rest_name="retransmit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Logging retransmit activity', u'alt-name': u'retransmit'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)

  log_adjacency = __builtin__.property(_get_log_adjacency, _set_log_adjacency)
  log_all = __builtin__.property(_get_log_all, _set_log_all)
  log_bad_packet = __builtin__.property(_get_log_bad_packet, _set_log_bad_packet)
  log_database = __builtin__.property(_get_log_database, _set_log_database)
  log_retransmit = __builtin__.property(_get_log_retransmit, _set_log_retransmit)


  _pyangbind_elements = {'log_adjacency': log_adjacency, 'log_all': log_all, 'log_bad_packet': log_bad_packet, 'log_database': log_database, 'log_retransmit': log_retransmit, }


