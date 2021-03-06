
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import nexthops
class prefix(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/fec/ldp-fec-prefixes/prefix. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__destination','__state','__ingress','__egress','__filtered','__lwd','__nexthops',)

  _yang_name = 'prefix'
  _rest_name = 'prefix'

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
    self.__ingress = YANGDynClass(base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__destination = YANGDynClass(base=unicode, is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__egress = YANGDynClass(base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__filtered = YANGDynClass(base=unicode, is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__lwd = YANGDynClass(base=unicode, is_leaf=True, yang_name="lwd", rest_name="lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__nexthops = YANGDynClass(base=YANGListType("nexthop",nexthops.nexthops, yang_name="nexthops", rest_name="nexthops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nexthop', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}), is_container='list', yang_name="nexthops", rest_name="nexthops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefixes', u'prefix']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefixes', u'prefix']

  def _get_destination(self):
    """
    Getter method for destination, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/destination (string)

    YANG Description: destination
    """
    return self.__destination
      
  def _set_destination(self, v, load=False):
    """
    Setter method for destination, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/destination (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination() directly.

    YANG Description: destination
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination(self):
    self.__destination = YANGDynClass(base=unicode, is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/state (string)

    YANG Description: state
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/state (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_ingress(self):
    """
    Getter method for ingress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/ingress (string)

    YANG Description: ingress
    """
    return self.__ingress
      
  def _set_ingress(self, v, load=False):
    """
    Setter method for ingress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/ingress (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress() directly.

    YANG Description: ingress
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__ingress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress(self):
    self.__ingress = YANGDynClass(base=unicode, is_leaf=True, yang_name="ingress", rest_name="ingress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_egress(self):
    """
    Getter method for egress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/egress (string)

    YANG Description: egress
    """
    return self.__egress
      
  def _set_egress(self, v, load=False):
    """
    Setter method for egress, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/egress (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress() directly.

    YANG Description: egress
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__egress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress(self):
    self.__egress = YANGDynClass(base=unicode, is_leaf=True, yang_name="egress", rest_name="egress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_filtered(self):
    """
    Getter method for filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/filtered (string)

    YANG Description: filtered
    """
    return self.__filtered
      
  def _set_filtered(self, v, load=False):
    """
    Setter method for filtered, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/filtered (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filtered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filtered() directly.

    YANG Description: filtered
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filtered must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__filtered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filtered(self):
    self.__filtered = YANGDynClass(base=unicode, is_leaf=True, yang_name="filtered", rest_name="filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_lwd(self):
    """
    Getter method for lwd, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/lwd (string)

    YANG Description: lwd
    """
    return self.__lwd
      
  def _set_lwd(self, v, load=False):
    """
    Setter method for lwd, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/lwd (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lwd() directly.

    YANG Description: lwd
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="lwd", rest_name="lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lwd must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="lwd", rest_name="lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__lwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lwd(self):
    self.__lwd = YANGDynClass(base=unicode, is_leaf=True, yang_name="lwd", rest_name="lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_nexthops(self):
    """
    Getter method for nexthops, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/nexthops (list)
    """
    return self.__nexthops
      
  def _set_nexthops(self, v, load=False):
    """
    Setter method for nexthops, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefixes/prefix/nexthops (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nexthops is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nexthops() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("nexthop",nexthops.nexthops, yang_name="nexthops", rest_name="nexthops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nexthop', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}), is_container='list', yang_name="nexthops", rest_name="nexthops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nexthops must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("nexthop",nexthops.nexthops, yang_name="nexthops", rest_name="nexthops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nexthop', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}), is_container='list', yang_name="nexthops", rest_name="nexthops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__nexthops = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nexthops(self):
    self.__nexthops = YANGDynClass(base=YANGListType("nexthop",nexthops.nexthops, yang_name="nexthops", rest_name="nexthops", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='nexthop', extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}), is_container='list', yang_name="nexthops", rest_name="nexthops", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-fec-prefix-interface-nexthops-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  destination = __builtin__.property(_get_destination)
  state = __builtin__.property(_get_state)
  ingress = __builtin__.property(_get_ingress)
  egress = __builtin__.property(_get_egress)
  filtered = __builtin__.property(_get_filtered)
  lwd = __builtin__.property(_get_lwd)
  nexthops = __builtin__.property(_get_nexthops)


  _pyangbind_elements = {'destination': destination, 'state': state, 'ingress': ingress, 'egress': egress, 'filtered': filtered, 'lwd': lwd, 'nexthops': nexthops, }


