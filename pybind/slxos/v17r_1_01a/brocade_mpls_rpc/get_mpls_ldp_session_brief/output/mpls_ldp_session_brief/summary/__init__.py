
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class summary(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/get-mpls-ldp-session-brief/output/mpls-ldp-session-brief/summary. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__peerLdpId','__state','__adjacency','__role','__maxHold','__timeLeft',)

  _yang_name = 'summary'
  _rest_name = 'summary'

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
    self.__maxHold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maxHold", rest_name="maxHold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__timeLeft = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeLeft", rest_name="timeLeft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__adjacency = YANGDynClass(base=unicode, is_leaf=True, yang_name="adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__peerLdpId = YANGDynClass(base=unicode, is_leaf=True, yang_name="peerLdpId", rest_name="peerLdpId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__role = YANGDynClass(base=unicode, is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

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
      return [u'brocade_mpls_rpc', u'get-mpls-ldp-session-brief', u'output', u'mpls-ldp-session-brief', u'summary']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-mpls-ldp-session-brief', u'output', u'mpls-ldp-session-brief', u'summary']

  def _get_peerLdpId(self):
    """
    Getter method for peerLdpId, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/peerLdpId (string)

    YANG Description: Peer LDP ID
    """
    return self.__peerLdpId
      
  def _set_peerLdpId(self, v, load=False):
    """
    Setter method for peerLdpId, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/peerLdpId (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peerLdpId is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peerLdpId() directly.

    YANG Description: Peer LDP ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="peerLdpId", rest_name="peerLdpId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peerLdpId must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="peerLdpId", rest_name="peerLdpId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__peerLdpId = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peerLdpId(self):
    self.__peerLdpId = YANGDynClass(base=unicode, is_leaf=True, yang_name="peerLdpId", rest_name="peerLdpId", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/state (string)

    YANG Description: Session State
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/state (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Session State
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=unicode, is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_adjacency(self):
    """
    Getter method for adjacency, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/adjacency (string)

    YANG Description: Adjacency Used
    """
    return self.__adjacency
      
  def _set_adjacency(self, v, load=False):
    """
    Setter method for adjacency, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/adjacency (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjacency is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjacency() directly.

    YANG Description: Adjacency Used
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjacency must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__adjacency = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjacency(self):
    self.__adjacency = YANGDynClass(base=unicode, is_leaf=True, yang_name="adjacency", rest_name="adjacency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_role(self):
    """
    Getter method for role, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/role (string)

    YANG Description: My Role
    """
    return self.__role
      
  def _set_role(self, v, load=False):
    """
    Setter method for role, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/role (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_role is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_role() directly.

    YANG Description: My Role
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """role must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__role = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_role(self):
    self.__role = YANGDynClass(base=unicode, is_leaf=True, yang_name="role", rest_name="role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_maxHold(self):
    """
    Getter method for maxHold, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/maxHold (uint32)

    YANG Description: Max Hold Time
    """
    return self.__maxHold
      
  def _set_maxHold(self, v, load=False):
    """
    Setter method for maxHold, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/maxHold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maxHold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maxHold() directly.

    YANG Description: Max Hold Time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maxHold", rest_name="maxHold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maxHold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maxHold", rest_name="maxHold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__maxHold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maxHold(self):
    self.__maxHold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="maxHold", rest_name="maxHold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_timeLeft(self):
    """
    Getter method for timeLeft, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/timeLeft (uint32)

    YANG Description: Hold time left
    """
    return self.__timeLeft
      
  def _set_timeLeft(self, v, load=False):
    """
    Setter method for timeLeft, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_session_brief/output/mpls_ldp_session_brief/summary/timeLeft (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeLeft is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeLeft() directly.

    YANG Description: Hold time left
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeLeft", rest_name="timeLeft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeLeft must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeLeft", rest_name="timeLeft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__timeLeft = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeLeft(self):
    self.__timeLeft = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeLeft", rest_name="timeLeft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  peerLdpId = __builtin__.property(_get_peerLdpId, _set_peerLdpId)
  state = __builtin__.property(_get_state, _set_state)
  adjacency = __builtin__.property(_get_adjacency, _set_adjacency)
  role = __builtin__.property(_get_role, _set_role)
  maxHold = __builtin__.property(_get_maxHold, _set_maxHold)
  timeLeft = __builtin__.property(_get_timeLeft, _set_timeLeft)


  _pyangbind_elements = {'peerLdpId': peerLdpId, 'state': state, 'adjacency': adjacency, 'role': role, 'maxHold': maxHold, 'timeLeft': timeLeft, }


