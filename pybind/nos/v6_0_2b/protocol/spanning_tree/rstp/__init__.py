
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import error_disable_timeout
import port_channel
class rstp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/spanning-tree/rstp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__description','__bridge_priority','__error_disable_timeout','__forward_delay','__max_age','__port_channel','__shutdown','__hello_time','__transmit_holdcount',)

  _yang_name = 'rstp'
  _rest_name = 'rstp'

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
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree description', u'cli-multi-value': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='string', is_config=True)
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the hello interval for the spanning \ntree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(32768), is_leaf=True, yang_name="bridge-priority", rest_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority commands', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__error_disable_timeout = YANGDynClass(base=error_disable_timeout.error_disable_timeout, is_container='container', presence=False, yang_name="error-disable-timeout", rest_name="error-disable-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Error-disable-timeout for the spanning tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Turn off the spanning-tree protocol'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    self.__transmit_holdcount = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6), is_leaf=True, yang_name="transmit-holdcount", rest_name="transmit-holdcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Transmit hold count of the bridge', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__port_channel = YANGDynClass(base=port_channel.port_channel, is_container='container', presence=False, yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Controls behaviour of port-channel for spanning-tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    self.__forward_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(15), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)

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
      return [u'protocol', u'spanning-tree', u'rstp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'spanning-tree', u'rstp']

  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /protocol/spanning_tree/rstp/description (string)
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /protocol/spanning_tree/rstp/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree description', u'cli-multi-value': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree description', u'cli-multi-value': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0..64']}), default=unicode(""), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree description', u'cli-multi-value': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='string', is_config=True)


  def _get_bridge_priority(self):
    """
    Getter method for bridge_priority, mapped from YANG variable /protocol/spanning_tree/rstp/bridge_priority (uint32)
    """
    return self.__bridge_priority
      
  def _set_bridge_priority(self, v, load=False):
    """
    Setter method for bridge_priority, mapped from YANG variable /protocol/spanning_tree/rstp/bridge_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(32768), is_leaf=True, yang_name="bridge-priority", rest_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority commands', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(32768), is_leaf=True, yang_name="bridge-priority", rest_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority commands', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__bridge_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_priority(self):
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(32768), is_leaf=True, yang_name="bridge-priority", rest_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority commands', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_error_disable_timeout(self):
    """
    Getter method for error_disable_timeout, mapped from YANG variable /protocol/spanning_tree/rstp/error_disable_timeout (container)
    """
    return self.__error_disable_timeout
      
  def _set_error_disable_timeout(self, v, load=False):
    """
    Setter method for error_disable_timeout, mapped from YANG variable /protocol/spanning_tree/rstp/error_disable_timeout (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_error_disable_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_error_disable_timeout() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=error_disable_timeout.error_disable_timeout, is_container='container', presence=False, yang_name="error-disable-timeout", rest_name="error-disable-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Error-disable-timeout for the spanning tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """error_disable_timeout must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=error_disable_timeout.error_disable_timeout, is_container='container', presence=False, yang_name="error-disable-timeout", rest_name="error-disable-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Error-disable-timeout for the spanning tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__error_disable_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_error_disable_timeout(self):
    self.__error_disable_timeout = YANGDynClass(base=error_disable_timeout.error_disable_timeout, is_container='container', presence=False, yang_name="error-disable-timeout", rest_name="error-disable-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Error-disable-timeout for the spanning tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)


  def _get_forward_delay(self):
    """
    Getter method for forward_delay, mapped from YANG variable /protocol/spanning_tree/rstp/forward_delay (uint32)
    """
    return self.__forward_delay
      
  def _set_forward_delay(self, v, load=False):
    """
    Setter method for forward_delay, mapped from YANG variable /protocol/spanning_tree/rstp/forward_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forward_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forward_delay() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(15), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forward_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(15), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__forward_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forward_delay(self):
    self.__forward_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(15), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_max_age(self):
    """
    Getter method for max_age, mapped from YANG variable /protocol/spanning_tree/rstp/max_age (uint32)
    """
    return self.__max_age
      
  def _set_max_age(self, v, load=False):
    """
    Setter method for max_age, mapped from YANG variable /protocol/spanning_tree/rstp/max_age (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_age() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_age must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__max_age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_age(self):
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(20), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_port_channel(self):
    """
    Getter method for port_channel, mapped from YANG variable /protocol/spanning_tree/rstp/port_channel (container)
    """
    return self.__port_channel
      
  def _set_port_channel(self, v, load=False):
    """
    Setter method for port_channel, mapped from YANG variable /protocol/spanning_tree/rstp/port_channel (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_channel() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=port_channel.port_channel, is_container='container', presence=False, yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Controls behaviour of port-channel for spanning-tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_channel must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=port_channel.port_channel, is_container='container', presence=False, yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Controls behaviour of port-channel for spanning-tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__port_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_channel(self):
    self.__port_channel = YANGDynClass(base=port_channel.port_channel, is_container='container', presence=False, yang_name="port-channel", rest_name="port-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Controls behaviour of port-channel for spanning-tree', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)


  def _get_shutdown(self):
    """
    Getter method for shutdown, mapped from YANG variable /protocol/spanning_tree/rstp/shutdown (empty)
    """
    return self.__shutdown
      
  def _set_shutdown(self, v, load=False):
    """
    Setter method for shutdown, mapped from YANG variable /protocol/spanning_tree/rstp/shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Turn off the spanning-tree protocol'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Turn off the spanning-tree protocol'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)""",
        })

    self.__shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown(self):
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Turn off the spanning-tree protocol'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)


  def _get_hello_time(self):
    """
    Getter method for hello_time, mapped from YANG variable /protocol/spanning_tree/rstp/hello_time (uint32)
    """
    return self.__hello_time
      
  def _set_hello_time(self, v, load=False):
    """
    Setter method for hello_time, mapped from YANG variable /protocol/spanning_tree/rstp/hello_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the hello interval for the spanning \ntree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the hello interval for the spanning \ntree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__hello_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_time(self):
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the hello interval for the spanning \ntree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_transmit_holdcount(self):
    """
    Getter method for transmit_holdcount, mapped from YANG variable /protocol/spanning_tree/rstp/transmit_holdcount (uint32)
    """
    return self.__transmit_holdcount
      
  def _set_transmit_holdcount(self, v, load=False):
    """
    Setter method for transmit_holdcount, mapped from YANG variable /protocol/spanning_tree/rstp/transmit_holdcount (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transmit_holdcount is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transmit_holdcount() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6), is_leaf=True, yang_name="transmit-holdcount", rest_name="transmit-holdcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Transmit hold count of the bridge', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transmit_holdcount must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6), is_leaf=True, yang_name="transmit-holdcount", rest_name="transmit-holdcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Transmit hold count of the bridge', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__transmit_holdcount = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transmit_holdcount(self):
    self.__transmit_holdcount = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(6), is_leaf=True, yang_name="transmit-holdcount", rest_name="transmit-holdcount", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Transmit hold count of the bridge', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)

  description = __builtin__.property(_get_description, _set_description)
  bridge_priority = __builtin__.property(_get_bridge_priority, _set_bridge_priority)
  error_disable_timeout = __builtin__.property(_get_error_disable_timeout, _set_error_disable_timeout)
  forward_delay = __builtin__.property(_get_forward_delay, _set_forward_delay)
  max_age = __builtin__.property(_get_max_age, _set_max_age)
  port_channel = __builtin__.property(_get_port_channel, _set_port_channel)
  shutdown = __builtin__.property(_get_shutdown, _set_shutdown)
  hello_time = __builtin__.property(_get_hello_time, _set_hello_time)
  transmit_holdcount = __builtin__.property(_get_transmit_holdcount, _set_transmit_holdcount)


  _pyangbind_elements = {'description': description, 'bridge_priority': bridge_priority, 'error_disable_timeout': error_disable_timeout, 'forward_delay': forward_delay, 'max_age': max_age, 'port_channel': port_channel, 'shutdown': shutdown, 'hello_time': hello_time, 'transmit_holdcount': transmit_holdcount, }


