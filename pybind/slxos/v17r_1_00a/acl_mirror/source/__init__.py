
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class source(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-access-list - based on the path /acl-mirror/source. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__src_interface_type','__src_interface_name','__destination','__dst_interface_type','__dst_interface_name',)

  _yang_name = 'source'
  _rest_name = 'source'

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
    self.__dst_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="dst-interface-name", rest_name="dst-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)
    self.__dst_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="dst-interface-type", rest_name="dst-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    self.__src_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="src-interface-name", rest_name="src-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)
    self.__src_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}},), is_leaf=True, yang_name="src-interface-type", rest_name="src-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)

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
      return [u'acl-mirror', u'source']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'acl-mirror', u'source']

  def _get_src_interface_type(self):
    """
    Getter method for src_interface_type, mapped from YANG variable /acl_mirror/source/src_interface_type (enumeration)
    """
    return self.__src_interface_type
      
  def _set_src_interface_type(self, v, load=False):
    """
    Setter method for src_interface_type, mapped from YANG variable /acl_mirror/source/src_interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_interface_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}},), is_leaf=True, yang_name="src-interface-type", rest_name="src-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}},), is_leaf=True, yang_name="src-interface-type", rest_name="src-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__src_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_interface_type(self):
    self.__src_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}},), is_leaf=True, yang_name="src-interface-type", rest_name="src-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)


  def _get_src_interface_name(self):
    """
    Getter method for src_interface_name, mapped from YANG variable /acl_mirror/source/src_interface_name (mirror-ifname)
    """
    return self.__src_interface_name
      
  def _set_src_interface_name(self, v, load=False):
    """
    Setter method for src_interface_name, mapped from YANG variable /acl_mirror/source/src_interface_name (mirror-ifname)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_src_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_src_interface_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="src-interface-name", rest_name="src-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """src_interface_name must be of a type compatible with mirror-ifname""",
          'defined-type': "brocade-ip-access-list:mirror-ifname",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="src-interface-name", rest_name="src-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)""",
        })

    self.__src_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_src_interface_name(self):
    self.__src_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="src-interface-name", rest_name="src-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)


  def _get_destination(self):
    """
    Getter method for destination, mapped from YANG variable /acl_mirror/source/destination (enumeration)
    """
    return self.__destination
      
  def _set_destination(self, v, load=False):
    """
    Setter method for destination, mapped from YANG variable /acl_mirror/source/destination (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination(self):
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'destination': {'value': 0}},), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)


  def _get_dst_interface_type(self):
    """
    Getter method for dst_interface_type, mapped from YANG variable /acl_mirror/source/dst_interface_type (enumeration)
    """
    return self.__dst_interface_type
      
  def _set_dst_interface_type(self, v, load=False):
    """
    Setter method for dst_interface_type, mapped from YANG variable /acl_mirror/source/dst_interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dst_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dst_interface_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="dst-interface-type", rest_name="dst-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dst_interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-access-list:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="dst-interface-type", rest_name="dst-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)""",
        })

    self.__dst_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dst_interface_type(self):
    self.__dst_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'port-channel': {'value': 3}},), is_leaf=True, yang_name="dst-interface-type", rest_name="dst-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='enumeration', is_config=True)


  def _get_dst_interface_name(self):
    """
    Getter method for dst_interface_name, mapped from YANG variable /acl_mirror/source/dst_interface_name (mirror-ifname)
    """
    return self.__dst_interface_name
      
  def _set_dst_interface_name(self, v, load=False):
    """
    Setter method for dst_interface_name, mapped from YANG variable /acl_mirror/source/dst_interface_name (mirror-ifname)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dst_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dst_interface_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="dst-interface-name", rest_name="dst-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dst_interface_name must be of a type compatible with mirror-ifname""",
          'defined-type': "brocade-ip-access-list:mirror-ifname",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="dst-interface-name", rest_name="dst-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)""",
        })

    self.__dst_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dst_interface_name(self):
    self.__dst_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|1[0-6])/([1-9]|[1-9][0-9])(:[1-4])?)|([1-9]|[1-9][0-9]|[1-9][0-9]{2}|[1-5][0-9]{3}|6[0-1][0-4]{2}))'}), is_leaf=True, yang_name="dst-interface-name", rest_name="dst-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='mirror-ifname', is_config=True)

  src_interface_type = __builtin__.property(_get_src_interface_type, _set_src_interface_type)
  src_interface_name = __builtin__.property(_get_src_interface_name, _set_src_interface_name)
  destination = __builtin__.property(_get_destination, _set_destination)
  dst_interface_type = __builtin__.property(_get_dst_interface_type, _set_dst_interface_type)
  dst_interface_name = __builtin__.property(_get_dst_interface_name, _set_dst_interface_name)


  _pyangbind_elements = {'src_interface_type': src_interface_type, 'src_interface_name': src_interface_name, 'destination': destination, 'dst_interface_type': dst_interface_type, 'dst_interface_name': dst_interface_name, }

